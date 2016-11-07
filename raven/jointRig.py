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
    
    # PyNode 리캐스팅
    target = pm.PyNode(target)
    obj = pm.PyNode(obj)
    
    # 롹 걸린 어트리뷰트 파악
    lockedAttrs = obj.listAttr( locked=True )
    
    # 롹을 잠깐 풀고
    for attr in lockedAttrs:
        attr.unlock()
        
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


class RigModule(object):
    def __init__(self):
        self._jointFile    = None
        self._templateFile = None
        self._templatePrefix = ''
        self._jointNode_checkList = []
        self._templateNode_checkList = []
        
        self.side = None        
        
        self.joint    = Struct()
        self.template = Struct()
        self.rig      = Struct()
    


    def __importJoint(self):
        ''' ma파일에서 조인트 임포트 
        
        :note:
            ma파일 조정시 export selection으로 파일 업데이트 할것.
        '''

        # ma파일 오픈
        tmp = __file__.replace('\\','/')
        split = tmp.split('/')        
        filePath = '/'.join(split[:-1]) + '/files/' + self._jointFile
        
        # 임포트
        # nodes = pm.importFile( filePath, returnNewNodes=True, renameAll=True, renamingPrefix=self.jointPefix )  # @UnusedVariable     
        pm.importFile( filePath )  # @UnusedVariable

    def isJointExists(self):
        ''' 필요 조인트가 존재하는지 체크 '''
        
        # 필요한 목록이 정의되어 있지 않으면 에러
        if not self._jointNode_checkList:
            raise AttributeError(u"필요한 조인트가 정의 되어 있지 않습니다.")
        
        # 조인트가 존재하는지 확인
        cond = False
        for jnt in self._jointNode_checkList:
            if pm.objExists(jnt):
                cond = True
        
        # 결과 리턴      
        return cond
    
    def registJoint(self):
        ''' 조인트 등록 '''
        # 이미 조인트가 존재하면 에러, 중지.
        if not self.isJointExists():
            raise AttributeError(u"필요한 조인트가 존재하지 않습니다.")
        
    def createJoint(self):
        ''' 조인트 생성 '''
        # 이미 조인트가 존재하면 에러, 중지.
        if self.isJointExists():
            raise AttributeError(u"조인트가 이미 존재합니다.")
        
        # 조인트를 파일에서 임포트
        self.__importJoint()
        
        # 임포트된 조인트 등록
        self.registJoint()
    
    
  
    def __importTemplate(self):
        ''' ma파일에서 조인트 임포트 
        
        :note:
            ma파일 조정시 export selection으로 파일 업데이트 할것.
        '''

        # ma파일 오픈
        tmp   = __file__.replace('\\','/')
        split = tmp.split('/')        
        filePath = '/'.join(split[:-1]) + '/files/' + self._templateFile
        
        # 임포트
        nodes = pm.importFile( filePath, returnNewNodes=True, renameAll=True, renamingPrefix=self._templatePrefix )  # @UnusedVariable  
         
    def isTemplateExists(self):
        ''' 필요 템플릿 노드가 존재하는지 체크 '''
        
        # 필요한 목록이 정의되어 있지 않으면 에러
        if not self._templateNode_checkList:
            raise AttributeError(u"필요한 템플릿 노드가 정의 되어 있지 않습니다.")
        
        # 조인트가 존재하는지 확인
        cond = False
        for node in self._templateNode_checkList:
            
            prefix = self._templatePrefix +'_'
            
            if pm.objExists(prefix + node):
                cond = True
        
        # 결과 리턴      
        return cond
    
    def registTemplate(self):
        ''' 템플릿 등록 '''
        if not self.isTemplateExists():
            raise AttributeError(u"필요한 템플릿 노드가 존재하지 않습니다.")
        
        prefix = self._templatePrefix +'_'
        
        self.template.root = pm.PyNode( prefix + 'root')
        self.template.const_grp = pm.PyNode( prefix + 'const_grp')         
        
    def createTemplate(self):
        # 필요한 조인트가 존재하지 않으면 에러.
        if not self.isJointExists():
            raise AttributeError(u"필요한 조인트가 존재하지 않습니다.")
        
        # 템플릿을 파일에서 임포트
        self.__importTemplate()
        
        # 템플릿 등록
        self.registTemplate()
                

