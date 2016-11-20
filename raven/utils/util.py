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

