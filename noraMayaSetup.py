from importlib import reload
import maya.cmds as cmds
import noraMain
reload(noraMain)


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

