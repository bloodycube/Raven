# coding:utf-8
'''
Created on 2016. 10. 28.

@author: kyuho_choi

joint Labeling

눈 개수 여러개 가능하게.


import sys
sys.path.append(r'D:\workspace_Git\Raven')

import raven
reload(raven)
eyeL = raven.facialJoint.Eye( side='L' )
eyeL.createJoint()
eyeL.rigTemplate()
'''

import pymel.core as pm

def snap(target, obj, constType):
    # 롹 걸린 어트리뷰트 파악하고
    lockedAttrs = obj.listAttr( locked=True )
    
    # 롹을 잠깐 풀고
    for attr in lockedAttrs:
        attr.unlock()
        print attr
        
    # 위치 맞춘다음
    if constType=='parent':
        pm.delete( pm.parentConstraint( target, obj) )
    elif constType=='point':
        pm.delete( pm.pointConstraint( target, obj) )
    
    # 다시 롹
    for attr in lockedAttrs:
        attr.lock()
    

class Struct(object):
    ''' 리그 자료형 '''
    def getList(self):
        result = []
        lst = self.__dict__.values()
        for item in lst:
            if pm.objExists(item.name()):
                result.append( item )
        return result

class Eye(object):
    '''
    눈 조인트 생성
    기본위치
    
    :example:
    >> import sys
    >> sys.path.append(r'D:\workspace_Git\Raven')
    >> import raven
    >> reload(raven)
    >> leftEye = raven.facialJoint.Eye( side='L' )
    
    '''
    def __init__(self, side='L'):
        self.side = side
        self.joint = Struct()
        self.template = Struct()
       
    def __importJoint(self):
        ''' ma파일에서 조인트 얻어옴
        
        :memo: 
            D:\workspace_Git\Raven\raven\files\eye_joint.ma
            __file__/files/eye.ma
        '''
        # ma파일 오픈
        tmp = __file__.replace('\\','/')
        split = tmp.split('/')        
        filePath = '/'.join(split[:-1]) + '/files/eye_joint.ma'
        nodes = pm.importFile(filePath, returnNewNodes=True)  # @UnusedVariable
        
        # 필요 조인트들 등록
        self.joint.eye          = pm.PyNode('TMP__eye__SIDE__jnt')
        self.joint.eyeBall      = pm.PyNode('TMP__eyeBall__SIDE__jnt')
        self.joint.eyeEnd       = pm.PyNode('TMP__eyeBallEnd__SIDE__jnt')
        self.joint.upperLid     = pm.PyNode('TMP__upperLid__SIDE__jnt')
        self.joint.upperLidEnd  = pm.PyNode('TMP__upperLidEnd__SIDE__jnt')
        self.joint.lowerLid     = pm.PyNode('TMP__lowerLid__SIDE__jnt')
        self.joint.lowerLidEnd  = pm.PyNode('TMP__lowerLidEnd__SIDE__jnt')
          
    def __importTemplate(self):
        ''' ma파일에서 템플릿 얻어옴
        
        :memo: 
            D:\workspace_Git\Raven\raven\files\eye_template.ma
            __file__/files/eye.ma
        '''
        
        # prefix정의 
        prefix = 'tmpEye_%s_' % self.side
        
        # ma파일 오픈
        tmp = __file__.replace('\\','/')
        split = tmp.split('/')        
        filePath = '/'.join(split[:-1]) + '/files/eye_template.ma'
        nodes = pm.importFile( filePath, returnNewNodes=True, renameAll=True, renamingPrefix=prefix )  # @UnusedVariable
        
        # 필요 조인트들 등록 
        if prefix:
            prefix+='_'
            
        self.template.root_hdl     = pm.PyNode( prefix+'root_hdl')
        #self.template.eye_rot
        self.template.front        = pm.PyNode( prefix+'front_hdl')
        self.template.up           = pm.PyNode( prefix+'up_hdl')        
        self.template.iris         = pm.PyNode( prefix+'iris_hdl')
        self.template.upperLid     = pm.PyNode( prefix+'upperLid_hdl')
        self.template.lowerLid     = pm.PyNode( prefix+'lowerLid_hdl')
        self.template.upperLid_zro = pm.PyNode( prefix+'upperLid_zro')
        self.template.lowerLid_zro = pm.PyNode( prefix+'lowerLid_zro')      
        self.template.upperLid_rot = pm.PyNode( prefix+'upperLid_rot')
        self.template.lowerLid_rot = pm.PyNode( prefix+'lowerLid_rot')
        self.template.const_grp    = pm.PyNode( prefix+'const_grp')        
    
    def createJoint(self):
        ''' 조인트 생성 '''
        
        self.__importJoint()
        jnts = self.joint.getList()
        
        # 신규이름 생성
        # 원본 파일은 TMP__<jointName>__SIDE__jnt 형식으로 네이밍 되어 있음
        newNames = []
        for jnt in jnts:       
            newName = jnt.name().replace('__SIDE__','_%s_'%self.side)
            newName = newName.replace('TMP__','')        
            newNames.append( newName )
            #print newName
        
        # 씬에 같은 이름의 조인트가 있는지 체크
        condition = False
        for name in newNames:
            if pm.objExists(name):
                condition = True
                
        # 같은이름의 노드가 존재하면 에러 출력하고 중지.
        if condition:
            pm.select(jnts)
            pm.delete(jnts)
            raise NameError(u"같은이름의 노드가 이미 존재합니다.")
        
        # 이름변경, 라벨변경, 
        for name, jnt in zip(newNames,jnts):
            jnt.rename(name)
            
            if self.side == 'L':
                jnt.side.set(1)
            elif self.side == 'R':
                jnt.side.set(2)
            elif self.side == 'C':
                jnt.side.set(0)
            else:
                jnt.side.set(3)
                
            jnt.drawLabel.set(True)   
        
    def rigTemplate(self):
        # 조인트가 준비되지 않았으면 에러 출력. 중지.
        if not self.joint.getList():
            raise AttributeError(u"조인트가 준비되지 않았습니다.")
        
        #
        # 템플릿 파일 임포트
        #
        self.__importTemplate()        

        #
        # 템플릿 위치 조인트에 맞춤 
        #
        self.joint.upperLid.r.set(0,0,0)
        self.joint.lowerLid.r.set(0,0,0)
        
        snap( self.joint.eye, self.template.root_hdl, 'parent')
        snap( self.joint.upperLidEnd, self.template.upperLid_zro, 'parent' )
        snap( self.joint.lowerLidEnd, self.template.lowerLid_zro, 'parent' )
        
        # 템플릿을 살짝 띄움.
        self.template.upperLid.tx.set(1)
        self.template.lowerLid.tx.set(1)
        
        #
        # 조인트를 템플릿에 구속
        #
        
        # 루트
        consts = []
        consts.append( pm.pointConstraint( self.template.root_hdl, self.joint.eye ) )
        consts.append( pm.aimConstraint( self.template.front, self.joint.eye, aim=(1,0,0), u=(0,1,0), wu=(0,1,0), wut='object', wuo=self.template.up ) )
        
        # 윗,아랫 눈꺼풀
        self.template.upperLid_rot.rz >> self.joint.upperLid.joz
        self.template.lowerLid_rot.rz >> self.joint.lowerLid.joz
        
        # 눈알
        consts.append( pm.pointConstraint( self.template.iris, self.joint.eyeEnd ) )
        
        # 컨스트레인 노드 정리
        pm.parent( consts, self.template.const_grp )


class Jaw(object):
    def __init__(self):
        pass
        
    def createJoint(self):
        pm.select(cl=True)
        self.jaw = pm.joint()
        pm.select(cl=True)


def main():
    centerEye = Eye( side='C' )
    #leftEye = Eye( side='L' )
    #rightEye = Eye( side='R' )
    
    centerEye.createJoint()
    #leftEye.createJoint()
    #rightEye.createJoint()
    
    #print leftEye.joints
    
    

    