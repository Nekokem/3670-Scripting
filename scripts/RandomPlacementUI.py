import maya.cmds as cmds

class RandomPlacementUI():
    def __init__(self):
        self.RandomPlacement_Window = 'RandomPlacementWinderSetting'
            
    
    def create(self):
        self.delete()
        
        self.RandomPlacement_Window = cmds.window(title = 'RandomePlacement Window Settings', widthHeight=(500,500))
        self.colLayout = cmds.columnLayout(parent=self.RandomPlacement_Window, adjustableColumn=True )
        cmds.text(label="Number of Duplicates", parent = self.colLayout)
        self.numDups = cmds.intField(parent=self.colLayout)
        cmds.text(label="Minimun X", parent = self.colLayout)
        self.minX = cmds.intField(parent=self.colLayout)
        cmds.text(label="Maximun X", parent = self.colLayout)
        self.maxX = cmds.intField(parent=self.colLayout)
        cmds.text(label="Minimun Y", parent = self.colLayout)
        self.minY = cmds.intField(parent=self.colLayout)
        cmds.text(label="Maximun Y", parent = self.colLayout)
        self.maxY = cmds.intField(parent=self.colLayout)
        cmds.text(label="Minimun Z", parent = self.colLayout)
        self.minZ = cmds.intField(parent=self.colLayout)
        cmds.text(label="Maximun Z", parent = self.colLayout)
        self.maxZ = cmds.intField(parent=self.colLayout)
        cmds.button(parent=self.colLayout, label='Set', command=lambda *x: self.RandomPlacement())
        
        cmds.showWindow(self.RandomPlacement_Window)
    
    def delete(self):
        if cmds.window(self.RandomPlacement_Window, exists=True):
            cmds.deleteUI(self.RandomPlacement_Window)


    def RandomPlacement(self):
        
        sel = cmds.ls(selection=True)
        numberOfDups = cmds.intField(self.numDups, q=True, value=True)
        minX = cmds.intField(self.minX, q=True, value=True)
        maxX = cmds.intField(self.maxX, q=True, value=True)
        minY = cmds.intField(self.minY, q=True, value=True)
        maxY = cmds.intField(self.maxY, q=True, value=True)
        minZ = cmds.intField(self.maxZ, q=True, value=True)
        maxZ = cmds.intField(self.maxZ, q=True, value=True)

        for obj in range(len(cmds.ls(selection=True))):
            index = obj

            for obj in range(numberOfDups):
                tempObj = (cmds.duplicate(sel[index], rr=True))
                randomX = random.uniform(minX, maxX)
                randomY = random.uniform(minY, maxY)
                randomZ = random.uniform(minZ, maxZ)

                cmds.select(tempObj)
                cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ]) 


RandomPlacement_Window = RandomPlacementUI()

RandomPlacement_Window.create()                                      