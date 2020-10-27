import maya.cmds as cmds


cmds.polyCylinder(sx=10, sy=5, sz=1, h=2)

cmds.move( 0, 5, 0, 'pCylinder1', absolute=True )

cmds.polyCylinder(r=.25, sx=10, sy=5, sz=1, h=10)

cmds.group( 'pCylinder1', 'pCylinder2', n='Marshmallow stick' )