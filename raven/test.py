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

class Struct():
    pass

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
        self.joint._file = self.__filePath + data['joint']['file']
        
        # 레이아웃 존재 유무 체크용 리스트
        self.joint._nodeList = []
        for item in data['joint']['nodeList']:
            self.joint._nodeList.append( item.replace('__SIDE__',self.__getSideChar()) )
            
        self.rootJnt = data['rootJnt'].replace('__SIDE__',self.__getSideChar() )
        
        # ---------------------------
        #
        # 레이아웃 관련 데이터 파싱
        #
        # ---------------------------
        self.rootLay                    = self.__filePath + data['rootLay']
        self.layout._file               = self.__filePath + data['layout']['file']
        self.layout._importPrefix       = self._prefix + '%sLay_'%self.__getSideChar()
        self.layout._prefix             = self.layout._importPrefix + '_'
        self.layout._const_grp          = self.layout._prefix + data['layout']['const_grp']
        self.layout._constMe_to_parent  = self.layout._prefix + data['layout']['constMe_to_parent']
        
        # 레이아웃 존재 유무 체크용 리스트
        self.layout._nodeList = []
        for item in data['layout']['nodeList']:
            self.layout._nodeList.append( self.layout._prefix + item )
        
        # 스내핑용 데이터
        self.layout._snap_layToJnt  = []
        for item in data['snap_layToJnt']:
            jnt       = item['jnt'].replace('__SIDE__',self.__getSideChar())
            hdl       = self.layout._prefix + item['hdl']
            constType = item['type']
            offset    = item['offset']
            
            self.layout._snap_layToJnt.append( {"joint":jnt, "handle":hdl, "constType":constType, "offset":offset} )
            
        # 컨트트레인용 데이터
        self.layout._const_jntToLay = []
        for item in data['const_JntToLay']:
            outputNode = self.layout._prefix + item['outputNode']
            target     = item['target'].replace('__SIDE__',self.__getSideChar() )
            
            self.layout._const_jntToLay.append( {"outputNode":outputNode, "target":target} )
       
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
         
        # 존재하지 않으면 파일 임포트
        nodes = pm.importFile( self.joint._file, returnNewNodes = True )
        for nodeName in nodes:
            node = pm.PyNode(nodeName)
            node.rename( node.name().replace('__SIDE__',self.__getSideChar()) )
        
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
        pm.importFile( self.layout._file, returnNewNodes = True, renameAll = True, renamingPrefix = self.layout._importPrefix )
        
        # 조인트가 존재하면 레이아웃을 조인트에 붙임.
        if self.isJntExists():
            self.__snap_layTojnt()
            self.__const_jntToLay()

    def isJntExists(self):
        ''' 조인트 존재 유무 체크 '''
        condition = True
        for nodeName in self.joint._nodeList:
            if not pm.objExists(nodeName):
                condition = False
        return condition
    
    def isLayExists(self):
        ''' 레이아웃 존재 유무 체크 '''
        condition = True
        for nodeName in self.layout._nodeList:
            if not pm.objExists(nodeName):
                condition = False
        return condition

    def __snap_layTojnt(self):
        ''' 레이아웃 리그를 조인트에 위치 시킴 '''
        
        # 레이아웃이 존재하지 않으면 에러, 중지.
        if not self.isLayExists():
            raise AttributeError (u"레이아웃 리그가 존재하지 않습니다.")        
        
        # 위치 조정
        for item in self.layout._snap_layToJnt:
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
        for item in self.layout._const_jntToLay:
            outputNode = pm.PyNode( item['outputNode'] )
            target     = pm.PyNode( item['target'] )
            
            # 위치 구속
            const = pm.pointConstraint( outputNode, target )
            
            # 조인트 오리엔트 구속
            outputNode.jo >> target.jo
            
            # 컨스트레인을 컨스트레인 그룹에 페어런트 : 삭제용
            pm.parent( const, self.layout._const_grp)
            
            # 조인트 로테이션을 리셋 시킴
            target.r.set(0,0,0)
        
        # 페어런트 조인트가 존재하면 _constMe_to_parent 노드를 페어런트 조인트에 페어런트
        print self.rootJnt
        rootJnt = pm.PyNode( self.rootJnt )
        parent = rootJnt.getParent()
        if parent:
            consts = []
            consts.append( pm.parentConstraint( parent, self.layout._constMe_to_parent) )
            #consts.append( pm.parentConstraint( parent, self.rootLay) )
            pm.parent(consts, self.layout._const_grp)

    def open_jntFile(self):
        ''' 조인트 파일 오픈 '''
        pm.openFile( self.joint._file, f=True )
        
    def save_jntFile(self):
        ''' 조인트 파일 저장 '''
        sel = pm.selected()
        if not sel:
            raise AttributeError(u'내보낼 노드의 일부를 선택하세요.')
        pm.select( sel[0].root() )
        pm.exportSelected( self.joint._file )
        
    def open_layFile(self):
        ''' 조인트 파일 오픈 '''
        pm.openFile( self.layout._file, f=True )
        
    def save_layFile(self):
        ''' 조인트 파일 저장 '''
        sel = pm.selected()
        if not sel:
            raise AttributeError(u'내보낼 노드의 일부를 선택하세요.')
        pm.select( sel[0].root() )
        pm.exportSelected( self.layout._file )
        
class Eye(Module):
    _jsonFile = 'eye.json'
    _prefix   = 'Eye'
    def __init__(self, side='L', parent='head_jnt' ):
        super(Eye,self).__init__(side, parent)


class Head(Module):
    _jsonFile = 'head.json'
    _prefix   = 'Head'
    def __init__(self, side='', parent=None ):
        super(Head,self).__init__(side, parent)


        
        
        
        
        
        
        