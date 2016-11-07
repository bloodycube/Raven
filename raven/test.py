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
    def __init__(self):
        self.jsonFile = 'head.json'
        self.prefix = 'Head'
        
        self.filePath = None
        self.data = None
        
        self.__getFilePath()
        self.__getData()
    
    def __getFilePath(self):
        tmp   = __file__.replace('\\','/')
        split = tmp.split('/')   
        filePath = '/'.join(split[:-1]) + '/files/'
        self.filePath = filePath
    
    def __getData(self):
        # 파일에서 데이터 로딩
        jsonFileLocation = self.filePath + self.jsonFile
        with open( jsonFileLocation, 'r') as fileHdl:
            data = json.loads( fileHdl.read() )
        self.data = data
       
    def createJoint(self):
        fileLocation = self.filePath + self.data['joint']['file']
        pm.importFile( 
            fileLocation, 
            #returnNewNodes=True, 
            #renameAll=True, 
            #renamingPrefix=prefix 
            )  # @UnusedVariable
        
    def createLayout(self):
        # 파일 로딩
        fileLocation = self.filePath + self.data['layout']['file']
        pm.importFile( 
            fileLocation, 
            returnNewNodes=True, 
            renameAll=True, 
            renamingPrefix=self.prefix
            )  # @UnusedVariable
        
        # snap
        for item in self.data['snapLayHdlToJnt']:
            jnt = item['jnt']
            hdl = pm.PyNode( '%s_%s' % ( self.prefix, item['hdl'] ) )
            constType = item['type']
            offset = item['offset']
            
            # 스내핑~
            snap( jnt, hdl, constType=constType)
            
            if offset:
                for attr,val in zip(['tx','ty','tz'], offset):
                    # 어트리뷰트가 잠긴경우 그냥 패스
                    try:
                        hdl.attr(attr).set(val)
                    except:
                        pass
                
        
        # constraint
        for item in self.data['constJntToLayHdl']:
            const_grp  = pm.PyNode( '%s_%s' % ( self.prefix, self.data['layout']['const_grp']))
            outputNode = pm.PyNode( '%s_%s' % ( self.prefix, item['outputNode']) )
            target = pm.PyNode( item['target'] )
            
            const = pm.pointConstraint( outputNode, target )
            outputNode.jo >> target.jo
            
            pm.parent( const, const_grp)
        
class Eye(Module):
    def __init__(self, side='L'):
        super(Head,self).__init__()
        self.jsonFile = 'eye.json'
        self.prefix = 'Eye'
        self.side = side
        

class Head(Module):
    def __init__(self):
        super(Head,self).__init__()
        
        self.jsonFile = 'head.json'
        self.prefix = 'Head'
        
        
        