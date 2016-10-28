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
def zeroGroup( *objs, **kwargs):    
    '''
    objs = transform nodes name
    prefix = prefix
    suffix = suffix
    translate = translate zero
    rotate = rotate zero
    scale = scale zero
    '''
    
    # objs inputs
    if objs:
        pm.select(objs)
    objs = pm.ls(sl=True, flatten=True)
    if not objs:
        return
    
    # kwargs inputs
    prefix      = kwargs.get('prefix', '') 
    suffix      = kwargs.get('suffix', '_zro') 
    translate   = kwargs.get('translate',True)
    rotate      = kwargs.get('rotate',True)
    scale       = kwargs.get('scale',True)
    lockAttrZro = kwargs.get('lockZroAttr',True) 

    zeroGrps = []
    for obj in objs:
        obj = pm.PyNode(obj)

        grp = pm.group(n=prefix + obj + suffix, em=True)

        if translate:
            pm.delete(pm.pointConstraint(obj, grp))
        if rotate:
            pm.delete(pm.orientConstraint(obj, grp))
        if scale:
            pm.delete(pm.scaleConstraint(obj, grp))

        parent = obj.getParent()
        if parent:
            grp.setParent(parent)

        if lockAttrZro:
            grp.t.lock()
            grp.r.lock()
            grp.s.lock()
            grp.v.lock()

        obj.setParent(grp)
        zeroGrps.append(grp)

    return zeroGrps


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


def rigCurveConnect(*objs, **kwargs):
    '''
    update : 2015-04-15
    '''
    if objs:
        pm.select(objs)

    sel = pm.selected(type='transform')
    if not sel:
        raise

    obj = sel[0]

    # 삭제
    delete = kwargs.get('delete', False)
    if delete:
        for crvShp in obj.getShapes():
            if crvShp.hasAttr('curveConnectedLOC'):
                try:
                    pm.delete(crvShp, crvShp.curveConnectedLOC.inputs())
                except:
                    pass
        return True

    # 타겟 가져옴.
    target = sel[1]

    name = kwargs.get('name') or kwargs.get('n', target + '_CONNCRV')
    position = kwargs.get('position') or kwargs.get('p', (0, 0, 0))

    # 커브 생성
    crvTrans = pm.curve(n=name, d=1, p=[position, position], k=[0, 1])
    crvShape = crvTrans.getShape()

    # obj에 커브 쉐입을 종속 시킴 : 커브를 선택해도 오브젝트를 선택한 효과를 줌.
    pm.parent(crvShape, obj, r=True, s=True)
    pm.delete(crvTrans)

    # target에 locator를 종속 시킴
    loc = pm.pointCurveConstraint(crvShape + '.ep[1]', ch=True)[0]
    loc = pm.PyNode(loc)
    pm.pointConstraint(target, loc)

    # 로케이서 속성 조정
    loc.getShape().localPosition.set(0, 0, 0)
    loc.getShape().v.set(False)
    loc.v.set(False)
    loc.setParent(obj)
    loc.rename(target + '_CONNLOC')

    # 커브쉐입에 어트리뷰트 추가
    crvShape.addAttr('curveConnectedTo',  at='message')
    crvShape.addAttr('curveConnectedLOC', at='message')

    # 어트리뷰트 연결
    target.message >> crvShape.curveConnectedTo
    loc.   message >> crvShape.curveConnectedLOC

    return loc


def vector_strToVec( inputVal ):
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
        kwargs['aimVector']     = vector_strToVec( kwargs.pop('aim') if 'aim' in kwargs.keys() else kwargs.get('aimVector',    'x') )
        kwargs['upVector']      = vector_strToVec( kwargs.pop('u')   if 'u'   in kwargs.keys() else kwargs.get('upVector',     'y') )
        kwargs['worldUpVector'] = vector_strToVec( kwargs.pop('wu')  if 'wu'  in kwargs.keys() else kwargs.get('worldUpVector','y') )

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
