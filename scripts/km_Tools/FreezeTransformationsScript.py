import maya.cmds as cmds

class FreezeTransUI():
   def __init__(self):
       self.FreezeWindow = 'FreezeWindowSetting'
    
   def create(self):
       
       self.delete()

       self.FreezeWindow = cmds.window(title = 'Freeze Window Settings', widthHeight=(500,500))
       self.colLayout = cmds.columnLayout(parent=self.FreezeWindow, adjustableColumn=True )
       cmds.button(parent=self.colLayout, label='Freeze', command=lambda *x: self.FreezeTrans())

       cmds.showWindow(self.FreezeWindow)
    
   def delete(self):
       if cmds.window(self.FreezeWindow, exists=True):
           cmds.deleteUI(self.FreezeWindow)
            
   def FreezeTrans(self):
       self.sel = cmds.ls(selection=True)
       cmds.makeIdentity (self.sel, apply=True, t=1, r=1, s=1, n=0, pn=1)        