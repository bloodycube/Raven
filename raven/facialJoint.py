# coding:utf-8
'''
Created on 2016. 10. 28.

@author: kyuho_choi

joint Labeling

눈 개수 여러개 가능하게.



'''

import pymel.core as pm
import utils as ut

class Template(object):

    def __init__(self, side='L'):
        '''초기회'''
        # TODO: 입력예외처리, 같은측 노드가 있다거나.. 등등.
        self.side = side
        self.meta = None

    def create(self):
        '''노드생성'''
        # node Create
        grp_eyeRig = pm.group(em=True, n='tmp_eyeRig__SIDE__grp')
        loc_eyePos = pm.group(em=True, n='tmp_eyePos__SIDE__loc')
        loc_irisPos = pm.spaceLocator(n='tmp_irisPos__SIDE__loc')
        loc_eyelidUp = pm.spaceLocator(n='tmp_eyelidUp__SIDE__loc')
        grp_lidGrp = pm.group(em=True, n='tmp_lid__SIDE__grp')
        loc_upperLidPos = pm.spaceLocator(n='tmp_upperLidPos__SIDE__loc')
        loc_lowerLidPos = pm.spaceLocator(n='tmp_lowerLidPos__SIDE__loc')

        # Hierachy
        pm.parent(loc_upperLidPos, loc_lowerLidPos, grp_lidGrp)
        pm.parent(grp_lidGrp, loc_eyePos)
        pm.parent(loc_eyePos, loc_irisPos,
                  loc_eyelidUp, grp_eyeRig)

        # default Position
        loc_irisPos.tz.set(5)
        loc_upperLidPos.ty.set(1)
        loc_lowerLidPos.ty.set(-1)
        loc_eyelidUp.ty.set(5)

        # constraint
        pm.pointConstraint(loc_irisPos, grp_lidGrp)
        pm.aimConstraint(loc_irisPos, loc_eyePos, aim=(
            0, 0, 1), u=(0, 1, 0), wut='object', wuo=loc_eyelidUp)

        # attr Lock
        loc_irisPos.r.lock()
        loc_irisPos.s.lock()
        loc_eyelidUp.r.lock()
        loc_eyelidUp.s.lock()
        loc_upperLidPos.tx.lock()
        loc_upperLidPos.r.lock()
        loc_upperLidPos.s.lock()
        loc_lowerLidPos.tx.lock()
        loc_lowerLidPos.r.lock()
        loc_lowerLidPos.s.lock()
        loc_irisPos.v.lock()
        loc_eyelidUp.v.lock()
        loc_upperLidPos.v.lock()
        loc_lowerLidPos.v.lock()

        # rename
        for node in [grp_eyeRig, loc_eyePos, loc_irisPos, loc_eyelidUp, grp_lidGrp, loc_upperLidPos, loc_lowerLidPos]:
            node.rename(node.name().replace('_SIDE_', self.side))
            node.rename(node.name().replace('__', '_'))

        ut.zeroGroup(
            [loc_irisPos, loc_eyelidUp, loc_upperLidPos, loc_lowerLidPos])

        # display : scale
        loc_irisPos.localScale.set(0, 0, 0)
        loc_eyelidUp.localScale.set(0, 0, 0)
        loc_upperLidPos.localScale.set(0, 0, 0)
        loc_lowerLidPos.localScale.set(0, 0, 0)
        grp_eyeRig.displayHandle.set(True)
        loc_irisPos.displayHandle.set(True)
        loc_eyelidUp.displayHandle.set(True)
        loc_upperLidPos.displayHandle.set(True)
        loc_lowerLidPos.displayHandle.set(True)

        # display : color
        grp_eyeRig.overrideEnabled.set(True)
        grp_eyeRig.overrideColor.set(28)  # darkBlue
        loc_irisPos.overrideEnabled.set(True)
        loc_irisPos.overrideColor.set(4)  # darkRed
        loc_eyelidUp.overrideEnabled.set(True)
        loc_eyelidUp.overrideColor.set(23)  # darkGreen

        # display : line
        ut.rigCurveConnect(loc_irisPos, loc_eyePos)
        ut.rigCurveConnect(loc_eyelidUp, loc_eyePos)

        # write meta data
        node_meta = grp_eyeRig  # pm.group(em=True, n='meta1')
        node_meta.addAttr('rigMetaType', dt='string')
        node_meta.addAttr('side', dt='string')
        node_meta.addAttr('rigGrp', at='message')
        node_meta.addAttr('eyePos', at='message')
        node_meta.addAttr('irisPos', at='message')
        node_meta.addAttr('eyelidUp', at='message')
        node_meta.addAttr('upperLidPos', at='message')
        node_meta.addAttr('lowerLidPos', at='message')
        pm.select(node_meta)

        node_meta.rigMetaType.set('eyeTemplate')
        node_meta.side.set(self.side)
        grp_eyeRig.message >> node_meta.rigGrp
        loc_eyePos.message >> node_meta.eyePos
        loc_irisPos.message >> node_meta.irisPos
        loc_eyelidUp.message >> node_meta.eyelidUp
        loc_upperLidPos.message >> node_meta.upperLidPos
        loc_lowerLidPos.message >> node_meta.lowerLidPos

        node_meta.rigMetaType.lock(True)
        node_meta.side.lock(True)

        # select
        pm.select(grp_eyeRig)
        
        self.meta = node_meta        
        self.rigGrp = grp_eyeRig
        self.eyePos = loc_eyePos
        self.irisPos = loc_irisPos
        self.eyelidUp = loc_eyelidUp
        self.upperLidPos = loc_upperLidPos
        self.lowerLidPos = loc_lowerLidPos

