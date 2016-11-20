import pymel.core as pm

import sys
sys.path.append(r'D:\workspace_Git\Raven')

import raven.jointBaseRig as rig
import raven.rigLib.transform as tr
reload(rig)
reload(tr)

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

# 눈 인스턴스 생성
rightEye = rig.Eye('R')
 
# 눈 조인트 생성
rightEye.createJoint()
 
# 조인트 레이아웃 생성
rightEye.createLayout()
 
# Symmetry Rig
symList = [
    {'input':leftEye.layout.root,         'output':rightEye.layout.root,         'orient':"head_jnt", 'axis':'z'},
    {'input':leftEye.layout.eye_up,       'output':rightEye.layout.eye_up,       'orient':"head_jnt", 'axis':'z'},
    {'input':leftEye.layout.eye_aim,      'output':rightEye.layout.eye_aim,      'orient':"head_jnt", 'axis':'z'},
    {'input':leftEye.layout.upperLid_aim, 'output':rightEye.layout.upperLid_aim, 'orient':"head_jnt", 'axis':'z'},
    {'input':leftEye.layout.lowerLid_aim, 'output':rightEye.layout.lowerLid_aim, 'orient':"head_jnt", 'axis':'z'},
    {'input':leftEye.layout.iris_pos,     'output':rightEye.layout.iris_pos,     'orient':"head_jnt", 'axis':'z'},
    {'input':leftEye.layout.upperLid_pos, 'output':rightEye.layout.upperLid_pos, 'orient':"head_jnt", 'axis':'z'},
    {'input':leftEye.layout.lowerLid_pos, 'output':rightEye.layout.lowerLid_pos, 'orient':"head_jnt", 'axis':'z'},
    ]
for item in symList:
    tr.SymmetryRig( item['input'], item['output'], item['orient'], axis='z' )

# 턱 인스턴스 생성
jaw = rig.Jaw()

# 턱 조인트 생성
jaw.createJoint()

# 턱 조인트 리그 생
jaw.createLayout()


########################
reload(rig)
reload(tr)

# 눈 인스턴스 생성
leftEye = rig.Eye('L')

# 눈 조인트 생성
leftEye.createJoint()

# 레이아웃 생성
leftEye.createLayout()

# 조인트 레이아웃 생성
leftEye.createRig()

print len(pm.ls())
