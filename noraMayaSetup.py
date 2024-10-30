from importlib import reload
import maya.cmds as cmds
import maya.api.OpenMaya as om
import sys
import noraMain
import NoraSimpleTools.noraPolynomialFittingNode as noraFitNode
reload(noraMain)
reload(noraFitNode)


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


class NoraSMC:
    def __init__(self):
        self.win_name = 'noraSMCWin'
        if cmds.menuItem(self.win_name, ex=True):
            cmds.deleteUI(self.win_name)

    def load_window(self):
        if cmds.window(self.win_name, ex=True):
            cmds.deleteUI(self.win_name)
        win = noraMain.NoraMain()
        win.show()

