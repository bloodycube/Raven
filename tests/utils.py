'''
Created on 2016. 11. 9.

@author: kyuho_choi
'''
import pymel.core as pm

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

