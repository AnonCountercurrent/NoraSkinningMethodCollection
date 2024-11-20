from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral import noraUtilities
from NoraUtilities.UI import noraJointSettingsWidget
from NoraGeneral import noraStringInput
from NoraGeneral import noraPathSelect
from NoraGeneral import noraFileList
from NoraGeneral import noraFrameRange

reload(noraUtilities)
from NoraGeneral.noraUtilities import *
reload(noraJointSettingsWidget)
reload(noraStringInput)
reload(noraPathSelect)
reload(noraFileList)
reload(noraFrameRange)


def get_title():
    return 'Joint Settings'


def get_ui():
    return NoraJointSettings()


def get_width():
    return 460


def get_height():
    return 580


def get_use_custom_front_style():
    return False


class NoraJointSettings(QtWidgets.QDialog, noraJointSettingsWidget.Ui_noraJointSettingsWidget):
    def __init__(self, parent=None):
        super(NoraJointSettings, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # UI
        self.frame_range = noraFrameRange.NoraFrameRange()
        self.rideVerticalLayout.addWidget(self.frame_range)
        self.file_list_widget = noraFileList.NoraFileList()
        self.file_list_widget.file_only = True
        self.rideVerticalLayout.addWidget(self.file_list_widget)
        self.output_widget = noraPathSelect.NoraPathSelect()
        self.rideVerticalLayout.addWidget(self.output_widget)
        self.socket_name_widget = noraStringInput.NoraStringInput()
        self.socket_name_widget.label.setText("挂点名：")
        self.rideVerticalLayout.addWidget(self.socket_name_widget)

        # 事件绑定
        self.makeJointScaledUEStylePushButton.clicked.connect(self.make_selected_joint_scaled_ue_style)
        self.restBipPushButton.clicked.connect(self.rest_bip)

    @staticmethod
    def make_selected_joint_scaled_ue_style():
        selected_objects = cmds.ls(selection=True, long=True, objectsOnly=True)
        for obj in selected_objects:
            object_type = cmds.objectType(obj)
            if object_type == 'joint':
                cmds.setAttr(f"{obj}.segmentScaleCompensate", True)
                parent = get_parent_joint(obj)
                if parent:
                    cmds.connectAttr(f"{parent}.scaleX", f"{obj}.scaleX", force=True)
                    cmds.connectAttr(f"{parent}.scaleY", f"{obj}.scaleY", force=True)
                    cmds.connectAttr(f"{parent}.scaleZ", f"{obj}.scaleZ", force=True)

    def rest_bip(self):
        cmds.autoKeyframe(state=False)
        source_files = self.file_list_widget.get_file_list()
        if len(source_files) != 2:
            print("len(source_files) != 2")
            return
        start_frame = self.frame_range.start_frame
        end_frame = self.frame_range.end_frame
        if end_frame < start_frame:
            print('end_frame < start_frame')
            return
        socket_name = self.socket_name_widget.text
        if len(socket_name) == 0:
            print('socket_name == 0')
            return

        # 有挂点的文件
        source_file = source_files[0]
        source_file_name = source_file.split('/')[-1].split('.')[0]
        source_file_type = source_file.split('.')[-1]
        try:
            # 打开带有挂点的文件
            cmds.file(source_file, o=True, type=self.file_list_widget.typeDict[source_file_type], ignoreVersion=True, options=self.file_list_widget.optionsDict[source_file_type], force=True)
            # 获取空间名
            source_file_namespaces = cmds.namespaceInfo(listOnlyNamespaces=True, recurse=True)
            source_file_namespaces = [item for item in source_file_namespaces if item not in ['UI', 'shared']]
            # 导入引用
            import_reference()
        except Exception as error:
            print('---- {0} import Failed. {1}'.format(source_file, error))
        cmds.currentUnit(time='ntsc')

        # 导入有错误没关系，先找到输入的Socket
        cached_socket_transforms = []
        socket_long_name = None
        for namespace in source_file_namespaces:
            if cmds.objExists(namespace + ":" + socket_name):
                socket_long_name = namespace + ":" + socket_name
                break
        if source_file_name is None:
            print('can not found socket name')
            return
        for t in range(start_frame, end_frame + 1):
            current_time = om.MTime(t, om.MTime.k30FPS)
            oma.MAnimControl.setCurrentTime(current_time)
            ts = get_dag_path_by_name(socket_long_name).inclusiveMatrix()
            cached_socket_transforms.append(ts)

        # 输出的动画
        fbx_file = source_files[1]
        fbx_file_name = fbx_file.split('/')[-1].split('.')[0]
        fbx_file_type = fbx_file.split('.')[-1]
        try:
            cmds.file(fbx_file, o=True, type=self.file_list_widget.typeDict[fbx_file_type], ignoreVersion=True, options=self.file_list_widget.optionsDict[fbx_file_type], force=True)
        except Exception as error:
            print('---- {0} import Failed. {1}'.format(source_file, error))
        cmds.currentUnit(time='ntsc')

        # 缓存 root 和 bip001 变换
        cached_root_transforms = []
        cached_bip_transforms = []
        root_path = get_dag_path_by_name('Root')
        bip_path = get_dag_path_by_name('Bip001')
        for t in range(start_frame, end_frame + 1):
            current_time = om.MTime(t, om.MTime.k30FPS)
            oma.MAnimControl.setCurrentTime(current_time)
            cached_root_transforms.append(root_path.inclusiveMatrix())
            cached_bip_transforms.append(bip_path.inclusiveMatrix())

        # 计算移除挂点动画后的位置
        root_ts_fn = om.MFnTransform(root_path)
        bip_ts_fn = om.MFnTransform(bip_path)
        cmds.autoKeyframe(state=True)
        frame_num = end_frame - start_frame + 1
        for i in range(frame_num):
            current_time = om.MTime(i + start_frame, om.MTime.k30FPS)
            oma.MAnimControl.setCurrentTime(current_time)
            # 计算位置
            bip_ts = cached_bip_transforms[i]
            socket_ts = cached_socket_transforms[i]
            root_ts = cached_root_transforms[i]
            bip_ts_local = om.MTransformationMatrix(bip_ts * socket_ts.inverse()) # man! what can I say! maya 矩阵右乘，请记好
            root_ts_local =  om.MTransformationMatrix(root_ts * socket_ts.inverse())
            root_ts_fn.setTranslation(root_ts_local.translation(om.MSpace.kWorld), om.MSpace.kWorld)
            root_ts_fn.setRotation(root_ts_local.rotation(asQuaternion=True), om.MSpace.kWorld)
            bip_ts_fn.setTranslation(bip_ts_local.translation(om.MSpace.kWorld), om.MSpace.kWorld)
            bip_ts_fn.setRotation(bip_ts_local.rotation(asQuaternion=True), om.MSpace.kWorld)
            # 设置关键帧
            cmds.setKeyframe(root_path.fullPathName(), attribute='translate')
            cmds.setKeyframe(root_path.fullPathName(), attribute='rotate')
            cmds.setKeyframe(bip_path.fullPathName(), attribute='translate')
            cmds.setKeyframe(bip_path.fullPathName(), attribute='rotate')
        cmds.autoKeyframe(state=False)

