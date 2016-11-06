'''
Created on 2016. 11. 4.

@author: kyuho_choi
'''
import pymel.core as pm

sel = pm.selected()
node = sel[0]
for node in sel:
    pm.setAttr( node.useOutlinerColor, True )
    pm.setAttr( node.outlinerColor, 1,1,0 )

pm.mel.AEdagNodeCommonRefreshOutliners()  # @UndefinedVariable


sel = pm.selected()
node = sel[0]
for node in sel:
    pm.setAttr( node.useOutlinerColor, True )
    pm.setAttr( node.outlinerColor, 1,0,0 )
    
sel = pm.selected()
node = sel[0]
for node in sel:
    col = .5
    pm.setAttr( node.useOutlinerColor, True )    
    pm.setAttr( node.outlinerColor, col,col,col )


import
def saveData(fileName):
    data = {}
    for sysGrp in sysGrpList:
        sysGrp = pm.PyNode(sysGrp)
        attrList = sysGrp.listAttr(ud=True)
        for attr in attrList:
            data[attr.name()] = attr.get()
    
    fileHandle = open(fileName, 'w')
    json.dump(data, fileHandle, indent=4)
    fileHandle.close()
    
def loadData(fileName):
    data = {}
    if os.path.exists(fileName):
        fileHandle = open(fileName, 'r')
        data = json.loads(fileHandle.read())
        fileHandle.close()
    
    for attr, value in data.iteritems():
        try:
            pm.setAttr(attr, value)
        except:
            print attr