# coding:utf-8
'''
Created on 2016. 11. 20.

@author: kyuho_choi
'''

import pymel.core as pm
import pymel.core.datatypes as dt

def checkNameConflict():
    ''' 씬 내 이름 충돌 확인 '''
    sameNameList = []
    sel = pm.ls()
    for item in sel:
        if "|" in item.name():
            sameNameList.append(item)
    
    if not sameNameList:
        print u"이름 충돌 없습니다."
        return 
    

    print u"이름 충돌이 있습니다."
    for node in sameNameList:
        print node.name()
        
    pm.select(sameNameList)
    
    return sameNameList

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