class Eye(object):
    '''
    눈 조인트 생성
    기본위치
    
    :example:
        import sys
        sys.path.append(r'D:\workspace_Git\Raven')
        
        import raven
        reload(raven)
        eyeL = raven.jointRig.Eye( side='L' )
        eyeL.createJoint()
        eyeL.rigTemplate()
    
    '''
    def __init__(self, side='L'):
        self.side     = side
        self.joint    = Struct()
        self.template = Struct()
        self.rig      = Struct()
  
    def __importJoint(self):
        ''' ma파일에서 조인트 임포트 
        
        :note:
            ma파일 조정시 export selection으로 파일 업데이트 할것.
        '''

        # prefix정의 
        prefix = 'tmpJoint_' 

        # ma파일 오픈
        tmp = __file__.replace('\\','/')
        split = tmp.split('/')        
        filePath = '/'.join(split[:-1]) + '/files/eye_joint.ma'
        nodes = pm.importFile( filePath, returnNewNodes=True, renameAll=True, renamingPrefix=prefix )  # @UnusedVariable
        
        # 프리픽스 조정 : 임포트시 자동으로 '_'캐릭터가 붙음
        if prefix:
            prefix+='_'
        self.__jointPefix = prefix
            
        # 필요 노드 등록
        self.joint.eye          = pm.PyNode( prefix+'eye__SIDE__jnt' )
        self.joint.eyeBall      = pm.PyNode( prefix+'eyeBall__SIDE__jnt' )
        self.joint.iris         = pm.PyNode( prefix+'iris__SIDE__jnt' )
        self.joint.upperLid     = pm.PyNode( prefix+'upperLid__SIDE__jnt' )
        self.joint.upperLidEnd  = pm.PyNode( prefix+'upperLidEnd__SIDE__jnt' )
        self.joint.lowerLid     = pm.PyNode( prefix+'lowerLid__SIDE__jnt' )
        self.joint.lowerLidEnd  = pm.PyNode( prefix+'lowerLidEnd__SIDE__jnt' )
      
    def __importTemplate(self):
        ''' ma파일에서 템플릿 임포트 
        
        :note:
            ma파일 조정시 export selection으로 파일 업데이트 할것.
        '''
        
        # prefix정의 
        prefix = 'eye_%s_temp_' % self.side
        
        # ma파일 오픈
        tmp = __file__.replace('\\','/')
        split = tmp.split('/')        
        filePath = '/'.join(split[:-1]) + '/files/eye_template.ma'
        nodes = pm.importFile( filePath, returnNewNodes=True, renameAll=True, renamingPrefix=prefix )  # @UnusedVariable
        
        # 프리픽스 조정 : 임포트시 자동으로 '_'캐릭터가 붙음
        if prefix:
            prefix+='_'
            
        # 필요 노드 등록
        self.template.root             = pm.PyNode( prefix+'root')
        self.template.eye_pos          = pm.PyNode( prefix+'eye_pos')
        self.template.eye_aim          = pm.PyNode( prefix+'eye_aim')
        self.template.eye_up           = pm.PyNode( prefix+'eye_up')
        self.template.eye_rot          = pm.PyNode( prefix+'eye_rot')     
        self.template.iris_pos         = pm.PyNode( prefix+'iris_pos')
        self.template.upperLid_aim     = pm.PyNode( prefix+'upperLid_aim')
        self.template.lowerLid_aim     = pm.PyNode( prefix+'lowerLid_aim')
        self.template.upperLid_pos     = pm.PyNode( prefix+'upperLid_pos')
        self.template.lowerLid_pos     = pm.PyNode( prefix+'lowerLid_pos')
        
        self.template.eye_aim_zro      = pm.PyNode( prefix+'eye_aim_zro')
        self.template.iris_pos_zro     = pm.PyNode( prefix+'iris_pos_zro')
        self.template.upperLid_aim_zro = pm.PyNode( prefix+'upperLid_aim_zro')
        self.template.lowerLid_aim_zro = pm.PyNode( prefix+'lowerLid_aim_zro')
        self.template.upperLid_pos_zro = pm.PyNode( prefix+'upperLid_pos_zro')
        self.template.lowerLid_pos_zro = pm.PyNode( prefix+'lowerLid_pos_zro')    
        self.template.upperLid_rot     = pm.PyNode( prefix+'upperLid_rot')
        self.template.lowerLid_rot     = pm.PyNode( prefix+'lowerLid_rot')
        self.template.const_grp        = pm.PyNode( prefix+'const_grp')        

    def createJoint(self):
        ''' 조인트 생성 '''
        
        self.__importJoint()
        jnts = self.joint.getList()
        
        # 신규이름 생성
        # 원본 파일은 TMP__<jointName>__SIDE__jnt 형식으로 네이밍 되어 있음
        newNames = []
        for jnt in jnts:       
            newName = jnt.name().replace('__SIDE__','_%s_'%self.side)
            newName = newName.replace( self.__jointPefix,'')        
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
                
            if jnt.otherType.get() in ['eye','iris','upperLidEnd','lowerLidEnd']:
                jnt.drawLabel.set(True)   

    def rigTemplate(self):
        ''' 조인트에 템플릿 구속 '''
        
        # 조인트가 준비되지 않았으면 에러 출력. 중지.
        if not self.joint.getList():
            raise AttributeError(u"조인트가 준비되지 않았습니다.")
        
        # ----------------------------------
        #
        # 템플릿 파일 임포트
        #
        # ----------------------------------
        self.__importTemplate()        

        # ----------------------------------
        #
        # 조인트에 템플릿 위치시킴
        #
        # ----------------------------------
        self.joint.upperLid.r.set(0,0,0)
        self.joint.lowerLid.r.set(0,0,0)
        
        snap( self.joint.eye,         self.template.root,             'parent' )
        snap( self.joint.iris,        self.template.eye_aim_zro,      'parent' )
        snap( self.joint.iris,        self.template.iris_pos_zro,     'parent' )
        snap( self.joint.upperLidEnd, self.template.upperLid_aim_zro, 'parent' )
        snap( self.joint.lowerLidEnd, self.template.lowerLid_aim_zro, 'parent' )
        snap( self.joint.upperLidEnd, self.template.upperLid_pos_zro, 'parent' )
        snap( self.joint.lowerLidEnd, self.template.lowerLid_pos_zro, 'parent' )
        
        # 템플릿을 살짝 띄움.
        self.template.upperLid_aim.tx.set(1)
        self.template.lowerLid_aim.tx.set(1)
        self.template.eye_aim.tx.set(2)
        
        # ----------------------------------
        #
        # 템플릿에 조인트 컨스트레인
        #
        # ----------------------------------
        
        # 로테이션 우선 처리 > 포지션 처리
        consts = []
        self.template.upperLid_rot.rz >> self.joint.upperLid.joz
        self.template.lowerLid_rot.rz >> self.joint.lowerLid.joz                
        consts.append( pm.orientConstraint( self.template.eye_rot,     self.joint.eye ) )
        consts.append( pm.pointConstraint( self.template.eye_pos,      self.joint.eye ) )        
        consts.append( pm.pointConstraint( self.template.upperLid_pos, self.joint.upperLidEnd ) )
        consts.append( pm.pointConstraint( self.template.lowerLid_pos, self.joint.lowerLidEnd ) )
        consts.append( pm.pointConstraint( self.template.iris_pos,     self.joint.iris ) )
        
        # 컨스트레인 노드 정리
        pm.parent( consts, self.template.const_grp )

    def rig(self):
        pass
    
    
