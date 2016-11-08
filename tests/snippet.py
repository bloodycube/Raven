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

