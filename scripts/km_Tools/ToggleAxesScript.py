import maya.cmds as cmds

class ToggleAxes():
   def __init__(self):
         self.ToggleWindow = 'ToggleWindowSetting'
    
   def create(self):
       
       self.delete()

       self.ToggleWindow = cmds.window(title = 'Toggle Axes Window Settings', widthHeight=(500,500))
       self.colLayout = cmds.columnLayout(parent=self.ToggleWindow, adjustableColumn=True )
       cmds.button(parent=self.colLayout, label='toggle', command=lambda *x: self.Toggle())

       cmds.showWindow(self.ToggleWindow)
    
   def delete(self):
       if cmds.window(self.ToggleWindow, exists=True):
           cmds.deleteUI(self.ToggleWindow)
   def Toggle(self):
       sels = cmds.ls(selection=True)
        
       for sel in sels:
           cmds.setAttr(sel + '.jointOrientX', cb=True)
           cmds.setAttr(sel + '.jointOrientY', cb=True)
           cmds.setAttr(sel + '.jointOrientZ', cb=True)
           cmds.setAttr(sel + '.displayLocalAxis', cb=True)
           if cmds.getAttr(sel + '.displayLocalAxis')==0:
               cmds.setAttr(sel + '.displayLocalAxis', 1)
           else:
               cmds.setAttr(sel + '.displayLocalAxis', 0)                  