'''
Created on 2016. 10. 31.

@author: kyuho_choi
'''

import pymel.core as pm

class Control(object):
    def __init__(self):
        pass
    
class Base(object):
    def __init__(self):
        self.top_grp = pm.group(n='Group', em=True)
        self.rig_grp = pm.group(n='rig_grp', em=True, p=self.top_grp)
        self.dfm_grp = pm.group(n='dfm_grp', em=True, p=self.top_grp)
        self.geo_grp = pm.group(n='geo_grp', em=True, p=self.top_grp)
        
        assetName_atr = 'characterName'
        sceneObjectType_attr = 'asset'
        
        for at in [assetName_atr,sceneObjectType_attr]:
            pm.addAttr( self.top_grp, ln=at, dt='string')
            
        self.top_grp.assetName.set( assetName_atr )
        self.top_grp.sceneObjectType_attr.set( sceneObjectType_attr )