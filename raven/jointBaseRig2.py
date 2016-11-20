# coding:utf-8
'''
Created on 2016. 11. 20.

@author: kyuho_choi
'''
import json
import pymel.core as pm

def getFilesDir():
    ''' 파일폴더 위치 '''
    tmp   = __file__.replace('\\','/')
    split = tmp.split('/')   
    filePath = '/'.join(split[:-1]) + '/files/'
    return filePath

def getJsonData( fileName ):
    ''' json 파일에서 필요 데이터 파싱 '''
    jsonFileLocation = getFilesDir() + fileName
    with open( jsonFileLocation, 'r') as fileHdl:
        data = json.loads( fileHdl.read() )
    return data

class Struct(object):
    pass

class Base(object):
    def setPrefix(self, prefix):
        ''' prefix 셋 '''
        self.__prefix = prefix

    def getPrefix(self):
        ''' prefix 겟 '''
        return self.__prefix

class Joint(Base):
    def __init__(self):
        pass


class Layout(Base):
    def __init__(self):
        pass
    
class Rig(Base):
    def __init__(self, jsonFileName=None, prefix=None):
        ''' 초기화 '''
        if jsonFileName: 
            self.setData(jsonFileName)
        if prefix:
            self.setPrefix(prefix)
        
    def setData(self, jsonFileName):
        ''' 데이터를 읽고 준비 '''
        data = getJsonData( jsonFileName )['rig']
        self.__rigFile = getFilesDir() + data['file']
    
    def importFile(self):
        ''' 리그파일 임포트 '''
        rigFilePath = self.__rigFile
        prefix      = self.getPrefix()
        
        # 파일 임포트
        nodes = []
        if prefix:
            nodes = pm.importFile( rigFilePath, returnNewNodes=True, renameAll=True, renamingPrefix=prefix+'_' )
        else:
            nodes = pm.importFile( rigFilePath, returnNewNodes=True )
        
        # 노드들 등록(트랜스폼 노드만)
        self.nodes = Struct()
        for node in nodes:
            print pm.nodeType(node)
            if pm.nodeType(node) == 'transform':
                key = node.name().replace( prefix+'_', '' )
                self.nodes.__setattr__( key, node )
        
    def setup(self):
        self.importFile()

    def isExists(self):
        pass
    
    def regist(self):
        pass
    
    def openRigFile(self):
        ''' 리그파일 수정용 : 조인트 오픈 '''
        pm.openFile( self.__rigFile, f=True )
        
    def saveRigFile(self):
        ''' 리그파일 수정용 : 조인트 파일 저장 '''
                
        # 뭐라도 하나 선택
        sel = pm.selected()
        if not sel:
            raise AttributeError(u'내보낼 노드의 일부를 선택하세요.')
        pm.select( sel[0].root() )
        
        # 저장
        pm.exportSelected( self.__rigFile )
        

class Module(object):
    def __init__(self, jsonFileName=None, prefix=None ):
        self.joint  = Joint()
        self.layout = Layout() 
        self.rig    = Rig()
    

class Eye(Module):
    def __init__(self, prefix=None ):
        super(Eye,self).__init__(jsonFileName='eye.json', prefix=prefix)
        