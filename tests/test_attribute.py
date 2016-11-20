'''
Created on 2016. 11. 19.

@author: kyuho_choi
'''
# window
import sys
sys.path.append(r'D:\workspace_Git\Raven')
import pymel.core as pm
import raven.rigLib.attribute as ut
reload(ut)

# resverse Rig
# 역으로 세팅할 어트리뷰트를 채널박스에서 두개 선택 하고 실행
ut.reversAttrRig()

sel = pm.selected()
driver = sel[0]
print driver

sel = pm.selected()
driven = sel[0]