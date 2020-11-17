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