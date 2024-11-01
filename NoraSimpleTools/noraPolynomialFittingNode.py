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
        NoraPolynomialFittingNode.attributeAffects(NoraPolynomialFittingNode.inDefaultValue, NoraPolynomialFittingNode.outValue)

    def __init__(self):
        om.MPxNode.__init__(self)

    def compute(self, plug:om.MPlug, data:om.MDataBlock):
        if plug == NoraPolynomialFittingNode.outValue:
            # 输入和数据
            active_handle = data.inputValue(NoraPolynomialFittingNode.inActivated) # MDataHandle
            default_handle = data.inputValue(NoraPolynomialFittingNode.inDefaultValue)
            degree_handle = data.inputValue(NoraPolynomialFittingNode.inDegree)
            intercept_handle = data.inputValue(NoraPolynomialFittingNode.inIntercept)
            coefficients_handle = data.inputArrayValue(NoraPolynomialFittingNode.inCoefficients) # MArrayDataHandle
            radians_handle = data.inputArrayValue(NoraPolynomialFittingNode.inRadians)
            input_values_handle = data.inputArrayValue(NoraPolynomialFittingNode.inValues)
            # 输出句柄
            out_handle = data.outputValue(NoraPolynomialFittingNode.outValue)
            # 未激活输出默认值
            active_value = active_handle.asBool()
            default_value = default_handle.asDouble()
            if not active_value:
                out_handle.setDouble(default_value)
                data.setClean(plug)
                return None
            # 取值
            degree_value = degree_handle.asInt()
            intercept_value = intercept_handle.asDouble()
            # 获取系数
            coefficient_num = len(coefficients_handle)
            coefficient_values = np.empty(coefficient_num, dtype=nora_scalar_type)
            for i in range(coefficient_num):
                coefficients_handle.jumpToLogicalElement(i)
                coefficient_values[i] = coefficients_handle.inputValue().asDouble()
            # 获取输入
            input_value_num = len(input_values_handle)
            input_values = np.empty((1, input_value_num), dtype=nora_scalar_type)
            for i in range(input_value_num):
                radians_handle.jumpToLogicalElement(i)
                input_values_handle.jumpToLogicalElement(i)
                if radians_handle.inputValue().asBool():
                    input_values[0, i] = math.radians(input_values_handle.inputValue().asDouble())
                else:
                    input_values[0, i] = input_values_handle.inputValue().asDouble()
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
