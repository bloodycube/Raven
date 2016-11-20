# coding:utf-8
'''
Created on 2016. 10. 11.

@author: kyuho_choi
'''
import maya.OpenMaya as OpenMaya
import pymel.core as pm

class PartitionGeo(object):
    '''
    좌우, 상하 타겟 분리를 용이하게 해줌.

    #초기화
    part = PartitionForSplit()

    # 메쉬 등록
    part.setPartitionGeo()

    # 메쉬 어트리뷰트 페인팅


    # 파티션 값 리턴
    left = part.getPartitionWeight('left')
    right = part.getPartitionWeight('right')
    upper = part.getPartitionWeight('upper')
    lower = part.getPartitionWeight('lower')

    '''
    def __init__(self):
        ''' 초기화 '''
        self.__partitionGeo = None
        
    def setPartitionGeo(self, mesh=None):
        ''' 뉴트럴 메쉬 등록 '''
        
        # 입력이 있으면 입력된 노드를 선택
        if mesh:
            pm.select(mesh)
            
        # 입력이 없어도 선택된 오브젝트로 입력 대체
        sel = pm.selected( type=['mesh','transform'] )
        
        # 입력값이 없으면 에러
        if not sel:
            raise

        # 입력 노드타입이 mesh이면 등록
        if pm.nodeType(sel[0])=='mesh':
            mesh = sel[0] 
            
        # 트랜스폼이면 첮번째 쉐입을 등록 
        elif pm.nodeType(sel[0])=='transform':
            mesh = sel[0].getShape()
            
        #
        # 필요 어트리뷰트 추가
        #
        for attr in ['partitionWeight_left','partitionWeight_upper']:
            
            # 어트리뷰트가 이미 존재하면 패스
            if mesh.hasAttr( attr ):
                continue
                
            # 어트리뷰트 추가
            mesh.addAttr( attr, dt='doubleArray')
            
            # 초기값 0으로 채우기
            dv = [ 0.0 for _ in range( mesh.numVertices() )]
            attrName = '%s.%s' % (mesh.name(),attr)
            pm.Attribute( attrName ).set( dv )

        self.__partitionGeo = mesh
        self.setPaintable()
       
    def getPartitionGeo(self):
        ''' 파티션 메쉬 리턴 '''
        return self.__partitionGeo

    def getPartitionWeight(self, side='left'):
        ''' 메쉬에 저장된 값 리턴 '''
        mesh = self.getPartitionGeo()

        left = mesh.partitionWeight_left.get()
        upper = mesh.partitionWeight_upper.get()

        if side == 'left':            
            return left

        elif side =='right':
            return [ 1.0-val for val in left ]

        elif side =='upper':
            return upper

        elif side =='lower':
            return [ 1.0-val for val in upper ]

    def setPaintable(self):
        ''' 
        partitionWeight_left, partitionWeight_upper 값을 페인팅으로 입력.

        페인팅 방법
        1. 메쉬를 선택 > RMB > Paint > mesh > MeshShape.partitionWeight_left.
        1. 메쉬를 선택 > Maya > Window > Paint Attribute Tool

        * RMB 메뉴는 마야 재시동 하면 자동으로 사라짐
        
        '''
        pm.makePaintable( 'mesh', 'partitionWeight_left',  attrType='doubleArray')
        pm.makePaintable( 'mesh', 'partitionWeight_upper', attrType='doubleArray')
        # pm.mel.ArtPaintAttrToolOptions()
        
    
    def setPaintDisable(self):
        ''' partitionWeight_left, partitionWeight_upper paintable Attr 제거, 마야 UI조정 '''        
        #pm.makePaintable(clearAll=True)
        pm.makePaintable( 'mesh', 'partitionWeight_left', remove=True)
        pm.makePaintable( 'mesh', 'partitionWeight_upper', remove=True)