class Joint(object):

    def __init__(self, side='L'):
        '''초기화'''
        self.side = side

    def create(self):
        '''조인트 생성'''
        # create joints
        pm.select(cl=True)
        jnt_eyeBall = pm.joint()
        jnt_iris = pm.joint(p=(1, 0, 0))

        pm.select(cl=True)
        jnt_upperLid = pm.joint()
        jnt_upperLidEnd = pm.joint(p=(1, 0, 0))

        pm.select(cl=True)
        jnt_lowerLid = pm.joint()
        jnt_lowerLidEnd = pm.joint(p=(1, 0, 0))

        # jointOrient
        jnt_eyeBall.jointOrient.set(0, -90, 0)
        jnt_upperLid.jointOrient.set(0, -90, 0)
        jnt_lowerLid.jointOrient.set(0, -90, 0)

        # set Joint Label
        for jnt in [jnt_eyeBall, jnt_iris, jnt_upperLid, jnt_upperLidEnd, jnt_lowerLid, jnt_lowerLidEnd]:
            if self.side == 'L':
                jnt.side.set(1)  # Left
                jnt.typ.set(18)  # other

            if self.side == 'R':
                jnt.side.set(2)  # Right
                jnt.typ.set(18)  # other

        jnt_eyeBall.otherType.set('eyeBall')
        jnt_iris.otherType.set('iris')
        jnt_upperLid.otherType.set('upperLid')
        jnt_lowerLid.otherType.set('lowerLid')
        jnt_upperLidEnd.otherType.set('upperLidEnd')
        jnt_lowerLidEnd.otherType.set('lowerLidEnd')
        
        # return
        self.jnt_eyeBall = jnt_eyeBall
        self.jnt_iris = jnt_iris
        self.jnt_upperLid = jnt_upperLid        
        self.jnt_upperLidEnd = jnt_upperLidEnd
        self.jnt_lowerLid = jnt_lowerLid
        self.jnt_lowerLidEnd = jnt_lowerLidEnd

    def attachToTemplate(self, template=None):
        ''' 조인트 템플릿에 컨스트레인 '''
        
        # TODO: Template 인스턴스 형식 오류검사
        #template=Template()

        # get meta info
        grp_eyeRig = template.rigGrp
        loc_eyePos = template.eyePos
        loc_irisPos = template.irisPos
        loc_eyelidUp = template.eyelidUp
        loc_upperLidPos = template.upperLidPos
        loc_lowerLidPos = template.lowerLidPos
        self.side = template.side

        # create rig Append
        grp_jntConst = pm.group(em=True, n='tmp_jntConst_grp')
        pm.parent(grp_jntConst, grp_eyeRig, r=True)

        # constraint
        consts = []
        consts.append(pm.pointConstraint(loc_eyePos, self.jnt_eyeBall))
        consts.append(pm.pointConstraint(loc_eyePos, self.jnt_upperLid))
        consts.append(pm.pointConstraint(loc_eyePos, self.jnt_lowerLid))

        consts.append(pm.aimConstraint(loc_irisPos, self.jnt_eyeBall, aim=(1, 0, 0), u=(0, 1, 0), wut='objectRotation', wuo=grp_eyeRig))
        consts.append(pm.aimConstraint(loc_upperLidPos, self.jnt_upperLid, aim=(1, 0, 0), u=(0, 1, 0), wut='object', wuo=loc_eyelidUp))
        consts.append(pm.aimConstraint(loc_lowerLidPos, self.jnt_lowerLid, aim=(1, 0, 0), u=(0, 1, 0), wut='object', wuo=loc_eyelidUp))

        consts.append(pm.pointConstraint(loc_irisPos, self.jnt_iris))
        consts.append(pm.pointConstraint(loc_upperLidPos, self.jnt_upperLidEnd))
        consts.append(pm.pointConstraint(loc_lowerLidPos, self.jnt_lowerLidEnd))

        pm.parent(consts, grp_jntConst)

def humanTemplate():
    leftEye_tmp = Template('L')
    leftEye_tmp.create()
    leftEye_tmp.rigGrp.tx.set(5)
    
    leftEye_Jnt = Joint('L')
    leftEye_Jnt.create()
    leftEye_Jnt.attachToTemplate(leftEye_tmp)
    
    rightEye_tmp = Template('R')
    rightEye_tmp.create()
    
    rightEye_Jnt = Joint('R')
    rightEye_Jnt.create()
    rightEye_Jnt.attachToTemplate(rightEye_tmp)
    
    ut.rigSymTranslate( leftEye_tmp.rigGrp, rightEye_tmp.rigGrp )
    