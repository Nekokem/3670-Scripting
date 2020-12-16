import maya.cmds as cmds

class HistoryDeleteUI():
    def __init__(self):
        self.HistoryDeleteWindow = 'HistoryDeleteWindowSetting'
    
    def create(self):
        self.delete()

        self.HistoryDeleteWindow = cmds.window(title = 'Delete History Window Settings', widthHeight=(500,500))
        self.colLayout = cmds.columnLayout(parent=self.HistoryDeleteWindow, adjustableColumn=True )
        cmds.button(parent=self.colLayout, label='Delete', command=lambda *x: self.HistoryDelete())
        
        cmds.showWindow(self.HistoryDeleteWindow)
    
    def delete(self):
        if cmds.window(self.HistoryDeleteWindow, exists=True):
            cmds.deleteUI(self.HistoryDeleteWindow)
    
    def HistoryDelete(self):
        self.sel = cmds.ls(selection=True)
        cmds.delete(self.sel, ch=True)       