class SplitBlendShape(object):
    '''
    블라블라.
    
    Parameters
    ----------
    var1 : dlfjslf
        설명
        
    var1 : type
        설명

    
    Returns
    -------
    result : type
        설명 


    Sample
    ------
        # 준비물 Nutral, Partition, targets...
    
        # 인스턴스 생성
        split = SplitBlendShape()
    
        # 뉴트럴 메쉬, 파티션 메쉬 등록
        split.setNutralGeo('Nutral_Mesh')
        split.setPartitionGeo('partitionMesh')
    
        # smile메쉬 좌우 분리
        split.setTargetGeo('smile_Mesh')
        split.getSplitTargets(['left','right'])
    
        # frown메쉬 좌우 분리
        split.setTargetGeo('frown_Mesh')
        split.getSplitTargets(['left','right'])
    
        # funnel메쉬 좌상, 우상, 좌하, 우하 분리
        split.setTargetGeo('funnel_Mesh')
        split.getSplitTargets(['UL','UR','DL','DR'])
    
        # lip tighten메쉬 몽땅 분리
        split.setTargetGeo('lip_tighten')
        split.getSplitTargets(['Left','Right','Upper','lower','UL','UR','DL','DR'])


        # 인스턴스 생성
        split = SplitBlendShape()
        
        # 튜트럴 입력
        split.setNutralGeo() # 선택
        split.setNutralGeo('Nutral_Mesh') # 이름지정
        
        # 파티션 입력
        split.setPartitionGeo() # 선택
        split.setPartitionGeo('partitionMesh') # 이름지정
        
        # 타겟 입력
        split.setTargetGeo() # 선택
        split.setNutralGeo('Nutral_Mesh') # 이름지정
        split.setTargetGeo( getRebuildTargetFromShapeEditor()[0] )  # 쉐입에디터
        
        # 분리
        split.getSplitTargets(sides=['left','right'])
        
        
        # 뉴트럴 메쉬, 파티션 메쉬 등록
        split.setNutralGeo('Nutral_Mesh')
        split.setPartitionGeo('partitionMesh')
        
        # smile메쉬 좌우 분리
        split.setTargetGeo('smile_Mesh')
        split.getSplitTargets(['left','right'])
        
        # frown메쉬 좌우 분리
        split.setTargetGeo('frown_Mesh')
        split.getSplitTargets(['left','right'])
        
        # funnel메쉬 좌상, 우상, 좌하, 우하 분리
        split.setTargetGeo('funnel_Mesh')
        split.getSplitTargets(['UL','UR','DL','DR'])
        
        # lip tighten메쉬 몽땅 분리
        split.setTargetGeo('lip_tighten')
        split.getSplitTargets(['Left','Right','Upper','lower','UL','UR','DL','DR'])
        
        
        # 뉴트럴 메쉬, 파티션 메쉬 등록
        split = SplitBlendShape()
        split.setNutralGeo('nutral')
        split.setPartitionGeo('partition')
        
        split.setTargetGeo( getRebuildTargetFromShapeEditor()[0] )  # 쉐입에디터
        split.getSplitTargets(sides=['left','right'])


    '''
    def __init__(self):
        # MPointArray 자료형 newPointArray선언
        self.__nutralGeo = None
        self.__targetGeo = None
        self.__partitionGeo = PartitionGeo()
        self.__nutralPoint = OpenMaya.MPointArray()

    def setNutralGeo(self, mesh=None):
        ''' Nutral Geo 등록 '''
        # 입력이 있으면 입력된 노드를 선택
        if mesh:
            pm.select(mesh)
            
        # 입력이 없어도 선택된 오브젝트로 입력 대체
        sel = pm.selected( type=['mesh','transform'] )
        
        # 입력값이 없으면 에러
        if not sel:
            raise
        
        self.__nutralGeo = sel[0]
        
        pm.select(self.__nutralGeo)
        self.__setNutralVtxPosition()

    def setTargetGeo(self, mesh=None):
        ''' 분리될 타겟 Geo 등록'''
        # 입력이 있으면 입력된 노드를 선택
        if mesh:
            pm.select(mesh)
            
        # 입력이 없어도 선택된 오브젝트로 입력 대체
        sel = pm.selected( type=['mesh','transform'] )
        
        # 입력값이 없으면 에러
        if not sel:
            raise
        
        self.__targetGeo = sel[0]
        
    def setPartitionGeo(self, mesh=None):
        ''' 자동 스플릿을 위한 파티션메쉬 등록 '''
        self.__partitionGeo.setPartitionGeo(mesh)  

    def getSplitTargets(self, sides=['left', 'right'], offset=True):
        ''' 
        타겟 분리

        * 허용 문자
        sides = L, left
                R, right
                U, upper, up
                D, lower, down
                UL, LU, upperLeft
                UR, RU, upperRight
                DL, LD, lowerLeft
                DR, RD, lowerRight                

        '''
        #
        # 입력값 소문자로 변환
        # 입력 : sides = ['L','R','U','D','UP','down','right','upperRight','upperLeft','lowerRight','lowerLeft']
        # 변환 : sides = ['L', 'R', 'U', 'D', 'UL', 'UR', 'DL', 'DR']
        #
        sides = [ side.lower() for side in sides ]
        for i,side in enumerate(sides):
            if side in ['l','left']:
                sides[i] = '1_L'
            elif side in ['r','right']:
                sides[i] = '2_R'
            elif side in ['u','upper','up']:
                sides[i] = '3_U'
            elif side in ['d','lower','down']:
                sides[i] = '4_D'        
            elif side in ['ul','lu','upperleft','leftup']:
                sides[i] = '5_UL'
            elif side in ['ur','ru','upperright','rightup']:
                sides[i] = '6_UR'
            elif side in ['dl','ld','lowerleft','leftdown']:
                sides[i] = '7_DL'
            elif side in ['dr','rd','lowerright','rightdown']:
                sides[i] = '8_DR'                                
        sides = list(set(sides))
        sides.sort()
        sides = [ side.split('_')[-1] for side in sides ]
        
        # 결과 지오메트리를 저장 할 리스트
        resultGeo = []
        
        for i, side in enumerate(sides):
            
            # 웨이트값
            splitWeight=[]

            # 웨이트값 알아옴 
            if side == 'L':                       
                splitWeight = self.__partitionGeo.getPartitionWeight( 'left' )

            elif side == 'R':      
                splitWeight = self.__partitionGeo.getPartitionWeight( 'right' )

            elif side == 'U':     
                splitWeight = self.__partitionGeo.getPartitionWeight( 'upper' )

            elif side == 'D':     
                splitWeight = self.__partitionGeo.getPartitionWeight( 'lower' )

            elif side == 'UL':    
                weight1 = self.__partitionGeo.getPartitionWeight( 'left' )
                weight2 = self.__partitionGeo.getPartitionWeight( 'upper' )
                splitWeight = [w1*w2 for w1, w2 in zip(weight1,weight2)]

            elif side == 'UR':    
                weight1 = self.__partitionGeo.getPartitionWeight( 'right' )
                weight2 = self.__partitionGeo.getPartitionWeight( 'upper' )
                splitWeight = [w1*w2 for w1, w2 in zip(weight1,weight2)]

            elif side == 'DL':    
                weight1 = self.__partitionGeo.getPartitionWeight( 'left' )
                weight2 = self.__partitionGeo.getPartitionWeight( 'lower' )
                splitWeight = [w1*w2 for w1, w2 in zip(weight1,weight2)]

            elif side == 'DR':    
                weight1 = self.__partitionGeo.getPartitionWeight( 'right' )
                weight2 = self.__partitionGeo.getPartitionWeight( 'lower' )
                splitWeight = [w1*w2 for w1, w2 in zip(weight1,weight2)]

            # 메쉬 복사
            dup = pm.duplicate(self.__targetGeo)[0]
            
            # 분리
            pm.select(dup)
            self.__maekSplit( splitWeight )
               
            # 리네임
            dup.rename( '%s_%s' % (self.__targetGeo.name(), side) )
            
            # 위치조정
            if offset:
                min, max = self.__nutralGeo.boundingBox()  # @ReservedAssignment
                width = max.x - min.x
                offset = width + width * 0.2

                dup.tx.set( dup.tx.get() + offset*i + offset )
                
            # 결과 지오메트리 저장
            resultGeo.append(dup)               
                
        
        return resultGeo

    def getNutralGeo(self):
        return self.__nutralGeo
    
    def getTargetGeo(self):
        return self.__targetGeo
    
    def getPartitionGeo(self):
        return self.__partitionGeo
    
    def __setNutralVtxPosition(self):
        ''' Nutral Postion 입력 '''
        #
        # Get selected object : sel = pm.selected와 같음, 선택된 transform node에 접근해서, shape노드를 DAG연결로 찾는 과정임.
        #
        # MSelectionList 자료형 mSelList선언
        mSelList = OpenMaya.MSelectionList()
        
        # 선택된 노드를 mSelList목록에 추가
        OpenMaya.MGlobal.getActiveSelectionList(mSelList)  
         
        # mSelList를 iter형으로 변환, It는 iterate의 약자로 이해하면 됨.
        sel = OpenMaya.MItSelectionList(mSelList)
    
        # MDagPath 자료형 path선언
        dagPath = OpenMaya.MDagPath()
        
        # 선택된 노드에서 dag 노드 추출
        sel.getDagPath(dagPath)                             
    
        # MFnMesh에 선택한 메쉬정보 입력
        # Attach to MFnMesh
        mesh = OpenMaya.MFnMesh(dagPath)                    
    
        for i in range( mesh.numVertices() ):
            # MPoint 자료형 point선언
            point = OpenMaya.MPoint()
    
            # mesh의 i번 위치앖을 point에 넣음
            mesh.getPoint(i, point, OpenMaya.MSpace.kObject )                      
    
            # 결과 pointArray에 추가
            self.__nutralPoint.append(point)
  
    def __maekSplit(self, splitWeight=[]):
        ''' Nutral에 저장된 vtx포인트 정보로 지오메트리 조정 '''        
        #
        # Get selected object : sel = pm.selected와 같음, 선택된 transform node에 접근해서, shape노드를 DAG연결로 찾는 과정임.
        #
        # MSelectionList 자료형 mSelList선언
        mSelList = OpenMaya.MSelectionList()
        
        # 선택된 노드를 mSelList목록에 추가
        OpenMaya.MGlobal.getActiveSelectionList(mSelList)  
         
        # mSelList를 iter형으로 변환, It는 iterate의 약자로 이해하면 됨.
        sel = OpenMaya.MItSelectionList(mSelList)
    
        # MDagPath 자료형 path선언
        dagPath = OpenMaya.MDagPath()
        
        # 선택된 노드에서 dag 노드 추출
        sel.getDagPath(dagPath)                             
    
        # MFnMesh에 선택한 메쉬정보 입력
        # Attach to MFnMesh
        mesh = OpenMaya.MFnMesh(dagPath)    
    
        # Create empty point array to store new points
        pointArray = OpenMaya.MPointArray()              # MPointArray 자료형 newPointArray선언
    
        # print mesh.numVertices(), len(splitWeight)
        
        for i in range( mesh.numVertices() ):
            # MPoint 자료형 point선언
            point = OpenMaya.MPoint()
    
            # mesh의 i번 위치앖을 point에 넣음
            mesh.getPoint(i, point)                      
    
            # 조작
            if point.x:
                # Nutral - (difference) * weight
                point.x = self.__nutralPoint[i].x - (self.__nutralPoint[i].x - point.x) * splitWeight[i]
                point.y = self.__nutralPoint[i].y - (self.__nutralPoint[i].y - point.y) * splitWeight[i]
                point.z = self.__nutralPoint[i].z - (self.__nutralPoint[i].z - point.z) * splitWeight[i]
    
            # 조작결과 newPointArray에 추가
            pointArray.append(point)
    
        # 새로운 위치값을 한방에 메쉬에 적용 
        mesh.setPoints(pointArray)


