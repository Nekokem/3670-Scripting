import maya.cmds as cmds

class RandomPlacementUI():
    def __init__(self):
        self.RandomPlacement_Window = 'RandomPlacementWinderSetting'
            
    
    def create(self):
        self.delete()
        
        self.RandomPlacement_Window = cmds.window(title = 'Renamer Window Settings', widthHeight=(500,500))
        self.colLayout = cmds.columnLayout(parent=self.Renamer_Window, adjustableColumn=True )
        self.numDups = cmds.intField(parent=self.colLayout, placeholderText = 'Num of Dupicates')
        self.minX = cmds.intField(parent=self.colLayout, placeholderText = 'X Minimun')
        self.maxX = cmds.intField(parent=self.colLayout, placeholderText = 'X Maximun')
        self.minY = cmds.intField(parent=self.colLayout, placeholderText = 'Y Minimun')
        self.maxY = cmds.intField(parent=self.colLayout, placeholderText = 'Y Maximun')
        self.minZ = cmds.intField(parent=self.colLayout, placeholderText = 'Z Minimun')
        self.maxZ = cmds.intField(parent=self.colLayout, placeholderText = 'Z Maximun')
        cmds.button(parent=self.colLayout, label='Set', command=lambda *x: self.RandomPlacement())
        
        cmds.showWindow(self.RandomPlacement_Window)
    
    def delete(self):
        if cmds.window(self.RandomPlacement_Window, exists=True):
            cmds.deleteUI(self.RandomPlacement_Window)


    def RandomPlacement(self):
        
        sel = cmds.ls(selection=True)
        numberOfDups = cmds.intField(self.numDups, q=True, int=True)
        minX = cmds.intField(self.minX, q=True, int=True)
        maxX = cmds.intField(self.maxX, q=True, int=True)
        minY = cmds.intField(self.minY, q=True, int=True)
        maxY = cmds.intField(self.maxY, q=True, int=True)
        maxZ = cmds.intField(self.maxZ, q=True, int=True)
    
        for obj in range(len(cmds.ls(selection=True))):
            index = obj
        
            for obj in range(numDuplicates):
                tempObj = (cmds.duplicate(sel[index]), rr=True)
                randomX = random.uniform(minX, maxX)
                randomY = random.uniform(minY, maxY)
                randomZ = random.uniform(minZ, maxZ)
            
                cmds.select(tempObj)
                cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ])  


RandomPlacement_Window = RandomPlacementUI()

RandomPlacement_Window.create()  