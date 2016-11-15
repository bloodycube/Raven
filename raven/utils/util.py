# coding:utf-8
'''
Created on 2016. 10. 5.

@author: kyuho_choi
'''
import os
import pymel.core as pm
import pymel.core.datatypes as dt

#import pymel.core.datatypes as 

#def zeroGroup(objs=[], prefix='', suffix='_zro', translate=True, rotate=True, scale=False, lockAttrZro=True):


def rigCurveConnect(*objs, **kwargs):
    '''
    update : 2015-04-15
    update : 2016-11-03
    '''
    if objs:
        pm.select(objs)

    sel = pm.selected(type='transform')
    if not sel:
        raise

    obj = sel[0]

    #
    # 삭제
    #
    delete = kwargs.get('delete', False)
    if delete:
        deleteList = []
        
        for crvShp in obj.getShapes():
            if crvShp.hasAttr('curveConnectedLOC'):
                deleteList = [ crvShp, crvShp.curveConnectedLOC.inputs(), crvShp.history( type='nurbsCurve')[-1] ]

        if deleteList:
            pm.delete( deleteList )
            print deleteList
            
        return

    #
    # 생성
    #
    # 타겟 가져옴.
    target = sel[1]

    position = kwargs.get('position') or kwargs.get('p', (0, 0, 0))

    # 커브 생성
    crvTrans = pm.curve( d=1, p=[position, position], k=[0, 1])
    crvShape = crvTrans.getShape()

    # obj에 커브 쉐입을 종속 시킴 : 커브를 선택해도 오브젝트를 선택한 효과를 줌.
    pm.parent(crvShape, obj, r=True, s=True)
    pm.delete(crvTrans)
    crvShape.rename(obj+'Shape')

    # target에 locator를 종속 시킴
    loc, leastSquaresModifier = pm.pointCurveConstraint(crvShape + '.ep[1]', ch=True)
    loc = pm.PyNode(loc)
    leastSquaresModifier = pm.PyNode(leastSquaresModifier)
    const = pm.pointConstraint(target, loc)

    # 로케이서 속성 조정
    loc.getShape().localPosition.set(0, 0, 0)
    loc.getShape().v.set(False)
    loc.v.set(False)
    loc.setParent(obj)
    loc.rename( target + '_locator#')
    const.rename( target + '_pointConst#')

    # 커브쉐입에 어트리뷰트 추가 (깔끔 삭제용)
    crvShape.addAttr('curveConnectedTo',  at='message')
    crvShape.addAttr('curveConnectedLOC', at='message')
    crvShape.addAttr('curveConnectedOrgShape', at='message')    

    # 어트리뷰트 연결
    target.message >> crvShape.curveConnectedTo
    loc.   message >> crvShape.curveConnectedLOC
    
    # 선택
    pm.select(obj)

    return loc


def strToVec( inputVal ):
    '''
    Abstract
    ========
        1. 문자를 벡터형으로 리턴

        2. 예제 :
            >> getVectorByChar( 'x' )
            dt.Vector([1.0, 0.0, 0.0])

            >> getVectorByChar( 'y' )
            dt.Vector([1.0, 1.0, 0.0])

    @param inputVal: 'x','y','z','-x','-y','-z', or vector
    @type inputVal: str | tuple | pm.dt.Vector

    @return : 입력된 캐릭터에 대응하는 벡터
    @rtype : pm.dt.Vector

    @version No 0.7
    '''

    # 입력된 값이 문자열일경우
    if isinstance( inputVal, str ) or isinstance( inputVal, unicode ):

        # 입력된 값을 앞뒤 빈칸을 없애고, 소문자로 변경
        inputVal = inputVal.strip().lower()

        # 아래 리스트에 없는 값이 들어오면 에러
        if not inputVal in ['x','y','z','-x','-y','-z']:
            raise

        # 매칭
        if   inputVal.lower()== 'x': return dt.Vector( 1, 0, 0)
        elif inputVal.lower()=='-x': return dt.Vector(-1, 0, 0)
        elif inputVal.lower()== 'y': return dt.Vector( 0, 1, 0)
        elif inputVal.lower()=='-y': return dt.Vector( 0,-1, 0)
        elif inputVal.lower()== 'z': return dt.Vector( 0, 0, 1)
        elif inputVal.lower()=='-z': return dt.Vector( 0, 0,-1)

    else:
        return dt.Vector( inputVal )


