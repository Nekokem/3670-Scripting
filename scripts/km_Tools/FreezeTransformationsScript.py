import maya.cmds as cmds

def FreezeTrans():
    sel = cmds.ls(selection=True)
    FreezeTransformations
    preformFreezeTransformations(0)
    cmds.makeIdentity (apply=True, t=1, r=1, s=1, n=0, pn=1)