from importlib import reload
from xml.etree.ElementTree import tostring

from PySide6 import QtCore, QtWidgets
from NoraGeneral.UI import noraLoadDriverConfigWidget
from NoraGeneral.noraUtilities import *
from NoraUtilities import noraPoseGenerator
import json

reload(noraLoadDriverConfigWidget)

class NoraLoadDriverConfig(QtWidgets.QDialog, noraLoadDriverConfigWidget.Ui_noraLoadDriverConfigDialog):
    def __init__(self, parent=None):
        super(NoraLoadDriverConfig, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.loadDriverConfigLayout)

        self.label.setText("Driver Info: None")
        self.config = None
        self.pushButton.clicked.connect(self.load_config)

    def load_config(self):
        open_path = noraPoseGenerator.NoraPoseGeneratorWin.get_default_config_path()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption='读取配置',
            dir=open_path,
            filter='Configuration Files (*.json)')

        json_data = None
        if len(file_path) > 0:
            try:
                with open(file_path, 'rt') as readFile:
                    json_data = json.load(readFile)
            except ValueError as e:
                json_data = None
                print(e)

        if json_data is not None:
            self.config = noraPoseGenerator.NoraPoseGeneratorConfig([],
                                                                    [],
                                                                    json_data['num_samples'],
                                                                    json_data['start_frame'],
                                                                    json_data['controller_probability'],
                                                                    json_data['distribution'],
                                                                    json_data['sigma'])
            channels_list = json_data['channels']
            for c in channels_list:
                self.config.channels.append(noraPoseGenerator.ChannelInfo(**c))
            channel_limit = json_data['channel_min_max_values']
            for c in channel_limit:
                self.config.channel_min_max_values.append(noraPoseGenerator.NoraChannelMinMaxValue(**c))
            self.label.setText("Driver Info: " + str(len(channels_list)) + " channels")

    def get_matrix(self, start_frame: int, end_frame: int):
        """
        根据加载的驱动配置，获取channel值矩阵
        :return: frame x channel
        """
        if self.config is None:
            print("error: driver config is None")
            return None
        channel_num = len(self.config.channels)
        if channel_num == 0:
            return None
        frame_num = end_frame - start_frame
        channel_matrix = np.empty((frame_num, channel_num), dtype=float)
        cached_current_time = oma.MAnimControl.currentTime()
        for i in range(frame_num):
            t = i + start_frame
            oma.MAnimControl.setCurrentTime(om.MTime(t))
            for j in range(channel_num):
                channel_matrix[i, j] = float(cmds.getAttr(self.config.channels[j].name))
        oma.MAnimControl.setCurrentTime(cached_current_time)
        return channel_matrix