def snap( *args, **kwargs ):
    #TODO : 뭐든 조금 고쳐야 함
    '''
    @TODO : 완전히 작동하게 해야함.
    @param args: 오브젝트 리스트
    @type args: L{PyNode|unicode}

    @keyword type: 'point' | 'orient' | 'parent' | 'scale' | 'aim' | 'trans' | 'compo'
    @keyword aimVector:     type='aim' 일때만 작동
    @keyword upVector:      type='aim' 일때만 작동
    @keyword worldUpVector: type='aim' 일때만 작동

    @return : None
    @rtype : None

    @see Func: locAtCenter
    @version No: 0.5
    @author Name: Kyuho Choi
    @todo 1: 버그 잡아야함.
    
    
    '''
    if args:
        pm.select(args)
    args = pm.ls(sl=True, flatten=True)

    if not args: 
        raise

    type = kwargs.pop('type', 'point')  # @ReservedAssignment
    #print type
    print args

    if type=='point':
        pm.delete( pm.pointConstraint( *args, **kwargs) )
        return

    elif type=='orient':
        pm.delete( pm.orientConstraint( *args, **kwargs) )
        return

    elif type=='parent':
        pm.delete( pm.parentConstraint( *args, **kwargs) )
        return

    elif type=='scale':
        pm.delete( pm.scaleConstraint( *args, **kwargs) )
        return

    elif type=='aim':
        kwargs['aimVector']     = strToVec( kwargs.pop('aim') if 'aim' in kwargs.keys() else kwargs.get('aimVector',    'x') )
        kwargs['upVector']      = strToVec( kwargs.pop('u')   if 'u'   in kwargs.keys() else kwargs.get('upVector',     'y') )
        kwargs['worldUpVector'] = strToVec( kwargs.pop('wu')  if 'wu'  in kwargs.keys() else kwargs.get('worldUpVector','y') )

        if len(args)>2:
            #세개 이상선택 됐을때 세번째 선택된 오브젝트를 up오브젝트로 사용하도록 설정
            kwargs['worldUpType']   = 'object'
            kwargs['worldUpObject'] = args[2]

        pm.delete( pm.aimConstraint( args[0], args[1], **kwargs) )
        return

    elif type=='trans':
        point1 = pm.PyNode(args[0])
        point2 = pm.PyNode(args)

        pos = point1.getTranslation( space='world' )
        point2.setTranslation( pos, space='world')

    elif type=='compo':
        pos = getCenter( args[:-1] )
        point2 = pm.PyNode( args[-1] )
        point2.setTranslation(pos, space='world')
    
        
def getCenter( nodes, getPivot=True, getScalePivot=False ):
    '''
    선택된 컴포턴트나 트렌스폼노드들의 중심좌표를 리턴

    @param nodes: trnasform, or components 노드들
    @type nodes: list

    @param getPivot: (default True),  transform노드의 pivot을 기준으로 작동, 기본값을 True translate를 사용
    @type getPivot: bool

    @param getScalePivot: (default False), getPivot이 True일때 기본으로 rotatePivot을 사용하는데 scalePivot을 사용하고 싶을때 사용.
    @type getScalePivot: bool

    @return : 중심 좌표
    @rtype : pm.dt.Vector
    '''
    result = []
    if getPivot:
        for obj in nodes:
            if pm.nodeType(obj) == 'transform':
                xformResult = pm.xform( obj, q=True, ws=True, pivots=True)
                rtPiv, scPiv = xformResult[:3], xformResult[3:]

                if getScalePivot: res = scPiv
                else:             res = rtPiv

            else:
                res = pm.xform( obj, q=True, ws=True, t=True)

            result.extend( res )
    else:
        result = pm.xform( nodes, q=True, ws=True, t=True)

    # 입력된 자료의 평균값 알아냄
    points = []
    for i in range( len(result)/3 ):
        pnt = i*3
        x,y,z = result[pnt], result[pnt+1], result[pnt+2]
        points.append( dt.Vector(x,y,z) )

    arr = dt.Array(points)
    sum = dt.Vector( arr.sum(0) )  # @ReservedAssignment
    avr = sum / len(points)

    # 결과 리턴
    return avr


