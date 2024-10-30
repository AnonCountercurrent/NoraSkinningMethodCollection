import maya.api.OpenMaya as om


class NoraPolynomialFittingNode(om.MPxNode):
    id = om.MTypeId(0x00088601)
    inActive = om.MObject()
    inValues = om.MObject()
    outValue = om.MObject()

    @staticmethod
    def creator():
        return NoraPolynomialFittingNode()

    @staticmethod
    def initialize():
        # input
        n_attr = om.MFnNumericAttribute()
        NoraPolynomialFittingNode.inActive = n_attr.create("active", "ac", om.MFnNumericData.kBoolean, True)
        NoraPolynomialFittingNode.inValues = n_attr.create("inputValues", "in", om.MFnNumericData.kFloat)
        n_attr.keyable = True
        n_attr.array = True
        n_attr.usesArrayDataBuilder = True
        n_attr.readable = False
        # output
        n_attr = om.MFnNumericAttribute()
        NoraPolynomialFittingNode.outValue = n_attr.create("outputValue", "out", om.MFnNumericData.kFloat, 0.0)
        # add attributes
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.inActive)
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.inValues)
        NoraPolynomialFittingNode.addAttribute(NoraPolynomialFittingNode.outValue)
        NoraPolynomialFittingNode.attributeAffects(NoraPolynomialFittingNode.inValues, NoraPolynomialFittingNode.outValue)
        NoraPolynomialFittingNode.attributeAffects(NoraPolynomialFittingNode.inActive, NoraPolynomialFittingNode.outValue)

    def __init__(self):
        om.MPxNode.__init__(self)

    def compute(self, plug, data):
        return None

