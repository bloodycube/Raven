'''
Created on 2016. 10. 26.

@author: kyuho_choi
'''
import pymel.core as pm
import utils

def test():
    facs = utils.FACS()
    print facs.getAttrs(attrNum=False, attrGrp=False, attrName=True, splitAttrName=False, splitPart=False, auNum=False, auName=False)
    
    pm.polySphere()


