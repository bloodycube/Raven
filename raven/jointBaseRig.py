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

    def layoutRig_grp(self):
        ''' 노드가 모이는 그룹 세팅 '''
        node = 'layoutRig_grp'
        
        if pm.objExists(node):
            node = pm.PyNode( node )
        else:
            node = pm.group( n=node, em=True )
            
        return node

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
        
        # 페어런팅
        pm.parent( self.layout.parent, self.layoutRig_grp() )
        
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
            snap( parent, self.layout.parent)
            
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