def getRebuildTargetFromShapeEditor():
    '''
    쉐입 에디터에서 선택된 타겟 목록 얻어옴.
    
    Result: [u'blendShape1.2', u'blendShape1.3']
    [블렌드쉐입노드.타겟ID] 형식으로 리턴됨.
    split(".")으로 블렌드쉐입 노드와, 타겟 ID를 얻어옴.
    
    getShapeEditorTreeviewSelection() 명령어는 
    C:\Program Files\Autodesk\Maya2017\scripts\others\createShapePanelMenu.mel 파일에 있는 스크립트 임.
    '''
       
    # 쉐입 에디터에서 선택한 타겟 목록 리턴
    selectedTargetL = pm.mel.getShapeEditorTreeviewSelection(24)  # @UndefinedVariable
    # selectedTargetL = [u'blendShape2.0', u'blendShape2.1']      # 이런 형식으로 들어옴.
    
    resultMesh = []
    for item in selectedTargetL:
        # .으로 분리
        blendShapeNode, targetID = item.split('.') # blendShape1.1 => blendShape1 1
        
        # int형으로 변환
        targetID = int(targetID)
        
        # pynode로 변환
        blendShapeNode = pm.PyNode( blendShapeNode )
        
        # 타겟명을 알아야 함.
        attrs = blendShapeNode.listAliases()
        targetName = attrs[targetID][0]
        
        # sculptTarget명령어는 타겟이름과 같은 이름의 오브젝트가 존재하면 작동 안함.
        # 타겟이름과 같은 오브젝트가 씬에 있는지 체크
        if pm.objExists(targetName):
            print u' "%s" 타겟과 같은이름의 오브젝트가 이미 존재합니다.'%targetName
            continue
        
        # 타겟 분리
        mesh = pm.sculptTarget( blendShapeNode, e=True, regenerate=True, target=targetID )
        
        # 분리된 메쉬 
        resultMesh.append(mesh)
        
    return resultMesh


def isSelectMeshEnabled():
    '''
      Description:
             Judge target shapes exist or not by treeview selection.
    
      Return Value:
          Return 1 if enabled; otherwise return 0;
    '''
    return pm.mel.isSelectMeshEnabled()  # @UndefinedVariable


def splitBlendShape(nutralGeo, partitionGeo, targetGeo, split=['L','R']):
    '''
    함수버전
    '''
    split = SplitBlendShape()
    split.setNutralGeo(nutralGeo)
    split.setPartitionGeo(partitionGeo)    
    split.setTargetGeo( targetGeo )
    split.getSplitTargets(sides=split)