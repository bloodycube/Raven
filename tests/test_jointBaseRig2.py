import pymel.core as pm

import sys
sys.path.append(r'D:\workspace_Git\Raven')

import raven.jointBaseRig2 as rig
import raven.rigLib.transform as tr
reload(rig)
reload(tr)

# 눈 인스턴스 생성
leftEye = rig.Eye('L')

# 눈 조인트 생성
leftEye.createJoint()

# 조인트 레이아웃 생성
leftEye.createLayout()