def resetMesh(mesh=None):
    # 입력이 있으면 입력된 노드를 선택
    if mesh:
        pm.select(mesh)
        
    # 입력이 없어도 선택된 오브젝트로 입력 대체
    sel = pm.selected( o=True )
    
    # 입력값이 없으면 에러
    if not sel:
        raise

    # obj플러그인 로드
    if not pm.pluginInfo('objExport', q=True, loaded=True):
        pm.loadPlugin('objExport')

    # obj임시 저장 위치
    tmpfile = os.path.expanduser('~') + "/tmpObj.obj"

    # obj Export
    pm.select(mesh)
    pm.exportSelected( tmpfile, typ="OBJexport", options="groups=0;ptgroups=0;materials=0;smoothing=0;normals=0", f=True)

    # obj Import
    newMesh, newMeshShape = pm.importFile(tmpfile, rnn=True)  # @UnusedVariable

    # 임시저장 파일 삭제
    os.remove( tmpfile )
    
    pm.select(newMesh)


def vector_strToVec( inputVal ):
    '''
    update : 2015-04-27
    '''
    # 입력된 값이 문자열일경우
    if isinstance( inputVal, basestring ):
        # 입력된 값을 앞뒤 빈칸을 없애고, 소문자로 변경
        inputVal = inputVal.strip().lower()

        # 아래 리스트에 없는 값이 들어오면 에러
        if not inputVal in ['x','y','z','-x','-y','-z']:
            raise

        # 매칭
        if   inputVal.lower()== 'x': return dt.Vector( 1, 0, 0)
        elif inputVal.lower()=='-x': return dt.Vector(-1, 0, 0)
        elif inputVal.lower()== 'y': return dt.Vector( 0, 1, 0)
        elif inputVal.lower()=='-y': return dt.Vector( 0,-1, 0)
        elif inputVal.lower()== 'z': return dt.Vector( 0, 0, 1)
        elif inputVal.lower()=='-z': return dt.Vector( 0, 0,-1)

    # TODO : 보강이 필요함.
    # 그 외의 값이 입력된경우 
    else:
        return dt.Vector( inputVal )


