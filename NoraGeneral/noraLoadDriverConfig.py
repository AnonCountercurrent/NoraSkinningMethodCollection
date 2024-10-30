import math
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

        self.open_icon = self.style().standardIcon(getattr(QtWidgets.QStyle, "SP_DialogOpenButton"))
        self.pushButton.setIcon(self.open_icon)

        self.label.setText("驱动信息：None")
        self.config = None
        self.pushButton.clicked.connect(self.load_config)
        self.frameRangeButton.clicked.connect(self.set_frame_range)

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
            self.label.setText("驱动信息：" + str(len(channels_list)) + " channels")

    def set_frame_range(self):
        """
        设置动画条范围
        """
        if self.config is None:
            print("error: driver config is None")
            return None
        start_frame = self.config.start_frame
        frame_num = self.config.num_samples
        channel_num = len(self.config.channels)
        distribution = self.config.distribution
        if distribution == "combination":
            frame_num = int(np.prod(np.array([self.config.channels[c_idx].sample_num for c_idx in range(0, channel_num)], dtype=int)))
        end_frame = start_frame + frame_num
        cmds.playbackOptions(animationStartTime=0, animationEndTime=end_frame, minTime=0, maxTime=end_frame)


    def get_matrix(self, start_frame: int, end_frame: int, radians: bool):
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
        angular_channel_list = []
        for i in range(channel_num):
            angular_channel_list.append(is_rotation_attribute(self.config.channels[i].name))
        for i in range(frame_num):
            t = i + start_frame
            oma.MAnimControl.setCurrentTime(om.MTime(t))
            for j in range(channel_num):
                if radians and angular_channel_list[j]:
                    channel_matrix[i, j] = float(math.radians(cmds.getAttr(self.config.channels[j].name)))
                else:
                    channel_matrix[i, j] = float(cmds.getAttr(self.config.channels[j].name))
        oma.MAnimControl.setCurrentTime(cached_current_time)
        return channel_matrix
