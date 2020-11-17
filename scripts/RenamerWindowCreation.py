import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
    for sels in sel:
        collectionCount = stringName.count('#')
        selParts = stringName.partition('#' + collectionCount)
        numSystem = str(sel)
        
        if selParts[1]:
            print 'Numbers are sequential!'
            zeroFiller = numSystem.zfill(3)
            cmds.rename(tuple[0] + zeroFiller + tuple[2])
        else:
            print 'Not sequqntial! Figure out why!'

    selectionNum += 1

Renamer('L_Arm_###_Jnt')
# Error: TypeError: file <maya console> line 9: cannot concatenate 'str' and 'int' objects # 
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
    for sels in sel:
        collectionCount = stringName.count('#')
        selParts = stringName.partition('#' * collectionCount)
        numSystem = str(sel)
        
        if selParts[1]:
            print 'Numbers are sequential!'
            zeroFiller = numSystem.zfill(3)
            cmds.rename(tuple[0] + zeroFiller + tuple[2])
        else:
            print 'Not sequqntial! Figure out why!'

    selectionNum += 1

Renamer('L_Arm_###_Jnt')
Numbers are sequential!
# Error: TypeError: file <maya console> line 15: 'type' object has no attribute '__getitem__' # 
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
    for sels in sel:
        collectionCount = stringName.count('#')
        selParts = stringName.partition('#' * collectionCount)
        numSystem = str(sel)
        
        if selParts[1]:
            print 'Numbers are sequential!'
            zeroFiller = numSystem.zfill(3)
            cmds.rename(selParts[0] + zeroFiller + selParts[2])
        else:
            print 'Not sequqntial! Figure out why!'

    selectionNum += 1

Renamer('L_Arm_###_Jnt')
Numbers are sequential!
# Error: RuntimeError: file <maya console> line 15: Cannot rename a read only node. # 
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer('L_Arm_###_Jnt')
Numbers are sequential!
# Error: RuntimeError: file <maya console> line 15: Cannot rename a read only node. # 
select -r -ne defaultObjectSet ;
// Error: <function selCom at 0x7f29c5c04aa0>; // 
// Error: Line 1.1: Syntax error // 
select -cl  ;
select -r pSphere1 ;
// Error: <function selCom at 0x7f29c5c04aa0>; // 
// Error: Line 1.1: Syntax error // 
select -add pSphere2 ;
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer('L_Arm_###_Jnt')
Numbers are sequential!
Numbers are sequential!
select -cl  ;
select -r L_Arm_001_Jnt ;
doDelete;
select -r L_Arm_001_Jnt1 ;
// Error: <function selCom at 0x7f29c5c04aa0>; // 
// Error: Line 1.1: Syntax error // 
CreatePolygonSphere;
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere1 polySphere1 // 
CreatePolygonCylinder;
polyCylinder -r 1 -h 2 -sx 20 -sy 1 -sz 1 -ax 0 1 0 -rcp 0 -cuv 3 -ch 1;
// Result: pCylinder1 polyCylinder1 // 
move -r -os -wd 0 0 3.519198 ;
select -r pSphere1 ;
// Error: <function selCom at 0x7f29c5c04aa0>; // 
// Error: Line 1.1: Syntax error // 
select -add pCylinder1 ;
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer('L_Arm_###_Jnt')
Numbers are sequential!
Numbers are sequential!
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer('L_Arm_###_Jnt')
Numbers are sequential!
Numbers are sequential!
import maya.cmds as cmds

Renamer_Window = cmds.window()
print Renamer_Window

window1
import maya.cmds as cmds

Renamer_Window = cmds.window(title = 'Renamer Window Settings')


cmds.showWindow(Renamer_Window)
import maya.cmds as cmds

Renamer_Window = cmds.window(title = 'Renamer Window Settings')

cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: RuntimeError: file <maya console> line 5: Controls must have a layout.  No layout found in window : # 
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer_Window = cmds.window(title = 'Renamer Window Settings')

cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: RuntimeError: file <maya console> line 23: Controls must have a layout.  No layout found in window : # 
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer_Window = cmds.window(title = 'Renamer Window Settings')

cmds.columnLayout( adjustableColumn=True )
cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: AttributeError: file <maya console> line 8: 'bool' object has no attribute 'count' # 
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer_Window = cmds.window(title = 'Renamer Window Settings',width=(200))

cmds.columnLayout( adjustableColumn=True )
cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer_Window = cmds.window(title = 'Renamer Window Settings',width=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: TypeError: file <maya console> line 21: Invalid arguments for flag 'width'.  Expected int, got ( int, int ) # 
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmdLine = cmds.commandLine()
cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmdLine = cmds.commandLine()
cmds.commandLine( cmdLine, edit=True, height=25)
cmds.commandLine( cmdLine, edit=True, sourceType="python")
cmds.formLayout( form, edit=True, attachForm=[(cmdLine, 'top', 0), (cmdLine, 'left', 0), (cmdLine, 'right', 0), (field, 'left', 0), (field, 'bottom', 0), (field, 'right', 0)], attachNone=(cmdLine, 'bottom'), attachControl=(field, 'top', 5, cmdLine) )

cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: NameError: file <maya console> line 7: name 'form' is not defined # 
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmdLine = cmds.commandLine()
cmds.commandLine( cmdLine, edit=True, height=25)
cmds.commandLine( cmdLine, edit=True, sourceType="python")

cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: AttributeError: file <maya console> line 8: 'bool' object has no attribute 'count' # 
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmdLine = cmds.commandLine()
cmds.commandLine( cmdLine, edit=True, height=25)

cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmdLine = cmds.commandLine()
cmds.commandLine( cmdLine, edit=True, height=25)
cmds.commandLine(Input, annotation=string)

cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: NameError: file <maya console> line 6: name 'Input' is not defined # 
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))
Input = cmds.formLayout()
cmds.columnLayout( adjustableColumn=True )
cmdLine = cmds.commandLine()
cmds.commandLine( cmdLine, edit=True, height=25)
cmds.commandLine(Input, annotation=string)

cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: NameError: file <maya console> line 6: name 'string' is not defined # 
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))
Input = cmds.formLayout()
cmds.columnLayout( adjustableColumn=True )
cmdLine = cmds.commandLine()
cmds.commandLine( cmdLine, edit=True, height=25)
cmds.commandLine(Input, annotation=True)

cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))
Input = cmds.formLayout()
cmds.columnLayout( adjustableColumn=True )
cmdLine = cmds.commandLine()
cmds.commandLine( cmdLine, edit=True, height=25)
cmds.commandLine(Input, inputAnnotation=True)

cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: AttributeError: file <maya console> line 8: 'bool' object has no attribute 'count' # 
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmds.text( label='Name' )
name = cmds.textField()
cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: AttributeError: file <maya console> line 8: 'bool' object has no attribute 'count' # 
# Error: AttributeError: file <maya console> line 8: 'bool' object has no attribute 'count' # 
import maya.cmds as cmds

def Renamer(stringName):
    sel = cmds.ls(selection = True)
    selectionNum = 1
    
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

Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmds.text( label='Name' )
name = cmds.textField()
cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmds.text( label='New Name' )
name = cmds.textField()
cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
Renamer_Window = cmds.window(title = 'Renamer Window Settings',widthHeight=(500,500))

cmds.columnLayout( adjustableColumn=True )
cmds.text( label='New Name' )
name = cmds.textField()
cmds.button(label='Rename', command=Renamer)

cmds.showWindow(Renamer_Window)
# Error: AttributeError: file <maya console> line 8: 'bool' object has no attribute 'count' # 
