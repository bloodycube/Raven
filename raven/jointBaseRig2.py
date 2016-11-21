# coding:utf-8
'''
Created on 2016. 11. 20.

@author: kyuho_choi
'''
import os.path
import json
import pymel.core as pm

def getFilesDir():
    ''' 파일폴더 위치 '''
    tmp   = __file__.replace('\\','/')
    split = tmp.split('/')   
    filePath = '/'.join(split[:-1]) + '/files/'
    
    if not os.path.exists(filePath):
        raise AttributeError(u'경로가 존재하지 않아요 : '+filePath)
        
    return filePath


def snap(*obj, **kwargs):
    ''' obj 스내핑 '''
    
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
    pass


class Base(object):
    def __init__(self, jsonFileName=None, prefix='', rigType=None):
        ''' 초기화 '''
        self.__jsonData = None
        self.__prefix   = ''
        self.__rigType  = None
        
        if jsonFileName: 
            self.setJsonData(jsonFileName)
            
        if prefix:
            self.setPrefix(prefix)
            
        if rigType:
            self.setRigType(rigType)
            
        self.tryNodeRegist()

    def setRigType(self, rigType):
        self.__rigType = rigType
        
    def getRigType(self):
        ''' rigType 설정 [joint, layout, rig] '''
        if not self.__rigType  :
            raise AttributeError(u"rigType이 지정되지 않았습니다.")
        
        return self.__rigType        

    def setJsonData(self, jsonFileName ):
        ''' jsonData 설정 '''
        
        # json 파일 경로
        jsonFileLocation = getFilesDir() + jsonFileName
        
        # 파일 유무 체크
        if not os.path.exists(jsonFileLocation):
            raise AttributeError(u'json파일이 존재하지 않아요 : ' + jsonFileLocation)
    
        # json 파일 리딩
        with open( jsonFileLocation, 'r') as fileHdl:
            data = json.loads( fileHdl.read() )
        
        # 데이터 쓰기
        self.__jsonData = data
        
        # 노드 레지스트 시도
        self.tryNodeRegist()
        
    def getJsonData(self):
        ''' jsonData 리턴 '''
        if not self.__jsonData:
            raise AttributeError(u"jsonData가 정의 되지 않았습니다. setJsonData( jsonFileName, key)를 사용하여 데이터를 설정 해주세요.")
        return self.__jsonData
    
    def setPrefix(self, prefix):
        ''' prefix 셋 '''
        self.__prefix = prefix
        
        self.tryNodeRegist()

    def getPrefix(self):
        ''' prefix 겟 '''
        return self.__prefix    

    def isExists(self, printNotExist=False):
        ''' 씬에 필요노드가 존재하는지 검사, 하나라도 없으면 Flase를 출력 '''
        condition = True        
        prefix = self.getPrefix() + "_" if self.getPrefix() else ""
        rigType = self.getRigType()
       
        notExists = [] 
        for node in self.getJsonData()[rigType]['node']:
            nodeName = prefix + node
            if not pm.objExists(nodeName):
                condition = False
                notExists.append(nodeName)
                
        if printNotExist:
            print "notExistsNode =", notExists
            
        return condition
    
    def tryNodeRegist(self):
        ''' 씬에 해당 노드가 존재하는지 시도 '''
        try:
            self.registNode()
        except:            
            pass
    
    def registNode(self):
        ''' 필요노드 등록 '''        
        self.nodes = Struct()
        prefix = self.getPrefix() + "_" if self.getPrefix() else ""
        rigType = self.getRigType()
        
        # 씬에 해당 필요 노드들이 존재하는지 확인
        if not self.isExists():
            raise AttributeError(u'씬에 필요노드가 존재하지 않습니다.')
        
        for item in self.getJsonData()[rigType]['node']:
            # 노드명 확정
            node = prefix + item
            
            # 노드타입 트랜스폼, 조인트만 등록
            if pm.nodeType(node) in ['transform','joint']:
                
                # item을 key, PyNode로 캐스팅 해서 집어 넣음.
                self.nodes.__setattr__( item, pm.PyNode(node) ) 
    
    def printNode(self):
        ''' 노드 목록 출력 '''
        # 내보낼 목록 선택
        sel = pm.selected()
        
        # 선택된게 없으면 에러
        if not sel:
            raise AttributeError(u'출력할 노드 목록의 일부를 선택하세요.')
        
        # prefix 처리
        # 정의된 prefix가 없으면 "", 있으면 prefix 끝에 "_"추가
        prefix = self.getPrefix() + "_" if self.getPrefix() else ""
        
        # 루트들 선택
        roots = []
        for node in sel:
            roots.append( node.root() )
        pm.select( roots, hi=True )
        
        # 다시한번 선택
        sel = pm.selected()
        
        # 아이템들 스트링형식으로 집어넣음 (조인트와 트랜스폼 노드만)
        result=[]
        for node in sel:
            if pm.nodeType(node) in ['transform','joint']:
                
                # prefix가 제외된 노드이름
                nodeName = node.name().replace(prefix,'')
                
                # 결과 추가
                result.append( '"%s", '%nodeName)
                
        # 마지막 아이템에서 ', '을 삭제
        if result:
            result[-1] = result[-1][:-2]
            
        # prefix, subfix 추가
        result.insert(0, '"node":[')
        result.append(']')
        
        # 내용 출력
        print ''.join(result)

    def printStatus(self):
        rigType = self.getRigType()
        
        print "rigType:",   self.getRigType()
        print "jsonData :", self.getJsonData()[rigType]
        print "prefix :",   self.getPrefix()
        print "isExists :", self.isExists()
        print "rigFilePath : (%s), %s" % ( os.path.exists(self.getFilePath()), self.getFilePath()) 
    
    def getFilePath(self):
        ''' 파일경로 리턴 '''
        rigType = self.getRigType()
        
        #return getFilesDir() + self.__jsonData['file']
        return getFilesDir() + self.getJsonData()[rigType]['file']
  
    def importFile(self):
        ''' 리그파일 임포트 '''
        # 씬에 이미 원하는 노드가 존재하는지 검사
        if self.isExists():
            raise AttributeError(u"씬에 이미 노드가 존재합니다.")
        
        # 변수 간단화
        filePath = self.getFilePath()
        prefix   = self.getPrefix()
        
        # 파일 존재유무 검사
        if not os.path.exists(filePath):
            raise AttributeError(u'%s 파일이 존재하지 않아요 : '+filePath)
        
        # 파일 임포트
        if prefix:
            pm.importFile( filePath, returnNewNodes=True, renameAll=True, renamingPrefix=prefix )
        else:
            pm.importFile( filePath, returnNewNodes=True )
            
        # 임포트된 노드 등록
        self.registNode()        
               
    def openFile(self):
        ''' 리그파일 수정용 : 조인트 오픈 '''
        filePath = self.getFilePath()
        
        # 파일 존재유무 검사
        if not os.path.exists(filePath):
            raise AttributeError(u'%s 파일이 존재하지 않아요 : '+filePath)
        
        pm.openFile( filePath, f=True )
        
    def saveFile(self):
        ''' 리그파일 수정용 : 조인트 파일 저장 '''
        filePath = self.getFilePath()
                
        # 뭐라도 하나 선택
        sel = pm.selected()
        if not sel:
            raise AttributeError(u'내보낼 노드의 일부를 선택하세요.')
        pm.select( sel[0].root() )
        
        # 저장
        pm.exportSelected( filePath )
        
    def setup(self):
        ''' 셋업 '''
        self.importFile()
        
    def __snap_layTojnt(self):
        ''' 레이아웃 리그를 조인트에 위치 시킴 '''
        
        # 레이아웃이 존재하지 않으면 에러, 중지.
        if not self.isLayExists():
            raise AttributeError (u"레이아웃 리그가 존재하지 않습니다.")        
        
        self.snap_layToJnt  = []
        for item in data['snap_layToJnt']:
            jnt       = item['jnt'].replace('__SIDE__',self.__getSideChar())
            hdl       = self.layoutPrefix + item['hdl']
            constType = item['type']
            offset    = item['offset']
            
            self.snap_layToJnt.append( {"joint":jnt, "handle":hdl, "constType":constType, "offset":offset} )
            
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
                    
class Joint(Base):
    def __init__(self, jsonFileName=None, prefix=''):
        ''' 초기화 '''
        super(Joint,self).__init__(jsonFileName, prefix, rigType='joint')
        
    def setup(self):
        Base.setup(self)
        
        
class Layout(Base):
    def __init__(self, jsonFileName=None, prefix=''):
        ''' 초기화 '''
        super(Layout,self).__init__(jsonFileName, prefix, rigType='layout')
    
    def setup(self):
        Base.setup(self)


class Rig(Base):
    def __init__(self, jsonFileName=None, prefix=''):
        ''' 초기화 '''
        super(Rig,self).__init__(jsonFileName, prefix, rigType='rig')
       
   
class Module(object):
    def __init__(self, jsonFileName=None, prefix='' ):
        self.joint  = Joint( jsonFileName, prefix)
        self.layout = Layout( jsonFileName, prefix) 
        self.rig    = Rig( jsonFileName, prefix)


class Eye(Module):
    def __init__(self, prefix=None ):
        super(Eye,self).__init__(jsonFileName='eye.json', prefix=prefix)
        