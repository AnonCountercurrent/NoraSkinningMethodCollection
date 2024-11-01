import NoraSimpleTools.noraPolynomialFittingNode as noraFitNode
import maya.api.OpenMaya as om
import sys


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass


def initializePlugin(obj):
    plugin = om.MFnPlugin(obj, "NoraSMC", "1.0", "Any")
    try:
        plugin.registerNode("noraPolynomialFitting", noraFitNode.NoraPolynomialFittingNode.id, noraFitNode.NoraPolynomialFittingNode.creator, noraFitNode.NoraPolynomialFittingNode.initialize)
    except:
        sys.stderr.write("Failed to register noraPolynomialFitting node\n")
        raise


def uninitializePlugin(obj):
    plugin = om.MFnPlugin(obj)
    try:
        plugin.deregisterNode(noraFitNode.NoraPolynomialFittingNode.id)
    except:
        sys.stderr.write("Failed to deregister noraPolynomialFitting node\n")
        raise
