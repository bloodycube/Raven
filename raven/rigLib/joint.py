# coding:utf-8
'''
Created on 2016. 11. 20.

@author: kyuho_choi
'''

import pymel.core as pm
import pymel.core.datatypes as dt

def strToVec( inputVal ):
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