import os, sys
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
from maya import OpenMayaUI as omui
import maya.mel as mel
import maya.cmds as cmds
import numpy as np
import scipy as sp
from shiboken6 import wrapInstance
from PySide6 import QtWidgets
import math

nora_scalar_type = np.float64

class JointLimit:
    """
    关节约束信息
    """
    def __init__(self):
        self.min_rot_limit_x = 0.0
        self.max_rot_limit_x = 0.0
        self.min_rot_limit_y = 0.0
        self.max_rot_limit_y = 0.0
        self.min_rot_limit_z = 0.0
        self.max_rot_limit_z = 0.0
        self.has_min_rot_limit_x = False
        self.has_max_rot_limit_x = False
        self.has_min_rot_limit_y = False
        self.has_max_rot_limit_y = False
        self.has_min_rot_limit_z = False
        self.has_max_rot_limit_z = False


def get_maya_main_window():
    """
    :return: maya 主窗口句柄
    """
    maya_main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(maya_main_window_ptr), QtWidgets.QWidget)  # Maya Main Window


def get_icon_path(in_icon_name):
    """
    :param in_icon_name: 图片资源名
    :return: 图片完整路径
    """
    current_path = os.path.dirname(__file__)
    current_path = current_path[:len(current_path) - len('NoraGeneral')]
    icon_path = current_path + '/NoraIcon/' + in_icon_name
    return icon_path


def get_smc_path():
    """
    获取工具路径
    """
    current_path = os.path.dirname(__file__)
    current_path = current_path[:len(current_path) - len('NoraGeneral')]
    return current_path


def get_document_path():
    return os.path.expanduser(r'~\Documents')


def get_selected_dag_path():
    """
    :return: 返回当前选择的 dag path
    """
    dag_path = om.MDagPath()
    selection_ls = om.MGlobal.getActiveSelectionList()
    if selection_ls.isEmpty():
        pass
    else:
        dag_path = selection_ls.getDagPath(0)
    return dag_path


def get_selected_dag_name():
    sel = cmds.ls(selection=True)
    if len(sel) == 0:
        return ""
    else:
        return sel[0]


def get_dg_node_by_name(node_name):
    selection_list = om.MSelectionList()
    selection_list.add(node_name)
    node_obj = selection_list.getDependNode(0)
    return om.MFnDependencyNode(node_obj)


def get_dag_path_by_name(node_name):
    selection_list = om.MSelectionList()
    selection_list.add(node_name)
    node_path = selection_list.getDagPath(0)
    return node_path


def get_parent_joint(joint_name):
    """
    获取父关节
    """
    parents = cmds.listRelatives(joint_name, parent=True)
    # 检查是否有父对象
    if parents:
        parent_name = parents[0]
        # 检查父对象是否为 joint 类型
        if cmds.objectType(parent_name) == 'joint':
            return parent_name
        else:
            return None
    else:
        return None


def get_true_source(source):
    """
    递归查找输入到指定属性的实际源节点
    :param attribute: 属性名称，如 "pSphere1.rotateX"
    :return: 实际源节点的名称
    """
    # 检查连接的节点类型，如果是 unitConversion 等中间节点，递归查找输入
    node_name = source.split('.')[0]
    node_type = cmds.nodeType(node_name)
    if node_type in ["unitConversion"]:
        previous_attribute = cmds.listConnections(node_name + ".input", source=True, destination=False, plugs=True)
        if previous_attribute:
            return get_true_source(previous_attribute[0])
        else:
            return None
    # 返回实际的源节点
    return source


def split_float(in_float_value, max_value = 1000000.0):
    """
    将一个浮点数拆分为一个 浮点数 f 和一个除数 i， f/i = in_float_value
    """
    factor = int(0)
    current_value = in_float_value
    while True:
        new_value = in_float_value * pow(10, factor + 1)
        if new_value < max_value and factor < 6:
            factor += 1
            current_value = new_value
        else:
            break
    return current_value, factor


def get_split_float_str(in_float_value, max_value = 1000000.0):
    """
    用于复制到UE，将一个浮点数拆分为一个 f 和系数 c， c * f = in_float_value
    """
    f1, f2 = split_float(in_float_value, max_value)
    if f2 == 0:
        f2 = 1
    else:
        f2 = 1.0 / pow(10, f2)
    return f"(X={f1:.10f},Y={f2:.10f})"


