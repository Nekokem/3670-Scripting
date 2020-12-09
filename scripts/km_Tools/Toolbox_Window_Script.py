import km_Tools
help(km_Tools)

ToolBoxWindow = 'ToolBoxWindowSettings'

Renamer = km_Tools.RenamerWindowScript.RenamerUI()

ToolBoxWindow = cmds.window(title = 'ToolBox Window Settings', widthHeight=(500,500))
colLayout = cmds.columnLayout(parent=ToolBoxWindow, adjustableColumn=True )
cmds.button(parent=self.colLayout, label='Renameer', command='Renamer.create()')

Random = km_Tools.RandomPlacementUI.RandomPlacementUI()

cmds.button(parent=self.colLayout, label='RandomPlacement', command='Random.create()')