def jntOrient( objs=[], orient=True, aimAxis='x', upAxis='y', worldAimVector='x', worldUpVector='y', worldUpType='scene'):
    '''
    update : 2015-04-27

    제약사항 :
        같은 오브젝트를 aim, up
    '''

    # args 처리
    if objs:
        pm.select(objs)
    objs = pm.ls(sl=True, type=['joint','transform'])
    if not objs:
        raise

    # 선택된 노드 리스팅
    sel = pm.selected()

    # 플래그 처리
    if worldUpType not in ['scene','object','objectrotation','vector']:
        raise

    aimAxis        = strToVec( aimAxis )
    worldAimVector = strToVec( worldAimVector )
    upAxis         = strToVec( upAxis )
    worldUpVector  = strToVec( worldUpVector ) 

    #=======================================================================
    #
    # Orient Joint to World 처리
    #
    #=======================================================================
    if not orient:  
        pm.joint( objs[0], e=True, oj='none', ch=False, zso=True )
        return

    #=======================================================================
    #
    # 시좍~
    #
    #=======================================================================
    joint  = None
    upObj  = None
    aimObj = None
    delList = []

    if len(objs)==1:
        # 하나만 선택했을때
        # aim축은 worldAimVector
        # up축은 worldUpVector
        # TODO : 조금 애매.. 함. 하나선택했을때 어떻게 동작할지 다시 생각해봐야할듯.

        joint  = objs[0] 
        aimObj = pm.spaceLocator()
        upObj  = pm.spaceLocator()
        delList.extend([aimObj,upObj])

        pm.delete( pm.pointConstraint( joint, aimObj) )    
        pm.delete( pm.pointConstraint( joint, upObj) )
        pm.move( aimObj, worldAimVector, os=True, r=True, wd=True)
        pm.move( upObj,  worldUpVector,  os=True, r=True, wd=True)

        # worldUpType이 'object', 'objecrotation'일경우엔 플래그 설정대로 작동 안함. 여기서 고쳐줌.
        if worldUpType in ['scene', 'vector']:        
            worldUpType = 'object'

    elif len(objs)==2:
        # 오브젝트를 두개 선택했을때.
        # 
        # up축은 마지막에 선택한 오브젝트를 향하고
        # aim축은 자식조인트를 향함.

        # worldAimVector, worldUpVector 플래그는 무시됨.

        selJnts = pm.ls( objs, type='joint' )
        if not selJnts:
            raise 
        joint  = selJnts[0] 

        objs.remove(joint)
        upObj  = objs[-1]

        aimObj = joint.getChildren( type='joint' )
        if not aimObj:
            raise

        # worldUpType이 'scene', 'vector'일경우엔 플래그 설정대로 작동 안함. 여기서 고쳐줌.
        if worldUpType in ['scene', 'vector']:        
            worldUpType = 'object'

    elif len(objs)>2:
        # 세개 이상의 오브젝트를 선택했을때.        
        # up축은 마지막에 선택한 오브젝트를 향하고
        # aim축은 두번째  오브젝트를 향함
        joint  = objs[0] 
        upObj  = objs[-1]   
        aimObj = objs[1]

        # worldUpType이 'scene', 'vector'일경우엔 플래그 설정대로 작동 안함. 여기서 고쳐줌.
        if worldUpType in ['scene', 'vector']:        
            worldUpType = 'object'

    # 더미생성
    joint_Loc = pm.spaceLocator(n='joint_loc')
    aim_Loc   = pm.spaceLocator(n='aim_loc')
    up_Loc    = pm.spaceLocator(n='up_loc')
    delList.extend([joint_Loc, aim_Loc, up_Loc])

    # 더미 위치조정       
    pm.delete( pm.parentConstraint( joint, joint_Loc ) )
    pm.delete( pm.pointConstraint( aimObj, aim_Loc) )    
    pm.delete( pm.pointConstraint( upObj, up_Loc) )

    # joint hierarchy 
    parent = joint.getParent()
    childs = joint.getChildren( type='transform' )

    # 로케이터를 joint와 같은 space에 놓고. 로케이션값 확인
    if parent:
        pm.parent( joint_Loc, parent )    
    pm.aimConstraint( aim_Loc, joint_Loc, aimVector=aimAxis, upVector=upAxis, worldUpType=worldUpType, worldUpVector=worldUpVector, worldUpObject=upObj)
    
    #
    # 결과값
    #
    result = joint_Loc.rotate.get()

    #=======================================================================
    #
    # 조인트에 값 적용
    #
    #=======================================================================
    # 1. joint에 childs(들)을 잠시 unparent
    if childs:
        pm.parent(childs, world=True)

    # 2. joint의 rotate관련 속성들 모두 초기화
    joint.rotate.     set(0,0,0)
    joint.rotateAxis. set(0,0,0)
    joint.jointOrient.set(result)

    # 3. children 있었으면 원상태로 돌림.
    if childs:
        pm.parent(childs, joint, absolute=True)

    #=======================================================================
    #
    # 정리
    #
    #=======================================================================
    # 관련 노드들 삭제
    pm.delete(delList)

    if sel:
        pm.select(sel)