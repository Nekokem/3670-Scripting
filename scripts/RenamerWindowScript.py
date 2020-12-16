import maya.cmds as cmds

class RenamerUI():
    def __init__(self):
        self.Renamer_Window = 'RenamerWinderSetting'
            
    
    def create(self):
        self.delete()

        self.Renamer_Window = cmds.window(title = 'Renamer Window Settings', widthHeight=(500,500))
        self.colLayout = cmds.columnLayout(parent=self.Renamer_Window, adjustableColumn=True )
        self.name = cmds.textField(parent=self.colLayout, placeholderText = 'New Name')
        cmds.button(parent=self.colLayout, label='Rename', command=lambda *x: self.Renamer())
        
        cmds.showWindow(self.Renamer_Window)
    
    def delete(self):
        if cmds.window(self.Renamer_Window, exists=True):
            cmds.deleteUI(self.Renamer_Window)
    
    def Renamer(self):
        sel = cmds.ls(selection = True)
        selectionNum = 1
        stringName = cmds.textField(self.name, q=True, text=True) 
    
        for sels in sel:
            collectionCount = stringName.count('#')
            selParts = stringName.partition('#' * collectionCount)
            numSystem = str(selectionNum)
        
            if selParts[1]:
                print 'Numbers are sequential!'
                zeroFiller = numSystem.zfill(3)
                cmds.rename(selParts[0] + zeroFiller + selParts[2])
            else:
                print 'Not sequqntial! Figure out why!'

            selectionNum += 1              