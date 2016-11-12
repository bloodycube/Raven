'''
Created on 2016. 11. 11.

@author: kyuho_choi
'''
import sys
sys.path.append(r'D:\workspace_Git\Raven')
import pymel.core as pm
import raven.transform as tr

reload(tr)

# sample 1
jnt1 = pm.joint( p=(0,0,-3) )
jnt2 = pm.joint( p=(0,3,0) )
jnt3 = pm.joint( p=(0,10,0) )
jnt4 = pm.joint( p=(5,5,2) )
jnt5 = pm.joint( p=(5,5,5) )
jnt6 = pm.joint( p=(-5,5,2) )
jnt7 = pm.joint( p=(-5,5,5) )
pm.joint( jnt1, e=True, zso=True, oj="xyz", sao='yup')
pm.joint( jnt2, e=True, zso=True, oj="xyz", sao='yup')
pm.joint( jnt4, e=True, zso=True, oj="xyz", sao='yup')
pm.joint( jnt6, e=True, zso=True, oj="xyz", sao='yup')
pm.parent(jnt4, jnt6, jnt2)

pm.select(jnt4,jnt6,jnt2)
a = tr.SymmetryRig( axis='z', offset=(0,0,180) )
pm.select(jnt4)

#===============================================================================
# 
# sample 2
# 
#===============================================================================
reload(tr)

# 테스트용 노드 생성
loc1 = pm.spaceLocator()
loc2 = pm.spaceLocator()
loc3 = pm.spaceLocator()
loc1.t.set(5,5,5)

# Symm Rig 
sym = tr.SymmetryRig( loc1, loc2, loc3, axis='z', offset=(0,0,180) )
pm.select(loc1)

# orient Node 위치 변경
loc3.r.set(-45,0,0)
loc3.t.set(5,5,-5)

# orient 노드 변경
loc4 = pm.spaceLocator()
sym.setOrient(loc4)
pm.select(loc1)

# output 노드 변경
sphere = pm.polySphere()[0]
sym.setOutput(sphere)

# orient 노드 변경
loc5 = pm.spaceLocator()
sym.setInput(loc5)
pm.select(loc1)