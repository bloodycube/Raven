# coding:utf-8
'''
Created on 2016. 11. 7.

@author: kyuho_choi
'''

import json
import pymel.core as pm

def snap(*obj, **kwargs):
    # 가변인수 처
    if obj:
        pm.select(obj)
    sel = pm.selected()
    if len(sel)<1:
        raise AttributeError(u"두개 이상의 오브젝트를 선택해주세요.")
        
    # 가변 키워드인수 처
    constType = kwargs.get('constType','parent')
    
    # PyNode 리캐스팅
    obj = sel.pop(-1)
    target = sel
    
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

  
def rigSymTranslate(sourceObj, targetObj):
    ''' 
    yz 평면 기준으로 뒤집음
    아래코드의 리깅 버전.
    디폴트는 YZ플랜을 기준.

    sel = pm.selected()    

    tx = sourceObj.tx.get()
    ty = sourceObj.ty.get()    
    rz = sourceObj.rz.get()

    targetObj.tx.set(-tx)
    targetObj.ty.set(ty)
    targetObj.tz.set(0)
    targetObj.rx.set(0)
    targetObj.ry.set(180)
    targetObj.rz.set(-rz) 
    '''
    # TODO: 매트릭스노드로 변경.

    # 컨트롤 노드
    symTr_grp = pm.group(n='symTranslate__%s_TO_%s' %
                         (sourceObj.name(), targetObj.name()), em=True)

    # 어트리뷰트 설정
    symTr_grp.addAttr('input_t', at='double3')
    symTr_grp.addAttr('input_tx', p='input_t', keyable=True)
    symTr_grp.addAttr('input_ty', p='input_t', keyable=True)
    symTr_grp.addAttr('input_tz', p='input_t', keyable=True)
    symTr_grp.addAttr('input_r', at='double3')
    symTr_grp.addAttr('input_rx', p='input_r', keyable=True)
    symTr_grp.addAttr('input_ry', p='input_r', keyable=True)
    symTr_grp.addAttr('input_rz', p='input_r', keyable=True)
    symTr_grp.addAttr('input_s', at='double3')
    symTr_grp.addAttr('input_sx', p='input_s', keyable=True)
    symTr_grp.addAttr('input_sy', p='input_s', keyable=True)
    symTr_grp.addAttr('input_sz', p='input_s', keyable=True)

    symTr_grp.addAttr('mult_t', at='double3')
    symTr_grp.addAttr('mult_tx', p='mult_t', keyable=True)
    symTr_grp.addAttr('mult_ty', p='mult_t', keyable=True)
    symTr_grp.addAttr('mult_tz', p='mult_t', keyable=True)
    symTr_grp.addAttr('mult_r', at='double3')
    symTr_grp.addAttr('mult_rx', p='mult_r', keyable=True)
    symTr_grp.addAttr('mult_ry', p='mult_r', keyable=True)
    symTr_grp.addAttr('mult_rz', p='mult_r', keyable=True)
    symTr_grp.addAttr('mult_s', at='double3')
    symTr_grp.addAttr('mult_sx', p='mult_s', keyable=True)
    symTr_grp.addAttr('mult_sy', p='mult_s', keyable=True)
    symTr_grp.addAttr('mult_sz', p='mult_s', keyable=True)

    symTr_grp.addAttr('offset_t', at='double3')
    symTr_grp.addAttr('offset_tx', p='offset_t', keyable=True)
    symTr_grp.addAttr('offset_ty', p='offset_t', keyable=True)
    symTr_grp.addAttr('offset_tz', p='offset_t', keyable=True)
    symTr_grp.addAttr('offset_r', at='double3')
    symTr_grp.addAttr('offset_rx', p='offset_r', keyable=True)
    symTr_grp.addAttr('offset_ry', p='offset_r', keyable=True)
    symTr_grp.addAttr('offset_rz', p='offset_r', keyable=True)
    symTr_grp.addAttr('offset_s', at='double3')
    symTr_grp.addAttr('offset_sx', p='offset_s', keyable=True)
    symTr_grp.addAttr('offset_sy', p='offset_s', keyable=True)
    symTr_grp.addAttr('offset_sz', p='offset_s', keyable=True)

    symTr_grp.addAttr('output_t', at='double3')
    symTr_grp.addAttr('output_tx', p='output_t', keyable=True)
    symTr_grp.addAttr('output_ty', p='output_t', keyable=True)
    symTr_grp.addAttr('output_tz', p='output_t', keyable=True)
    symTr_grp.addAttr('output_r', at='double3')
    symTr_grp.addAttr('output_rx', p='output_r', keyable=True)
    symTr_grp.addAttr('output_ry', p='output_r', keyable=True)
    symTr_grp.addAttr('output_rz', p='output_r', keyable=True)
    symTr_grp.addAttr('output_s', at='double3')
    symTr_grp.addAttr('output_sx', p='output_s', keyable=True)
    symTr_grp.addAttr('output_sy', p='output_s', keyable=True)
    symTr_grp.addAttr('output_sz', p='output_s', keyable=True)

    # Transform조작
    symTr_grp.mult_t.set(-1, 1, 1)
    symTr_grp.mult_r.set(-1, -1, -1)
    symTr_grp.mult_s.set(1, 1, 1)
    symTr_grp.offset_t.set(0, 0, 0)
    symTr_grp.offset_r.set(0, 180, 0)
    symTr_grp.offset_s.set(0, 0, 0)

    # 곱셈노드, 덧셈 노드 생성
    md_t = pm.createNode('multiplyDivide')
    md_r = pm.createNode('multiplyDivide')
    md_s = pm.createNode('multiplyDivide')
    pma_t = pm.createNode('plusMinusAverage')
    pma_r = pm.createNode('plusMinusAverage')
    pma_s = pm.createNode('plusMinusAverage')

    # 계산노드들에 값 입력
    symTr_grp.input_t >> md_t.input1
    symTr_grp.input_r >> md_r.input1
    symTr_grp.input_s >> md_s.input1
    symTr_grp.mult_t >> md_t.input2
    symTr_grp.mult_r >> md_r.input2
    symTr_grp.mult_s >> md_s.input2
    symTr_grp.offset_t >> pma_t.input3D[1]
    symTr_grp.offset_r >> pma_r.input3D[1]
    symTr_grp.offset_s >> pma_s.input3D[1]

    # 입력된 값을 처리 하는 리깅: 곱셈을 먼저 처리, 나중에 덧셈.
    md_t.output >> pma_t.input3D[0]
    md_r.output >> pma_r.input3D[0]
    md_s.output >> pma_s.input3D[0]

    # 출력
    pma_t.output3D >> symTr_grp.output_t
    pma_r.output3D >> symTr_grp.output_r
    pma_s.output3D >> symTr_grp.output_s

    # 입력, 출력에 선택한 노드 꼽음.
    sourceObj.t >> symTr_grp.input_t
    symTr_grp.output_t >> targetObj.t
    sourceObj.r >> symTr_grp.input_r
    symTr_grp.output_r >> targetObj.r
    sourceObj.s >> symTr_grp.input_s
    symTr_grp.output_s >> targetObj.s

    pm.select(sourceObj)
    return symTr_grp