class Head(RigModule):
    def __init__(self):
        super(Head,self).__init__()  
              
        self._jointFile    = 'head_joint.ma'
        self._templateFile = 'head_template.ma'        
        self._templatePrefix = 'headTmp'
        self._jointNode_checkList    = ['neck_jnt','head_jnt','headEnd_jnt']
        self._templateNode_checkList = ['root', 'head_up']
        
        # 씬에 필요 노드가 이미 존재하는지 체크
        try:
            self.registJoint()
        except:
            pass
        
        try:
            self.registTemplate()
        except:
            pass
        
    def registJoint(self):
        super(Head,self).registJoint()
              
        # 필요 노드 등록
        self.joint.neck         = pm.PyNode( 'neck_jnt' )
        self.joint.head         = pm.PyNode( 'head_jnt' )
        self.joint.headEnd      = pm.PyNode( 'headEnd_jnt' )
        
    def registTemplate(self):
        super(Head,self).registTemplate()
        
        prefix = self._templatePrefix +'_'
        
        # 필요 노드 등록
        self.template.head_pos         = pm.PyNode( prefix+'root')
        self.template.head_rot         = pm.PyNode( prefix+'head_up_zro')
        self.template.head_back        = pm.PyNode( prefix+'head_back_zro')
        self.template.head_up          = pm.PyNode( prefix+'headEnd_zro')
        self.template.head_up_zro      = pm.PyNode( prefix+'neck_aim_zro')
        self.template.head_up_zro      = pm.PyNode( prefix+'neck_zro')
        
        self.template.head_up_zro      = pm.PyNode( prefix+'head_up')
        self.template.head_up_zro      = pm.PyNode( prefix+'head_back')
        self.template.head_up_zro      = pm.PyNode( prefix+'neck_aim')
        
        self.template.head_up_zro      = pm.PyNode( prefix+'result_neck')
        self.template.head_up_zro      = pm.PyNode( prefix+'result_head')
        self.template.head_up_zro      = pm.PyNode( prefix+'result_headEnd')
        

         
    def createJoint(self):
        super(Head,self).createJoint()
        
    def createTemplate(self):
        super(Head,self).createTemplate()
        
        snapList = [
            ['root',            'head_jnt',     'parent', (0,0,0)],
            ['head_up_zro',     'headEnd_jnt',  'parent', (0,0,0)],
            ['head_back_zro',   'head_jnt',     'parent', (0,0,0)],
            ['headEnd_zro',     'headEnd_jnt',  'parent', (0,0,0)],            
            ['neck_aim_zro',    'neck_jnt',     'parent', (0,0,0)],
            ['neck_zro',        'neck_jnt',     'parent', (0,0,0)],
            
            ['head_up',         'headEnd_jnt',  'parent', (2,0,0)],
            ['head_back',       'head_jnt',     'parent', (0,5,0)],
            ['neck_aim',        'neck_jnt',     'parent', (-2,0,0)],
            ]
        
        #constList = []
        
        # ----------------------------------
        #
        # 조인트에 템플릿 위치시킴
        #
        # ----------------------------------
        self.joint.head.r.set(0,0,0)
        self.joint.neck.r.set(0,0,0)
        
        for layout, jnt, snapType, offset in snapList:
            layout = pm.PyNode( 'headLayout_'+layout )
            snap( layout, jnt, snapType )
            layout.t.set(offset)

        
        # 템플릿을 살짝 띄움.
        self.template.head_up.tx.set(2)
        
        # ----------------------------------
        #
        # 템플릿에 조인트 컨스트레인
        #
        # ----------------------------------
        
        # 로테이션 우선 처리 > 포지션 처리
        consts = []
        #self.template.upperLid_rot.rz >> self.joint.upperLid.joz
        #self.template.lowerLid_rot.rz >> self.joint.lowerLid.joz                
        consts.append( pm.orientConstraint( self.template.head_rot,     self.joint.head ) )
        consts.append( pm.pointConstraint( self.template.head_pos,      self.joint.head ) )        
        
        # 컨스트레인 노드 정리
        pm.parent( consts, self.template.const_grp )


