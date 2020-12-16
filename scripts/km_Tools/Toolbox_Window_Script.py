import maya.cmds as cmds

class ToolBoxUI():
    def __init__(self):
        self.ToolBoxWindow = 'ToolBoxWindowSettings'

    def create(self):
        
        self.ToolBoxWindow = cmds.window(title = 'ToolBox Window Settings', widthHeight=(500,500))
        self.colLayout = cmds.columnLayout(parent=self.ToolBoxWindow, adjustableColumn=True )
        cmds.button(parent=self.colLayout, label='Renamer', command=lambda *x: self.RenamerButton())
        cmds.button(parent=self.colLayout, label='Randomize', command=lambda *x: self.RandomButton())
        cmds.button(parent=self.colLayout, label='Freeze Transforms', command=lambda *x: self.FreezeButton())
        cmds.button(parent=self.colLayout, label='Delete History', command=lambda *x: self.HistoryDeleteButton())
        cmds.button(parent=self.colLayout, label='Group', command=lambda *x: self.ParentGrpButton())
        cmds.button(parent=self.colLayout, label='Constrain', command=lambda *x: self.ConstrainButton())
        cmds.button(parent=self.colLayout, label='Toggle', command=lambda *x: self.ToggleButton())


        cmds.showWindow(self.ToolBoxWindow)
        
        
    def delete(self):
        if cmds.window(self.ToolBoxWindow, exists=True):
            cmds.deleteUI(self.ToolBoxWindow)
            
    def RenamerButton(self):
        import RenamerWindowScript
        reload(RenamerWindowScript)
        Renamer = RenamerWindowScript.RenamerUI()
        Renamer.create()
        
    def RandomButton(self):
        import RandomPlacementUI
        reload(RandomPlacementUI)
        Random = RandomPlacementUI.RandomPlaceUI()
        Random.create()
        
    def FreezeButton(self):
        import FreezeTransformationsScript
        reload(FreezeTransformationsScript)
        Freeze = FreezeTransformationsScript.FreezeTransUI()
        Freeze.FreezeTrans()
        
    def HistoryDeleteButton(self):
        import HistoryDelete
        reload(HistoryDelete)
        History = HistoryDelete.HistoryDeleteUI()
        History.HistoryDelete()
        
    def ParentGrpButton(self):
        import ParentGrpScript
        reload(ParentGrpScript)
        Grp = ParentGrpScript.ParentGroupUI()
        Grp.ParentGroupFunc()
        
    def ConstrainButton(self):
        import ConstrainScript
        reload(ConstrainScript)
        Constrain = ConstrainScript.ConstrainUI()
        Constrain.ConstrainFunc()
        
    def ToggleButton(self):
        import ToggleAxesScript
        reload(ToggleAxesScript)
        Toggle = ToggleAxesScript.ToggleAxes()
        Toggle.Toggle()
            

ToolBoxWindow = ToolBoxUI()

ToolBoxWindow.create()                                      