def replace_fbx_asc_xxx(origin_str, force_hyphen=False):
    """
    Bip001FBXASC032RLFBXASC032Calf to Bip001-RL-Calf
    """
    out_str = str(origin_str)
    begin_index = 0
    while True:
        find_index = out_str.find('FBXASC', begin_index)
        if find_index == -1:
            break
        acs_code = out_str[find_index + 6 : find_index + 9]
        chr_str = str(chr(int(acs_code)))
        if force_hyphen:
            chr_str = '-'
        out_str = out_str[0:find_index] + chr_str + out_str[find_index + 9:]
        begin_index = find_index + 1
    return out_str


def get_attribute_values(attribute_name, node_name):
    """
    :return: 默认值，最小值，最大值
    """
    min_value = None
    max_value = None
    default_value = 0.0

    # If the attribute exists.
    if cmds.attributeQuery(attribute_name, node=node_name, exists=True):
        # If the minimum value exists.
        if cmds.attributeQuery(attribute_name, node=node_name, minExists=True):
            min_value = cmds.attributeQuery(attribute_name, node=node_name, minimum=True)[0]

        # If the maximum value exists.
        if cmds.attributeQuery(attribute_name, node=node_name, maxExists=True):
            max_value = cmds.attributeQuery(attribute_name, node=node_name, maximum=True)[0]

        # Get the default value.
        default_value = cmds.attributeQuery(attribute_name, node=node_name, listDefault=True)[0]

    return default_value, min_value, max_value


def is_rotation_attribute(full_name: str):
    """
    检查参数是不是旋转参数
    """
    if full_name.split('.')[1] in ["rotateX", "rotateY", "rotateZ"]:
        return True
    else:
        return False


def maya_double_array_to_ndarray(double_array):
    """
    用 MDoubleArray 创建 np.ndarray
    """
    length = len(double_array)
    np_array = np.empty(length, dtype=nora_scalar_type)
    for i in range(length):
        np_array[i] = double_array[i]
    return np_array


def get_channel_matrix(attribute_names, start_frame: int, end_frame: int, radians: bool):
    """
    获取参数矩阵 frame x channel
    """
    channel_num = len(attribute_names)
    angular_channel_list = []
    for i in range(channel_num):
        angular_channel_list.append(is_rotation_attribute(attribute_names[i]))
    frame_num = end_frame - start_frame
    channel_matrix = np.empty((frame_num, channel_num), dtype=nora_scalar_type)
    cached_current_time = oma.MAnimControl.currentTime()
    for i in range(frame_num):
        t = i + start_frame
        oma.MAnimControl.setCurrentTime(om.MTime(t))
        for j in range(channel_num):
            if radians and angular_channel_list[j]:
                channel_matrix[i, j] = float(math.radians(cmds.getAttr(attribute_names[j])))
            else:
                channel_matrix[i, j] = float(cmds.getAttr(attribute_names[j]))
    oma.MAnimControl.setCurrentTime(cached_current_time)
    return channel_matrix


def get_rotation_limits(joint_name, object_type_string):
    """
    获取关节上的角度约束
    """
    limit_info = JointLimit()

    if not object_type_string:
        object_type_string = cmds.objectType(joint_name)

    if object_type_string != 'joint':
        return False, limit_info

    # Get joint limits.
    query_results = cmds.joint(
        joint_name,
        q=True,
        limitSwitchX=True,
        limitSwitchY=True,
        limitSwitchZ=True,
        limitX=True,
        limitY=True,
        limitZ=True)

    limit_info.min_rot_limit_x = query_results[0]
    limit_info.max_rot_limit_x = query_results[1]
    limit_info.min_rot_limit_y = query_results[2]
    limit_info.max_rot_limit_y = query_results[3]
    limit_info.min_rot_limit_z = query_results[4]
    limit_info.max_rot_limit_z = query_results[5]
    limit_info.has_min_rot_limit_x = query_results[6]
    limit_info.has_max_rot_limit_x = query_results[7]
    limit_info.has_min_rot_limit_y = query_results[8]
    limit_info.has_max_rot_limit_y = query_results[9]
    limit_info.has_min_rot_limit_z = query_results[10]
    limit_info.has_max_rot_limit_z = query_results[11]
    return True, limit_info