def getFilePath():
    # ma파일 오픈
    tmp   = __file__.replace('\\','/')
    split = tmp.split('/')        
    filePath = '/'.join(split[:-1]) + '/files/'
    return filePath    

def eyeTest():
    jointFile = 'eye_joint.ma'
    layoutFile = 'eye_template.ma'
    layoutPrefix = 'eyeLayout'
    side = 'L'
    
    jointList = ['eye__SIDE__jnt', 'eyeBall__SIDE__jnt', 'iris__SIDE__jnt', 'upperLid__SIDE__jnt', 'upperLidEnd__SIDE__jnt', 'lowerLid__SIDE__jnt', 'lowerLidEnd__SIDE__jnt']
    
    snapList = [
        ['root',            'head_jnt',     'parent'],
        ['head_up_zro',     'headEnd_jnt',  'parent'],
        ['head_back_zro',   'head_jnt',     'parent'],
        ['headEnd_zro',     'headEnd_jnt',  'parent'],            
        ['neck_aim_zro',    'neck_jnt',     'parent'],
        ['neck_zro',        'neck_jnt',     'parent'],
        
        ['head_up',         'headEnd_jnt',  'parent'],
        ['head_back',       'head_jnt',     'parent'],
        ['neck_aim',        'neck_jnt',     'parent'],
        ]

    offsets = [        
        ['head_up',   (2,0,0)],
        ['head_back', (0,5,0)],
        ['neck_aim',  (-2,0,0)],
        ]
    
    constList = [
        ['result_neck','neck_jnt'],
        ['result_head','head_jnt'],
        ['result_headEnd','headEnd_jnt'],
        ]
    
    joint = Struct()
    layout = Struct()
    
    
    #--------------------------
    #
    # 파일 오픈
    #
    #--------------------------    
    filePath = getFilePath()
    
    # 조인트 파일 임포트
    if not pm.objExists('head_jnt'):
        pm.importFile( filePath + jointFile )
    
    # 템플릿 파일 임포트
    pm.importFile(  filePath + layoutFile , 
                    returnNewNodes=True, 
                    renameAll=True, 
                    renamingPrefix=layoutPrefix )  # @UnusedVariable
    layoutPrefix += '_'
    
    # ----------------------------------
    #
    # 조인트에 템플릿 위치시킴
    #
    # ----------------------------------
    for jnt in jointList:
        attr = jnt.split('__SIDE__')[0]
        jnt = pm.PyNode(jnt)
        jnt.rename( jnt.name().replace('__SIDE__','_%s_'%side) )        
        joint.__setattr__( attr, jnt)
        
    pm.select( joint.iris )
    print joint.iris.name()
    
    
