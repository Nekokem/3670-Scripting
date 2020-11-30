import maya.cmds as cmds

class RandomPlacementUI():
    def __init__(self):
        self.RandomPlacement_Window = 'RandomPlacementWinderSetting'
            
    
    def create(self):
        self.delete()
        
        self.RandomPlacement_Window = cmds.window(title = 'RandomePlacement Window Settings', widthHeight=(500,500))
        self.colLayout = cmds.columnLayout(parent=self.RandomePlacement_Window, adjustableColumn=True )
        cmds.text(label="Number of Duplicates", parent = self.layout_var)
        self.numDups = cmds.intField(parent=self.colLayout)
        cmds.text(label="Minimun X", parent = self.layout_var)
        self.minX = cmds.intField(parent=self.colLayout)
        cmds.text(label="Maximun X", parent = self.layout_var)
        self.maxX = cmds.intField(parent=self.colLayout)
        cmds.text(label="Minimun Y", parent = self.layout_var)
        self.minY = cmds.intField(parent=self.colLayout)
        cmds.text(label="Maximun Y", parent = self.layout_var)
        self.maxY = cmds.intField(parent=self.colLayout)
        cmds.text(label="Minimun Z", parent = self.layout_var)
        self.minZ = cmds.intField(parent=self.colLayout)
        cmds.text(label="Maximun Z", parent = self.layout_var)
        self.maxZ = cmds.intField(parent=self.colLayout)
        cmds.button(parent=self.colLayout, label='Set', command=lambda *x: self.RandomPlacement())
        
        cmds.showWindow(self.RandomPlacement_Window)
    
    def delete(self):
        if cmds.window(self.RandomPlacement_Window, exists=True):
            cmds.deleteUI(self.RandomPlacement_Window)


    def RandomPlacement(self):
        
        sel = cmds.ls(selection=True)
        numberOfDups = cmds.intField(self.numDups, q=True, int=True)
        min_X = cmds.intField(self.minX, q=True, int=True)
        max_X = cmds.intField(self.maxX, q=True, int=True)
        min_Y = cmds.intField(self.minY, q=True, int=True)
        max_Y = cmds.intField(self.maxY, q=True, int=True)
        min_Z = cmds.intField(self.maxZ, q=True, int=True)
        max_Z = cmds.intField(self.maxZ, q=True, int=True)
    
        for obj in range(len(cmds.ls(selection=True))):
            index = obj
        
            for obj in range(numDuplicates):
                tempObj = (cmds.duplicate(sel[index]), rr=True)
                randomX = random.uniform(min_X, max_X)
                randomY = random.uniform(min_Y, max_Y)
                randomZ = random.uniform(min_Z, max_Z)
            
                cmds.select(tempObj)
                cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ])  


RandomPlacement_Window = RandomPlacementUI()

RandomPlacement_Window.create()                                      