def apply_maya_limits(long_channel_name, limit_info, min_value, max_value):
    """
    将所需通道的最大值最小值返回
    """
    if long_channel_name == 'rotateX':
        if limit_info.has_min_rot_limit_x:
            min_value = limit_info.min_rot_limit_x
        if limit_info.has_max_rot_limit_x:
            max_value = limit_info.max_rot_limit_x
    elif long_channel_name == 'rotateY':
        if limit_info.has_min_rot_limit_y:
            min_value = limit_info.min_rot_limit_y
        if limit_info.has_max_rot_limit_y:
            max_value = limit_info.max_rot_limit_y
    elif long_channel_name == 'rotateZ':
        if limit_info.has_min_rot_limit_z:
            min_value = limit_info.min_rot_limit_z
        if limit_info.has_max_rot_limit_z:
            max_value = limit_info.max_rot_limit_z

    return min_value, max_value


def get_attribute_group_name(attribute_name, node_name):
    """
    获取channel所在的组
    """
    short_object_name = cmds.ls(node_name)[0]
    if cmds.attributeQuery(attribute_name, node=node_name, exists=True):
        parent_attribute = cmds.attributeQuery(attribute_name, node=node_name, listParent=True)
        if parent_attribute:
            return short_object_name + "." + parent_attribute[0]
    return short_object_name + "." + attribute_name


def get_short_name(obj):
    """
    获取对象短名
    """
    short_object_name = cmds.ls(obj)[0]
    pipe_index = short_object_name.rfind('|')
    if pipe_index != -1:
        short_object_name = short_object_name[pipe_index + 1:]
    return short_object_name


def set_keyframes(ctrl_name, attr_name, key_times, key_values):
    """
    连接曲线节点到给定端口，并设置帧
    """
    # 选择输入的管道
    sel_list = om.MSelectionList()
    sel_list.add("{0}.{1}".format(ctrl_name, attr_name))
    mplug = sel_list.getPlug(0)
    # 获取直连管道的曲线节点
    curve_node = oma.MFnAnimCurve(mplug)
    # 如果这个曲线节点不存在就创建一个
    try:
        curve_node.name()
    except:
        curve_node.create(mplug)

    # 先把旧关键帧移除
    # 移除所有
    # while curve_node.numKeys != 0:
    #     curve_node.remove(curve_node.numKeys - 1)
    # 仅移除重叠部分
    for key_time in key_times:
        found_key_index = curve_node.find(key_time)
        if found_key_index is not None:
            curve_node.remove(found_key_index)

    # 如果是角度类的曲线，转换成弧度
    angular_types = [oma.MFnAnimCurve.kAnimCurveTA, oma.MFnAnimCurve.kAnimCurveUA]
    if curve_node.animCurveType in angular_types:
        key_values = [math.radians(i) for i in key_values]
    # 设置帧
    curve_node.addKeys(
        key_times,
        key_values,
        oma.MFnAnimCurve.kTangentStep,
        oma.MFnAnimCurve.kTangentStep,
        True)


class NoraProgressBar:
    """
    进度条
    """
    def __init__(self):
        self.main_progress_bar = None

    def start_progress_bar(self, status_text='Processing...', interruptable=True, max_value=100):
        """
        创建新的进度
        """
        if self.main_progress_bar:
            self.stop_progress_bar()
        # 获取maya主窗体上的进度条
        self.main_progress_bar = mel.eval('$tmp = $gMainProgressBar')
        # 配置进度条
        cmds.progressBar(
            self.main_progress_bar,
            edit=True,
            beginProgress=True,
            isInterruptable=interruptable,
            status=status_text,
            maxValue=max_value)

    def set_progress_bar_value(self, progress_percentage):
        """
        设置进度
        """
        cmds.progressBar(self.main_progress_bar, edit=True, progress=progress_percentage)

    def is_progress_bar_cancelled(self):
        """
        返回是否取消了
        """
        if self.main_progress_bar:
            exists = cmds.progressBar(self.main_progress_bar, query=True, exists=True)
            if exists:
                result = cmds.progressBar(self.main_progress_bar, query=True, isCancelled=True)
                if result:
                    self.stop_progress_bar()
                return result
        return False

    def stop_progress_bar(self):
        """
        结束进度条
        """
        if self.main_progress_bar:
            cmds.progressBar(self.main_progress_bar, edit=True, endProgress=True)
        self.main_progress_bar = None