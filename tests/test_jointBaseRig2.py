import sys
sys.path.append(r'D:\workspace_Git\Raven')

import pymel.core as pm

import raven.jointBaseRig2 as jntRig
reload(jntRig)

jnt = jntRig.Joint()

jnt.getFilePath()
jnt.getJsonData()
jnt.isExists()

jnt.setJsonData("eye.json", key='joint')
jnt.getFilePath()
jnt.getJsonData()
jnt.isExists()

pm.newFile(f=True)
jnt.getPrefix()
jnt.importFile()
jnt.isExists()
jnt.printNode()

pm.newFile(f=True)
jnt.setPrefix("eye_L")
jnt.setPrefix("")
jnt.getPrefix()
jnt.isExists(True)
jnt.importFile()
jnt.isExists()
jnt.printNode()

jnt.openFile()
jnt.saveFile()