class Struct(object):
    ''' 리그 자료형 '''
    def getList(self):
        result = []
        lst = self.__dict__.values()
        for item in lst:            
            if pm.objExists( item ):
                result.append( item )
        return result
    

class Module(object):
    _jsonFile = None
    _prefix = None
    
    def __init__(self, side=None, parent=None):
        ''' 초기화 '''
        self.__side     = side        
        self.__filePath = None
        self.__parent   = parent
        self.joint  = Struct()
        self.layout = Struct()
        
        self.__getFilePath()
        self.__getData() 
    
    def __getFilePath(self):
        ''' 파일폴더 위치 '''
        tmp   = __file__.replace('\\','/')
        split = tmp.split('/')   
        filePath = '/'.join(split[:-1]) + '/files/'
        self.__filePath = filePath
    
    def __getData(self):
        ''' json 파일에서 필요 데이터 파싱 '''
        # ---------------------------
        #
        # json 파일 로딩
        #
        # ---------------------------
        jsonFileLocation = self.__filePath + self._jsonFile
        with open( jsonFileLocation, 'r') as fileHdl:
            data = json.loads( fileHdl.read() )            
                
        # ---------------------------
        #
        # 조인트 관련 데이터 파싱
        #
        # ---------------------------
        self.jointFile = self.__filePath + data['jointFile']
        
        self.jointNodeList = []
        for item in data['jointNodeList']:
            newName = item.replace('__SIDE__',self.__getSideChar() )
            self.jointNodeList.append( newName ) 
            
        self.rootJnt = []
        for item in data['rootJnt']:
            newName = item.replace('__SIDE__',self.__getSideChar() )
            self.rootJnt.append( newName )
        
        # ---------------------------
        #
        # 레이아웃 관련 데이터 파싱
        #
        # ---------------------------
        self.layoutFile           = self.__filePath + data['layoutFile']
        self.layout_importPrefix  = self._prefix + '%sLay_'%self.__getSideChar()
        self.layoutPrefix         = self.layout_importPrefix + '_'
        
        # 레이아웃 노드명 리스트에 등록 
        self.layoutNodeList = []
        for item in data['layoutNodeList']:
            newName = self.layoutPrefix + item
            self.layoutNodeList.append( newName )
               
        # 스내핑용 데이터
        self.snap_layToJnt  = []
        for item in data['snap_layToJnt']:
            jnt       = item['jnt'].replace('__SIDE__',self.__getSideChar())
            hdl       = self.layoutPrefix + item['hdl']
            constType = item['type']
            offset    = item['offset']
            
            self.snap_layToJnt.append( {"joint":jnt, "handle":hdl, "constType":constType, "offset":offset} )
            
        # 컨트트레인용 데이터
        self.const_jntToLay = []
        for item in data['const_JntToLay']:
            outputNode = self.layoutPrefix + item['outputNode']
            target     = item['target'].replace('__SIDE__',self.__getSideChar() )
            
            self.const_jntToLay.append( {"outputNode":outputNode, "target":target} )
       
    def __getSideChar(self):
        ''' side 캐릭터 처리 '''
        side = self.__side
        if side:
            side = '_%s_'%side
        else:
            side = '_'
        return side
    
    def createJoint(self):
        ''' 조인트 생성 '''
        
        # 이미 조인트가 존재하는지 확인
        if self.isJntExists():
            raise AttributeError (u"조인트가 이미 존재합니다.")
         
        # 존재하지 않으면 파일 임포트, PyNode로 리턴됨
        nodes = pm.importFile( self.jointFile, returnNewNodes = True )

        # __SIDE__로 표시된 노드, 이름 변경
        for node in nodes:
            node.rename( node.name().replace('__SIDE__', self.__getSideChar() ) )
            
        # 임포트한 노드들 등록
        self.registJoint()

        # 페어런트 노드가 존재하면 루트조인트 페어런트
        if self.__parent and pm.objExists(self.__parent):
            pm.parent( self.rootJnt, self.__parent )
        
        # 레이아웃이 이미 존재하면 레이아웃에 조인트를 붙임
        if self.isLayExists():
            self.__const_jntToLay()
        
    def createLayout(self):
        ''' 레이아웃 생성 '''  
        
        # 레이아웃이 이미 존재하면 레이아웃에 조인트를 붙임
        if self.isLayExists():
            raise AttributeError (u"레이아웃용 리그가 이미 존재합니다.")
         
        # 존재하지 않으면 파일 임포트
        pm.importFile( self.layoutFile, returnNewNodes = True, renameAll = True, renamingPrefix = self.layout_importPrefix )
        
        # 임포트한 노드들 등록
        self.registLayout()
        
        # 조인트가 존재하면 레이아웃을 조인트에 붙임.
        if self.isJntExists():
            self.__snap_layTojnt()
            self.__const_jntToLay()
    
    def registJoint(self):
        ''' self.joint에 joint 노드 등록 '''
        if not self.isJntExists():
            raise AttributeError (u"조인트 노드가 존재하지 않습니다.")
            
        for nodeName in self.jointNodeList:
            attr = nodeName.split('_')[0]
            node = pm.PyNode( nodeName )
            self.joint.__setattr__( attr , node )            

    def registLayout(self):
        ''' self.joint에 joint 노드 등록 '''
        if not self.isLayExists():
            raise AttributeError (u"레이아웃 노드가 존재하지 않습니다.")
            
        for nodeName in self.layoutNodeList:
            attr = nodeName.replace( self.layoutPrefix,'') # prefix를 떼버림
            node = pm.PyNode( nodeName )
            self.layout.__setattr__( attr , node )
           
    def isJntExists(self):
        ''' 조인트 존재 유무 체크 '''
        condition = True
        for nodeName in self.jointNodeList:
            if not pm.objExists(nodeName):
                condition = False
        return condition
    
    def isLayExists(self):
        ''' 레이아웃 존재 유무 체크 '''
        condition = True
        for nodeName in self.layoutNodeList:
   
            if not pm.objExists(nodeName):
                condition = False
        return condition

    def __snap_layTojnt(self):
        ''' 레이아웃 리그를 조인트에 위치 시킴 '''
        
        # 레이아웃이 존재하지 않으면 에러, 중지.
        if not self.isLayExists():
            raise AttributeError (u"레이아웃 리그가 존재하지 않습니다.")        
        
        # 위치 조정
        for item in self.snap_layToJnt:
            # 요소 분리
            jnt       = pm.PyNode( item['joint'] )
            hdl       = pm.PyNode( item['handle'] )
            constType = item['constType']
            offset    = item['offset']
            
            # 스내핑~
            snap( jnt, hdl, constType=constType)
            
            # 옵셋
            if offset:
                for attr, val in zip(['tx','ty','tz'], offset):
                    
                    # 어트리뷰트가 잠긴경우 그냥 패스
                    try:
                        hdl.attr(attr).set(val)
                    except:
                        pass
    
    def __const_jntToLay(self):
        ''' 조인트를 레이아웃 핸들에 구속 '''
        
        # 레이아웃이 존재하지 않으면 에러, 중지.
        if not self.isLayExists():
            raise AttributeError (u"레이아웃 리그가 존재하지 않습니다.")   
        
        # 조인트를 레이아웃 핸들에 구속
        for item in self.const_jntToLay:
            outputNode = pm.PyNode( item['outputNode'] )
            target     = pm.PyNode( item['target'] )
           
            # 위치 구속
            const = pm.pointConstraint( outputNode, target )
            
            # 조인트 로테이션 구속
            outputNode.r >> target.r
            
            # 조인트 오리엔트 구속
            outputNode.jo >> target.jo
            
            # 컨스트레인을 컨스트레인 그룹에 페어런트 : 삭제용
            pm.parent( const, self.layout.const_grp)
            
            # 조인트 로테이션을 리셋 시킴: 로테이션이 구속되어 적용 불가.. 혹시 필요할지도 몰라 놔뒀음. 조인트 로테이션 리셋은 여기서 해야함.
            #target.r.set(0,0,0)
        
        # 페어런트 조인트가 존재하면 constMe_to_parent 노드를 페어런트 조인트에 페어런트
        rootJnt = pm.PyNode( self.rootJnt[0] )
        parent = rootJnt.getParent()
        if parent:
            consts = []
            consts.append( pm.parentConstraint( parent, self.layout.constMe_to_parent) )
            
            # 루트를 임시로 빼고
            pm.parent( self.layout.root, w=True)
            
            # 페어런트에 스내핑
            snap( self.layout.parent, parent)
            
            # 컨스트레인을 건다음
            consts.append( pm.parentConstraint( parent, self.layout.parent) )
            
            # 다시 페어런트
            pm.parent( self.layout.root, self.layout.parent )
            
            # 생성된 컨스트레인 레이아웃에 포함시킴
            pm.parent(consts, self.layout.const_grp)

    def deleteLayout(self):
        # 레이아웃이 존재하지 않으면 에러, 중지.
        if not self.isLayExists():
            raise AttributeError (u"레이아웃 리그가 존재하지 않습니다.") 
        
        # 레이아웃 삭제 (parent를 한번에 삭제 할경우 찌그러지는 현상 생김)
        pm.delete( self.layout.const_grp )
        pm.delete( self.layout.parent )


    def open_jntFile(self):
        ''' 조인트 파일 오픈 '''
        pm.openFile( self.jointFile, f=True )
        
    def save_jntFile(self):
        ''' 조인트 파일 저장 '''
        sel = pm.selected()
        if not sel:
            raise AttributeError(u'내보낼 노드의 일부를 선택하세요.')
        pm.select( sel[0].root() )
        pm.exportSelected( self.jointFile )
        
    def open_layFile(self):
        ''' 조인트 파일 오픈 '''
        pm.openFile( self.layoutFile, f=True )
        
    def save_layFile(self):
        ''' 조인트 파일 저장 '''
        sel = pm.selected()
        if not sel:
            raise AttributeError(u'내보낼 노드의 일부를 선택하세요.')
        pm.select( sel[0].root() )
        pm.exportSelected( self.layoutFile )
        

class Head(Module):
    _jsonFile = 'head.json'
    _prefix   = 'Head'
    def __init__(self, side='', parent=None ):
        super(Head,self).__init__(side, parent)


class Jaw(Module):
    _jsonFile = 'jaw.json'
    _prefix   = 'Jaw'
    def __init__(self, side='', parent='head_jnt' ):
        super(Jaw,self).__init__(side, parent)


class Eye(Module):
    _jsonFile = 'eye.json'
    _prefix   = 'Eye'
    def __init__(self, side='L', parent='head_jnt' ):
        super(Eye,self).__init__(side, parent)

