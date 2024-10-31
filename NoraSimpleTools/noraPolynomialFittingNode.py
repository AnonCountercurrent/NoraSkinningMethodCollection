import maya.api.OpenMaya as om
import maya.cmds as cmds
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from NoraGeneral.noraUtilities import *
import numpy as np


class NoraPolynomialFittingNode(om.MPxNode):
    id = om.MTypeId(0x00088601)
    inActivated = om.MObject()
    inDefaultValue = om.MObject()
    inDegree = om.MObject()
    inIntercept = om.MObject()
    inCoefficients = om.MObject()
    inRadians = om.MObject()
    inValues = om.MObject()
    outValue = om.MObject()

    @staticmethod
    def creator():
        return NoraPolynomialFittingNode()

    @staticmethod
    def initialize():
        # input
        n_attr = om.MFnNumericAttribute()
        NoraPolynomialFittingNode.inActivated = n_attr.create("activated", "ac", om.MFnNumericData.kBoolean, False)
        NoraPolynomialFittingNode.inDefaultValue = n_attr.create("defaultValue", "dv", om.MFnNumericData.kDouble, 0.0)
        NoraPolynomialFittingNode.inDegree = n_attr.create("degree", "deg", om.MFnNumericData.kInt, 1)
        n_attr.setMin(1)
        n_attr.setMax(16)
        NoraPolynomialFittingNode.inIntercept = n_attr.create("intercept", "inter", om.MFnNumericData.kDouble, 0.0)
        NoraPolynomialFittingNode.inCoefficients = n_attr.create("coefficients", "coef", om.MFnNumericData.kDouble)
        n_attr.array = True
        n_attr.usesArrayDataBuilder = True
        NoraPolynomialFittingNode.inRadians = n_attr.create("radians", "ra", om.MFnNumericData.kBoolean)
        n_attr.array = True
        n_attr.usesArrayDataBuilder = True
        NoraPolynomialFittingNode.inValues = n_attr.create("inputValues", "in", om.MFnNumericData.kDouble)
        n_attr.keyable = True
        n_attr.array = True
        n_attr.usesArrayDataBuilder = True
        n_attr.readable = False
        # output
        n_attr = om.MFnNumericAttribute()
        NoraPolynomialFittingNode.outValue = n_attr.create("outputValue", "out", om.MFnNumericData.kDouble, 0.0)
        # add attributes
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.inActivated)
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.inDefaultValue)
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.inDegree)
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.inIntercept)
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.inCoefficients)
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.inRadians)
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.inValues)
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.outValue)
        NoraPolynomialFittingNode.attributeAffects(NoraPolynomialFittingNode.inValues, NoraPolynomialFittingNode.outValue)
        NoraPolynomialFittingNode.attributeAffects(NoraPolynomialFittingNode.inActivated, NoraPolynomialFittingNode.outValue)

    def __init__(self):
        om.MPxNode.__init__(self)

    def compute(self, plug:om.MPlug, data:om.MDataBlock):
        if plug == NoraPolynomialFittingNode.outValue or plug == NoraPolynomialFittingNode.inActivated:
            # 输入和数据
            active_data = data.inputValue(NoraPolynomialFittingNode.inActivated) # MDataHandle
            default_data = data.inputValue(NoraPolynomialFittingNode.inDefaultValue)
            degree_data = data.inputValue(NoraPolynomialFittingNode.inDegree)
            intercept_data = data.inputValue(NoraPolynomialFittingNode.inIntercept)
            coefficients_data = data.inputArrayValue(NoraPolynomialFittingNode.inCoefficients) # MArrayDataHandle
            radians_data = data.inputArrayValue(NoraPolynomialFittingNode.inRadians)
            input_values_data = data.inputArrayValue(NoraPolynomialFittingNode.inValues)
            # 输出句柄
            out_handle = data.outputValue(NoraPolynomialFittingNode.outValue)
            # 未激活输出默认值
            active_value = active_data.asBool()
            default_value = default_data.asDouble()
            if not active_value:
                out_handle.setDouble(default_value)
                data.setClean(plug)
                return None
            # 取值
            degree_value = degree_data.asInt()
            intercept_value = intercept_data.asDouble()
            # 获取系数
            coefficient_num = len(coefficients_data)
            coefficient_values = np.empty(coefficient_num, dtype=nora_scalar_type)
            for i in range(coefficient_num):
                coefficients_data.jumpToLogicalElement(i)
                coefficient_values[i] = coefficients_data.inputValue().asDouble()
            # 获取输入
            input_value_num = len(input_values_data)
            input_values = np.empty((1, input_value_num), dtype=nora_scalar_type)
            for i in range(input_value_num):
                radians_data.jumpToLogicalElement(i)
                input_values_data.jumpToLogicalElement(i)
                if radians_data.inputValue().asBool():
                    input_values[0, i] = math.radians(input_values_data.inputValue().asDouble())
                else:
                    input_values[0, i] = input_values_data.inputValue().asDouble()
            # 构造回归模型，并计算结果
            poly_features = PolynomialFeatures(degree=degree_value, include_bias=False)
            input_values_transformed = poly_features.fit_transform(input_values)
            model = LinearRegression()
            model.coef_ = coefficient_values
            model.intercept_ = intercept_value
            final_value = model.predict(input_values_transformed)
            # 输出
            out_handle = data.outputValue(NoraPolynomialFittingNode.outValue)
            out_handle.setDouble(final_value[0])
            data.setClean(plug)
        return None

    @staticmethod
    def custom_create_node(input_channels:list, output_channel:str, degree:int, default_value:float, intercept:float, coefficients:np.ndarray, radians=False):
        """
        用于创建这个节点
        """
        driver_num = len(input_channels)
        # 创建节点和连线
        node_name = cmds.createNode("noraPolynomialFitting")
        for i in range(driver_num):
            cmds.connectAttr(input_channels[i], f"{node_name}.inputValues[{i}]")
            if radians and is_rotation_attribute(input_channels[i]):
                cmds.setAttr(f"{node_name}.radians[{i}]", True)
            else:
                cmds.setAttr(f"{node_name}.radians[{i}]", False)
        cmds.connectAttr(f"{node_name}.outputValue", output_channel, force=True)
        # 数据写入
        cmds.setAttr(f"{node_name}.defaultValue", default_value)
        cmds.setAttr(f"{node_name}.degree", degree)
        cmds.setAttr(f"{node_name}.intercept", intercept)
        for i in range(coefficients.size):
            cmds.setAttr(f"{node_name}.coefficients[{i}]", coefficients[i])
        cmds.setAttr(f"{node_name}.activated", True)
