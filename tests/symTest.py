'''
Created on 2016. 11. 11.

@author: kyuho_choi
'''
import pymel.core as pm
import raven.transform as tr

reload(tr)

pm.select ('joint4','joint5','joint2')
a = tr.SymmetryRig(axis='z')