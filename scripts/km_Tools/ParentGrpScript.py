import maya.cmds as cmds

class ParentGroupUI():
    def __init__(self):
         self.ParentGrpWindow = 'ParentGrpWindowSetting'
    
    def create(self):
        self.delete()

        self.ParentGrpWindow = cmds.window(title = 'ParentGrp Window Settings', widthHeight=(500,500))
        self.colLayout = cmds.columnLayout(parent=self.ParentGrpWindow, adjustableColumn=True )
        cmds.button(parent=self.colLayout, label='Group', command=lambda *x: self.ParentGroupFunc())
        
        cmds.showWindow(self.ParentGrpWindow)
    
    def delete(self):
        if cmds.window(self.ParentGrpWindow, exists=True):
            cmds.deleteUI(self.ParentGrpWindow)
    
    def ParentGroupFunc(self):
        #select the objects
        self.sel = cmds.ls(selection=True)
        
        for self.s in self.sel:
        #group them together
            self.Grps = cmds.group(em=True)
        #match the transformations of the selection
            cmds.parent(self.s, self.Grps)
            