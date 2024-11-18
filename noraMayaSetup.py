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

    def load_window_with_args(self, args):
        if cmds.window(self.win_name, ex=True):
            cmds.deleteUI(self.win_name)
        win = noraMain.NoraMain()
        win.show()

    def add_menu(self):
        nora_tools = cmds.menu('noraTools', parent='MayaWindow', label='Nora')
        nora_smc = cmds.menuItem('noraSMC', parent=nora_tools, label="SMC", command=self.load_window_with_args)
        return nora_tools