def headTest():
    jointFile = 'head_joint.ma'
    layoutFile = 'head_template.ma'
    layoutPrefix = 'headLayout' 
    
    jointList = ['neck_jnt', 'head_jnt', 'headEnd_jnt']
    
    snapList = [
        ['root',            'head_jnt',     'parent'],
        ['head_up_zro',     'headEnd_jnt',  'parent'],
        ['head_back_zro',   'head_jnt',     'parent'],
        ['headEnd_zro',     'headEnd_jnt',  'parent'],            
        ['neck_aim_zro',    'neck_jnt',     'parent'],
        ['neck_zro',        'neck_jnt',     'parent'],
        
        ['head_up',         'headEnd_jnt',  'parent'],
        ['head_back',       'head_jnt',     'parent'],
        ['neck_aim',        'neck_jnt',     'parent'],
        ]

    offsets = [        
        ['head_up',   (2,0,0)],
        ['head_back', (0,5,0)],
        ['neck_aim',  (-2,0,0)],
        ]
    
    constList = [
        ['result_neck','neck_jnt'],
        ['result_head','head_jnt'],
        ['result_headEnd','headEnd_jnt'],
        ]
   
    #--------------------------
    #
    # 파일 오픈
    #
    #--------------------------
    filePath = getFilePath()
    
    # 조인트 파일 임포트
    if not pm.objExists('head_jnt'):
        pm.importFile( filePath + jointFile )
    
    # 템플릿 파일 임포트
    pm.importFile(  filePath + layoutFile, 
                    returnNewNodes=True, 
                    renameAll=True, 
                    renamingPrefix=layoutPrefix )  # @UnusedVariable
    layoutPrefix += '_'
        

    # ----------------------------------
    #
    # 조인트에 템플릿 위치시킴
    #
    # ----------------------------------      
    for jnt in jointList:
        pm.setAttr( '%s.%s'%(jnt,'r'), (0,0,0))
    
    for layout, jnt, snapType in snapList:
        layout = pm.PyNode( layoutPrefix + layout )
        snap( jnt, layout, snapType )

    for node, offset in offsets:
        node = pm.PyNode( layoutPrefix + node )
        for attr, val in zip(['tx','ty','tz'],offset):
            try:
                pm.setAttr( '%s.%s'%(node,attr), val )
            except:
                pass
    
    consts = []
    for result, jnt in constList:
        layoutNode = pm.PyNode(layoutPrefix + result)
        jnt = pm.PyNode(jnt)
        consts.append( pm.parentConstraint( layoutNode, jnt) )
        layoutNode.jo >> jnt.jo
        
    pm.parent( consts, layoutPrefix + 'const_grp')



def main():
    centerEye = Eye( side='C' )
    #leftEye = Eye( side='L' )
    #rightEye = Eye( side='R' )
    
    centerEye.createJoint()
    #leftEye.createJoint()
    #rightEye.createJoint()
    
    #print leftEye.joints
    
    

    