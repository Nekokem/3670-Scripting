import maya.cmds as cmds

class ConstrainUI():
    def __init__(self):
        self.ConstrainWindow = 'ConstrainWindowSetting'
    
    def create(self):
        self.delete()

        self.ConstrainWindow = cmds.window(title = 'Constrain Window Settings', widthHeight=(500,500))
        self.colLayout = cmds.columnLayout(parent=self.ConstrainWindow, adjustableColumn=True )
        cmds.button(parent=self.colLayout, label='Constrain', command=lambda *x: self.ConstrainFunc())
        
        cmds.showWindow(self.ConstrainWindow)
    
    def delete(self):
        if cmds.window(self.ConstrainWindow, exists=True):
            cmds.deleteUI(self.ConstrainWindow)
    
    def ConstrainFunc(self):
        sel = cmds.ls(sl=True)
        
        if len(sel) % 2 == 1:
            cmds.error('Too many items!!')
        
        ctrls = sel[:len(sel)/2]
        jnts = sel[len(sel)/2:]
        
        for i in range(len(ctrls)):
            cmds.parentConstraint(ctrls[i], jnts[i])
            cmds.scaleConstraint(ctrls[i], jnts[i])          