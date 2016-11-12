import pymel.core as pm

import sys
sys.path.append(r'D:\workspace_Git\Raven')

import raven.jointBaseRig as rig
import raven.transform as tr
reload(rig)

# 모듈 인스턴스 생성
head = rig.Head()

# 조인트 생성
head.createJoint()

# 레이아웃 생성
head.createLayout()

# 레이아웃 삭제
pm.delete( head.layout.parent )

# 레이아웃 재 생성
head.createLayout()

# 위치 조정
head.layout.root.t.set(0,0,0)
head.layout.root.r.set(0,0,0)

# 눈 인스턴스 생성
leftEye = rig.Eye('L')

# 눈 조인트 생성
leftEye.createJoint()

# 조인트 레이아웃 생성
leftEye.createLayout()

# 레이아웃 위치 조정
leftEye.layout.root.t.set(5,-5,-5)
leftEye.layout.root.r.set(0,0,-90)
leftEye.layout.root.s.set(.5,.5,.5)

# 눈 레이아웃 삭제
leftEye.deleteLayout()

# 눈 레이아웃 재생성
leftEye.createLayout()

# 스냅툴
# rig.snap()

# 눈 인스턴스 생성
rightEye = rig.Eye('R')
 
# 눈 조인트 생성
rightEye.createJoint()
 
# 조인트 레이아웃 생성
rightEye.createLayout()
 
# Symetry Rig
#sym = rig.SymmetryRig( leftEye.layout.root,   rightEye.layout.root,   axis='z' )
#sym = rig.SymmetryRig( leftEye.layout.eye_up, rightEye.layout.eye_up, axis='z' )

tr.SymmetryRig( leftEye.layout.root, rightEye.layout.root, "head_jnt",  axis='z' )


jaw = rig.Jaw()
jaw.createJoint()
jaw.createLayout()

