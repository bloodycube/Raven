# coding:utf-8

'''
Created on 2016. 9. 29.

@author: kyuho_choi

pm.select('FacialBS')
'''
# TODO: 좌우 자동 분리 코드 필요

# TODO: 눈썹 바인딩 코드 필요.

# TODO: 컨트롤러와 블렌드쉐입 중간을 매개하는 컨트롤러 필요.

# TODO: Attribute Renamer

# TODO: Blendshape Attribute Renamer

# TODO: Animation Clip Creator

# TODO: 

import pymel.core as pm

__blenTxt = ''

# TODO: UI와 코드 분리.
def ui():
    global __blenTxt
    if pm.window('blendShapeCtrlerUI', q=True, exists=True):
        pm.deleteUI('blendShapeCtrlerUI')

    with pm.window('blendShapeCtrlerUI'):
        with pm.columnLayout(adj=True):
            pm.button(l='Slider', c=pm.Callback(slider))
            pm.button(l='Both Side Slider', c=pm.Callback(bothShide))
            pm.button(l='Square Slider', c=pm.Callback(square))
            pm.button(l='Square(small) Slider', c=pm.Callback(square_small))
            
            with pm.rowLayout(nc=3):
                pm.button(l='Sym Translate', c=pm.Callback(rigSymTranslate))  

            pm.separator(h=16, style='in')
            with pm.rowLayout(nc=3):
                pm.button(
                    l='SetBlendShapeNode', w=100, c=pm.Callback(setBlendShapeNode))
                __blenTxt = pm.text(l='')
            with pm.rowLayout(nc=3):
                pm.button(l='Connect Blen', w=100, c=pm.Callback(connectBlen))
                pm.button(
                    l='DisConnect Blen', w=100, c=pm.Callback(disconnectBlen))

            pm.separator(h=16, style='in')
            with pm.rowLayout(nc=3):
                pm.button(l='Regist Ctrl', w=80, c=pm.Callback(registBlenCtrl))
                pm.button(l='Reset All', w=80, c=pm.Callback(resetBlenCtrl))
                pm.button(l='Reset Selected', w=80, c=pm.Callback(resetCtrl))
            pm.separator(h=8, style='in')
            with pm.rowLayout(nc=3):
                pm.button(l='Pose To Shelf', w=100, c=pm.Callback(poseToShelf))

def getAttrsFromChannelbox():
    '''
    채널박스에서 선택된 어트리뷰트 이름 리턴
    블렌드 쉐입은 잘 안됨..ㅠㅠㅠ
    @return: 어트리뷰트 리스트 리턴
    '''
    mainObjs = pm.channelBox(
        pm.melGlobals['gChannelBoxName'], q=True, mainObjectList=True)
    mainAttrs = pm.channelBox(
        pm.melGlobals['gChannelBoxName'], q=True, selectedMainAttributes=True)

    shapeObjs = pm.channelBox(
        pm.melGlobals['gChannelBoxName'], q=True, shapeObjectList=True)
    shapeAttrs = pm.channelBox(
        pm.melGlobals['gChannelBoxName'], q=True, selectedShapeAttributes=True)

    histObjs = pm.channelBox(
        pm.melGlobals['gChannelBoxName'], q=True, historyObjectList=True)
    histAttrs = pm.channelBox(
        pm.melGlobals['gChannelBoxName'], q=True, selectedHistoryAttributes=True)

    outputObjs = pm.channelBox(
        pm.melGlobals['gChannelBoxName'], q=True, outputObjectList=True)
    outputAttrs = pm.channelBox(
        pm.melGlobals['gChannelBoxName'], q=True, selectedOutputAttributes=True)

    shortNames = []
    for pair in ((mainObjs, mainAttrs), (shapeObjs, shapeAttrs), (histObjs, histAttrs), (outputObjs, outputAttrs)):
        objs, attrs = pair
        # print pair
        if attrs:
            for obj in objs:
                for attr in attrs:
                    shortNames.append('%s.%s' % (obj, attr))

    longNames = []
    for pair in ((mainObjs, mainAttrs), (shapeObjs, shapeAttrs), (histObjs, histAttrs), (outputObjs, outputAttrs)):
        objs, attrs = pair
        # print pair
        if attrs is not None:
            for node in objs:
                result = [
                    objs[0] + '.' + pm.attributeQuery(attr, n=node, ln=True) for attr in attrs]
                longNames.extend(result)

    longNames = list(set(longNames))

    return shortNames

    # return "%s.%s"%(mainObjs[-1],mainAttrs[-1])


# TODO: 하나의 클래스로 변경 (square, bothside, slider)

def square():
    #
    # Guide
    #
    # guide Shape
    guide = pm.curve(d=3, p=[(1.0, 1.2499999999999998, 1.1102230246251568e-16), (0.3333333333333333, 1.25, 3.70074341541719e-17), (-0.3333333333333333, 1.2500000000000002, -3.7007434154171876e-17), (-1.0, 1.2500000000000004, -1.1102230246251565e-16), (-1.0653009999999998, 1.2500000000000002, -1.2552203720872514e-16), (-1.195903, 1.1959030000000004, -1.5452150670114405e-16), (-1.25, 1.0653010000000005, -1.6653345369377348e-16), (-1.25, 1.0000000000000004, -1.6653345369377348e-16), (-1.25, 0.33333333333333376, -5.551115123125783e-17), (-1.2500000000000002, -0.3333333333333328, 5.551115123125783e-17), (-1.2500000000000004, -0.9999999999999994, 1.6653345369377348e-16), (-1.2500000000000004, -1.0653009999999994, 1.665334536937735e-16), (-1.1959030000000004, -1.1959029999999995, 1.545215067011441e-16), (-1.0653009999999998, -1.2499999999999996, 1.255220372087251e-16), (-1.0, -1.2499999999999998, 1.1102230246251568e-16), (-0.3333333333333333, -1.25, 3.70074341541719e-17),
                             (0.3333333333333333, -1.2500000000000002, -3.7007434154171876e-17), (1.0, -1.2500000000000004, -1.1102230246251565e-16), (1.0653009999999998, -1.2500000000000004, -1.2552203720872514e-16), (1.195903, -1.1959030000000006, -1.5452150670114405e-16), (1.25, -1.0653010000000005, -1.6653345369377348e-16), (1.25, -1.0000000000000007, -1.6653345369377348e-16), (1.25, -0.3333333333333339, -5.551115123125783e-17), (1.2500000000000002, 0.3333333333333328, 5.551115123125783e-17), (1.2500000000000004, 0.9999999999999996, 1.6653345369377348e-16), (1.2500000000000004, 1.0653009999999996, 1.665334536937735e-16), (1.1959030000000004, 1.1959029999999997, 1.545215067011441e-16), (1.0653009999999998, 1.2499999999999998, 1.255220372087251e-16), (1.0, 1.2499999999999998, 1.1102230246251568e-16)], k=[0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 5.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 8.0, 9.0, 9.0, 9.0, 10.0, 10.0, 10.0, 11.0, 12.0, 12.0, 12.0])
    guide.getShape().overrideEnabled.set(True)
    guide.getShape().overrideDisplayType.set(1)  # Template

    # snapPoint
    tmp = pm.spaceLocator()
    tmp.localScale.set(0, 0, 0)
    tmp.getShape().overrideEnabled.set(1)
    tmp.getShape().overrideDisplayType.set(2)  # Reference

    snapLoc = []
    snapPnts = [(0, 0), (0, 1), (1, 1), (1, 0), (1, -1),
                (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for x, y in snapPnts:
        loc = pm.duplicate(tmp)[0]
        loc.localPositionX.set(x)
        loc.localPositionY.set(y)
        pm.parent(loc.getShape(), guide, s=True, r=True)
        snapLoc.append(loc)

    pm.delete(snapLoc, tmp)

    guide.rename('guide')
    for shp in guide.getShapes():
        shp.rename('ctrlGuideShape#')

    #
    # Ctrl
    #
    # ctrl Shape
    ctrl = pm.curve(d=3, p=[(-0.2, 0.0, 0.0), (-0.2, -0.052240800000000004, 1.1599787796967576e-17), (-0.1567224, -0.1567224, 3.479936339090273e-17), (0.0, -0.2216388, 4.921369978205803e-17), (0.1567224, -0.1567224, 3.479936339090273e-17), (0.2, -0.052240800000000004, 1.1599787796967576e-17), (0.2, 0.0, 0.0), (0.2, 0.052240800000000004, -
                                                                                                                                                                                                                                                                                                                        1.1599787796967576e-17), (0.1567224, 0.1567224, -3.479936339090273e-17), (0.0, 0.2216388, -4.921369978205803e-17), (-0.1567224, 0.1567224, -3.479936339090273e-17), (-0.2, 0.052240800000000004, -1.1599787796967576e-17), (-0.2, 0.0, 0.0)], k=[2.0, 2.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.0, 10.0])
    ctrl.setLimit("translateMinX", -1)
    ctrl.setLimit("translateMinY", -1)
    ctrl.setLimit("translateMinZ", 0)
    ctrl.setLimit("translateMaxX", 1)
    ctrl.setLimit("translateMaxY", 1)
    ctrl.setLimit("translateMaxZ", 0)
    ctrl.rename('ctrl')

    # add Attr
    for attr in ['outMaxX', 'outMinX', 'outMaxY', 'outMinY']:
        ctrl.addAttr(attr, dv=0, min=0, max=1, keyable=True)
        ctrl.setAttr(attr, keyable=False, lock=False, channelBox=True)

    # Attr Lock
    for attr in ['tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']:
        ctrl.setAttr(attr, keyable=False, lock=True, channelBox=False)

    # Setdriven #1
    sdks = [
        # driverAttr, driverVal, drivenAttr, drivenVal
        (ctrl.tx,  0, ctrl.outMaxX, 0),
        (ctrl.tx,  0, ctrl.outMinX, 0),
        (ctrl.ty,  0, ctrl.outMaxY, 0),
        (ctrl.ty,  0, ctrl.outMinY, 0),
        (ctrl.tx,  1, ctrl.outMaxX, 1),
        (ctrl.tx, -1, ctrl.outMinX, 1),
        (ctrl.ty,  1, ctrl.outMaxY, 1),
        (ctrl.ty, -1, ctrl.outMinY, 1),
    ]
    for driverAttr, driverVal, drivenAttr, drivenVal in sdks:
        pm.setDrivenKeyframe(drivenAttr, currentDriver=driverAttr, driverValue=driverVal,
                             value=drivenVal, inTangentType='linear', outTangentType='linear')

    # parent
    pm.parent(ctrl, guide)
    pm.select(guide)

    return ctrl, guide

def square_small():
    #
    # Guide
    #
    # guide Shape
    guide = pm.curve( d=3, p=[ (1.0, 1.2499999999999998, 1.1102230246251568e-16), (0.6666666865348816, 1.25, 3.70074341541719e-17), (0.33333334326744074, 1.2500000000000002, -3.7007434154171876e-17), (0.0, 1.2500000000000004, -1.1102230246251565e-16), (-0.06530099999999983, 1.2500000000000002, -1.2552203720872514e-16), (-0.19590299999999994, 1.1959030000000004, -1.5452150670114405e-16), (-0.25, 1.0653010000000005, -1.6653345369377348e-16), (-0.25, 1.0000000000000004, -1.6653345369377348e-16), (-0.25, 0.6666666865348816, -5.551115123125783e-17), (-0.2500000000000002, 0.3333333432674408, 5.551115123125783e-17), (-0.25000000000000044, 5.551115123125783e-16, 1.6653345369377348e-16), (-0.25000000000000044, -0.06530099999999939, 1.665334536937735e-16), (-0.19590300000000038, -0.1959029999999995, 1.545215067011441e-16), (-0.06530099999999983, -0.24999999999999956, 1.255220372087251e-16), (0.0, -0.24999999999999978, 1.1102230246251568e-16), (0.33333334326744074, -0.25, 3.70074341541719e-17), (0.6666666865348816, -0.25, -3.7007434154171876e-17), (1.0, -0.25000000000000044, -1.1102230246251565e-16), (1.0653009999999998, -0.25000000000000044, -1.2552203720872514e-16), (1.195903, -0.1959030000000006, -1.5452150670114405e-16), (1.25, -0.0653010000000005, -1.6653345369377348e-16), (1.25, -6.661338147750939e-16, -1.6653345369377348e-16), (1.25, 0.3333333432674408, -5.551115123125783e-17), (1.2500000000000002, 0.6666666865348816, 5.551115123125783e-17), (1.2500000000000004, 0.9999999999999996, 1.6653345369377348e-16), (1.2500000000000004, 1.0653009999999996, 1.665334536937735e-16), (1.1959030000000004, 1.1959029999999997, 1.545215067011441e-16), (1.0653009999999998, 1.2499999999999998, 1.255220372087251e-16), (1.0, 1.2499999999999998, 1.1102230246251568e-16) ], k=[ 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 5.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 8.0, 9.0, 9.0, 9.0, 10.0, 10.0, 10.0, 11.0, 12.0, 12.0, 12.0 ] )
    guide.getShape().overrideEnabled.set(True)
    guide.getShape().overrideDisplayType.set(1)  # Template

    # snapPoint
    tmp = pm.spaceLocator()
    tmp.localScale.set(0, 0, 0)
    tmp.getShape().overrideEnabled.set(1)
    tmp.getShape().overrideDisplayType.set(2)  # Reference

    snapLoc = []
    snapPnts = [(0, 0), (0, 1), (1, 1), (1, 0)]
    for x, y in snapPnts:
        loc = pm.duplicate(tmp)[0]
        loc.localPositionX.set(x)
        loc.localPositionY.set(y)
        pm.parent(loc.getShape(), guide, s=True, r=True)
        snapLoc.append(loc)

    pm.delete(snapLoc, tmp)

    guide.rename('guide')
    for shp in guide.getShapes():
        shp.rename('ctrlGuideShape#')

    #
    # Ctrl
    #
    # ctrl Shape
    ctrl = pm.curve(d=3, p=[(-0.2, 0.0, 0.0), (-0.2, -0.052240800000000004, 1.1599787796967576e-17), (-0.1567224, -0.1567224, 3.479936339090273e-17), (0.0, -0.2216388, 4.921369978205803e-17), (0.1567224, -0.1567224, 3.479936339090273e-17), (0.2, -0.052240800000000004, 1.1599787796967576e-17), (0.2, 0.0, 0.0), (0.2, 0.052240800000000004, -
                                                                                                                                                                                                                                                                                                                        1.1599787796967576e-17), (0.1567224, 0.1567224, -3.479936339090273e-17), (0.0, 0.2216388, -4.921369978205803e-17), (-0.1567224, 0.1567224, -3.479936339090273e-17), (-0.2, 0.052240800000000004, -1.1599787796967576e-17), (-0.2, 0.0, 0.0)], k=[2.0, 2.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.0, 10.0])
    ctrl.setLimit("translateMinX", 0)
    ctrl.setLimit("translateMinY", 0)
    ctrl.setLimit("translateMinZ", 0)
    ctrl.setLimit("translateMaxX", 1)
    ctrl.setLimit("translateMaxY", 1)
    ctrl.setLimit("translateMaxZ", 0)
    ctrl.rename('ctrl')

    # add Attr
    for attr in ['outX', 'outY']:
        ctrl.addAttr(attr, dv=0, min=0, max=1, keyable=True)
        ctrl.setAttr(attr, keyable=False, lock=False, channelBox=True)

    # Attr Lock
    for attr in ['tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']:
        ctrl.setAttr(attr, keyable=False, lock=True, channelBox=False)

    # Setdriven #1
    sdks = [
        # driverAttr, driverVal, drivenAttr, drivenVal
        (ctrl.tx,  0, ctrl.outX, 0),
        (ctrl.ty,  0, ctrl.outY, 0),
        (ctrl.tx,  1, ctrl.outX, 1),
        (ctrl.ty,  1, ctrl.outY, 1),
    ]
    for driverAttr, driverVal, drivenAttr, drivenVal in sdks:
        pm.setDrivenKeyframe(drivenAttr, currentDriver=driverAttr, driverValue=driverVal,
                             value=drivenVal, inTangentType='linear', outTangentType='linear')

    # parent
    pm.parent(ctrl, guide)
    pm.select(guide)
    
    # Edit Attr
    for attr in ['outX', 'outY']:
        ctrl.setAttr(attr, keyable=False, lock=True, channelBox=True)

    return ctrl, guide

def bothShide():
    #
    # Guide
    #
    # guide Shape
    guide = pm.curve(d=3, p=[(0.0, -0.24999999999999978, -1.1102230246251565e-16), (0.33333333333333326, -0.25000000000000017, -3.7007434154171876e-17), (0.6666666666666665, -0.2500000000000004, 3.7007434154171864e-17), (1.0, -0.2500000000000004, 1.1102230246251573e-16), (1.0653009999999998, -0.2500000000000003, 1.2552203720872516e-16), (1.195903, -0.19590300000000044, 1.5452150670114405e-16), (1.2770485000000003, -4.0659597910774894e-16, 1.725394271900882e-16), (1.1959030000000004, 0.19590299999999966, 1.545215067011441e-16), (1.0653009999999998, 0.24999999999999978, 1.255220372087251e-16), (1.0, 0.24999999999999983, 1.1102230246251568e-16), (0.6666666666666667, 0.25000000000000017, 3.700743415417189e-17), (0.3333333333333335, 0.2500000000000004, -3.700743415417189e-17), (0.0, 0.25000000000000033, -1.1102230246251565e-16), (-0.33333333333333326, 0.25000000000000017,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     3.700743415417189e-17), (-0.6666666666666666, 0.2500000000000004, -3.700743415417189e-17), (-1.0, 0.25000000000000033, -1.1102230246251565e-16), (-1.0653009999999998, 0.2500000000000002, -1.2552203720872514e-16), (-1.195903, 0.19590300000000038, -1.5452150670114405e-16), (-1.2770485, 4.0659597910774894e-16, -1.725394271900882e-16), (-1.1959030000000002, -0.1959029999999996, -1.545215067011441e-16), (-1.065301, -0.2499999999999997, -1.2552203720872514e-16), (-1.0, -0.24999999999999978, -1.1102230246251565e-16), (-0.6666666666666667, -0.25000000000000017, -3.7007434154171876e-17), (-0.3333333333333335, -0.2500000000000004, 3.7007434154171864e-17), (2.220446049250313e-16, -0.2500000000000004, 1.1102230246251573e-16)], k=[6.0, 6.0, 6.0, 8.0, 8.0, 8.0, 9.0, 10.0, 11.0, 12.0, 12.0, 12.0, 14.0, 14.0, 14.0, 16.0, 16.0, 16.0, 17.0, 18.0, 19.0, 20.0, 20.0, 20.0, 22.0, 22.0, 22.0])
    guide.getShape().overrideEnabled.set(True)
    guide.getShape().overrideDisplayType.set(1)  # Template

    # snapPoint
    tmp = pm.spaceLocator()
    tmp.localScale.set(0, 0, 0)
    tmp.getShape().overrideEnabled.set(1)
    tmp.getShape().overrideDisplayType.set(2)  # Reference

    snapLoc = []
    snapPnts = [(0, 0), (1, 0), (-1, 0)]
    for x, y in snapPnts:
        loc = pm.duplicate(tmp)[0]
        loc.localPositionX.set(x)
        loc.localPositionY.set(y)
        pm.parent(loc.getShape(), guide, s=True, r=True)
        snapLoc.append(loc)

    pm.delete(snapLoc, tmp)

    guide.rename('guide')
    for shp in guide.getShapes():
        shp.rename('ctrlGuideShape#')

    #
    # Ctrl
    #
    # ctrl Shape
    ctrl = pm.curve(d=3, p=[(-0.2, 0.0, 0.0), (-0.2, -0.052240800000000004, 1.1599787796967576e-17), (-0.1567224, -0.1567224, 3.479936339090273e-17), (0.0, -0.2216388, 4.921369978205803e-17), (0.1567224, -0.1567224, 3.479936339090273e-17), (0.2, -0.052240800000000004, 1.1599787796967576e-17), (0.2, 0.0, 0.0), (0.2, 0.052240800000000004, -
                                                                                                                                                                                                                                                                                                                        1.1599787796967576e-17), (0.1567224, 0.1567224, -3.479936339090273e-17), (0.0, 0.2216388, -4.921369978205803e-17), (-0.1567224, 0.1567224, -3.479936339090273e-17), (-0.2, 0.052240800000000004, -1.1599787796967576e-17), (-0.2, 0.0, 0.0)], k=[2.0, 2.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.0, 10.0])
    ctrl.setLimit("translateMinX", -1)
    ctrl.setLimit("translateMinY", 0)
    ctrl.setLimit("translateMinZ", 0)
    ctrl.setLimit("translateMaxX", 1)
    ctrl.setLimit("translateMaxY", 0)
    ctrl.setLimit("translateMaxZ", 0)
    ctrl.rename('ctrl')

    # add Attr
    for attr in ['outMax', 'outMin']:
        ctrl.addAttr(attr, dv=0, min=0, max=1, keyable=True)
        ctrl.setAttr(attr, keyable=False, lock=False, channelBox=True)

    # Attr Lock
    for attr in ['ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']:
        ctrl.setAttr(attr, keyable=False, lock=True, channelBox=False)

    # Setdriven #1
    sdks = [
        # driverAttr, driverVal, drivenAttr, drivenVal
        (ctrl.tx,  0, ctrl.outMax, 0),
        (ctrl.tx,  0, ctrl.outMin, 0),
        (ctrl.tx,  1, ctrl.outMax, 1),
        (ctrl.tx, -1, ctrl.outMin, 1),
    ]
    for driverAttr, driverVal, drivenAttr, drivenVal in sdks:
        pm.setDrivenKeyframe(drivenAttr, currentDriver=driverAttr, driverValue=driverVal,
                             value=drivenVal, inTangentType='linear', outTangentType='linear')

    # parent
    pm.parent(ctrl, guide)
    pm.select(guide)

    return ctrl, guide


def slider():
    #
    # Guide
    #
    # guide Shape
    guide = pm.curve(d=3, p=[(1.6653345369377348e-16, 0.2500000000000002, -1.1102230246251563e-16), (-0.06530099999999994, 0.2500000000000002, -1.2552203720872514e-16), (-0.19590299999999994, 0.19590300000000038, -1.5452150670114405e-16), (-0.27704850000000003, 4.0659597910774894e-16, -1.725394271900882e-16), (-0.19590300000000016, -0.1959029999999996, -1.545215067011441e-16), (-0.06530100000000005, -0.2499999999999997, -1.2552203720872514e-16), (0.0, -0.24999999999999978, -1.1102230246251565e-16), (0.3333333333333333, -0.25000000000000017, -3.7007434154171876e-17), (0.6666666666666665, -0.2500000000000004, 3.7007434154171864e-17), (1.0000000000000002, -0.2500000000000004, 1.1102230246251573e-16),
                             (1.065301, -0.2500000000000003, 1.2552203720872516e-16), (1.195903, -0.19590300000000044, 1.5452150670114405e-16), (1.2770485, -4.0659597910774894e-16, 1.725394271900882e-16), (1.1959030000000002, 0.19590299999999966, 1.545215067011441e-16), (1.0653009999999998, 0.24999999999999978, 1.255220372087251e-16), (1.0, 0.24999999999999983, 1.1102230246251568e-16), (0.6666666666666667, 0.25000000000000017, 3.700743415417189e-17), (0.33333333333333337, 0.2500000000000004, -3.700743415417189e-17), (5.551115123125783e-17, 0.25000000000000033, -1.1102230246251565e-16)], k=[2.0, 2.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0, 8.0, 8.0, 8.0, 9.0, 10.0, 11.0, 12.0, 12.0, 12.0, 14.0, 14.0, 14.0])
    guide.getShape().overrideEnabled.set(True)
    guide.getShape().overrideDisplayType.set(1)  # Template

    # snapPoint
    tmp = pm.spaceLocator()
    tmp.localScale.set(0, 0, 0)
    tmp.getShape().overrideEnabled.set(1)
    tmp.getShape().overrideDisplayType.set(2)  # Reference

    snapLoc = []
    snapPnts = [(0, 0), (1, 0)]
    for x, y in snapPnts:
        loc = pm.duplicate(tmp)[0]
        loc.localPositionX.set(x)
        loc.localPositionY.set(y)
        pm.parent(loc.getShape(), guide, s=True, r=True)
        snapLoc.append(loc)

    pm.delete(snapLoc, tmp)

    guide.rename('guide')
    for shp in guide.getShapes():
        shp.rename('ctrlGuideShape#')

    #
    # Ctrl
    #
    # ctrl Shape
    ctrl = pm.curve(d=3, p=[(-0.2, 0.0, 0.0), (-0.2, -0.052240800000000004, 1.1599787796967576e-17), (-0.1567224, -0.1567224, 3.479936339090273e-17), (0.0, -0.2216388, 4.921369978205803e-17), (0.1567224, -0.1567224, 3.479936339090273e-17), (0.2, -0.052240800000000004, 1.1599787796967576e-17), (0.2, 0.0, 0.0), (0.2, 0.052240800000000004, -
                                                                                                                                                                                                                                                                                                                        1.1599787796967576e-17), (0.1567224, 0.1567224, -3.479936339090273e-17), (0.0, 0.2216388, -4.921369978205803e-17), (-0.1567224, 0.1567224, -3.479936339090273e-17), (-0.2, 0.052240800000000004, -1.1599787796967576e-17), (-0.2, 0.0, 0.0)], k=[2.0, 2.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.0, 10.0])
    ctrl.setLimit("translateMinX", 0)
    ctrl.setLimit("translateMinY", 0)
    ctrl.setLimit("translateMinZ", 0)
    ctrl.setLimit("translateMaxX", 1)
    ctrl.setLimit("translateMaxY", 0)
    ctrl.setLimit("translateMaxZ", 0)
    ctrl.rename('ctrl')

    # add Attr
    for attr in ['output']:
        ctrl.addAttr(attr, dv=0, min=0, max=1, keyable=True)
        ctrl.setAttr(attr, keyable=False, lock=False, channelBox=True)

    # Attr Lock
    for attr in ['ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']:
        ctrl.setAttr(attr, keyable=False, lock=True, channelBox=False)

    # Setdriven #1
    sdks = [
        # driverAttr, driverVal, drivenAttr, drivenVal
        (ctrl.tx,  0, ctrl.output, 0),
        (ctrl.tx,  1, ctrl.output, 1),
    ]
    for driverAttr, driverVal, drivenAttr, drivenVal in sdks:
        pm.setDrivenKeyframe(drivenAttr, currentDriver=driverAttr, driverValue=driverVal,
                             value=drivenVal, inTangentType='linear', outTangentType='linear')

    # parent
    pm.parent(ctrl, guide)
    pm.select(guide)

    return ctrl, guide


def convertCombinationToUtil( ):
    ''' 마야2017용 combinationShape노드를 하위버전 호환을 위해 util리깅으로 변환'''
    sel = pm.ls(sl=True, type='combinationShape')
    
    #comb = sel[0]
    for comb in sel:
        method = comb.combinationMethod.get()
        
        inputs = comb.inputs( plugs=True )
        outputs = comb.outputWeight.outputs( plugs=True )
        
        if not outputs:
            continue
        
        utilType = ''
        
        if method==0: # multi                       
            util = pm.createNode('multiplyDivide')
            inputs[0] >> util.input1X
            inputs[1] >> util.input2X
            
            for _ in outputs:
                util.outputX >> outputs[0] 
            
            utilType = 'Mult'      
          
            
        elif method==1: # multi
            util = pm.createNode('clamp')  # @ReservedAssignment
            inputs[0] >> util.inputR
            inputs[1] >> util.maxR
            util.minR.set(0)        
            
            for _ in outputs:
                util.outputR >> outputs[0]
                
            utilType = 'Min'
    
        
        util.rename( 'blenCorr_%s__%s__%s'%( utilType, inputs[0].getAlias(),inputs[1].getAlias() ) )
        comb.rename('deleteMe__'+comb.name())

def eyeSDK():
    sdks = []
    
    sdks.append(['eye_L_ctrl.eye_L_up_63',    0, 'eyeball_L_sdk.rz',   0])
    sdks.append(['eye_L_ctrl.eye_L_up_63',    1, 'eyeball_L_sdk.rz',  15])
    sdks.append(['eye_L_ctrl.eye_L_down_64',  0, 'eyeball_L_sdk.rz',   0])
    sdks.append(['eye_L_ctrl.eye_L_down_64',  1, 'eyeball_L_sdk.rz', -36])
    
    sdks.append(['eye_R_ctrl.eye_R_up_63',    0, 'eyeball_R_sdk.rz',   0]) 
    sdks.append(['eye_R_ctrl.eye_R_up_63',    1, 'eyeball_R_sdk.rz',  15])
    sdks.append(['eye_R_ctrl.eye_R_down_64',  0, 'eyeball_R_sdk.rz',   0])
    sdks.append(['eye_R_ctrl.eye_R_down_64',  1, 'eyeball_R_sdk.rz', -36])
    
    sdks.append(['eye_L_ctrl.eye_L_Left_61',  0, 'eyeball_L_sdk.ry',   0])
    sdks.append(['eye_L_ctrl.eye_L_Left_61',  1, 'eyeball_L_sdk.ry',  36])
    sdks.append(['eye_L_ctrl.eye_L_Right_62', 0, 'eyeball_L_sdk.ry',   0])
    sdks.append(['eye_L_ctrl.eye_L_Right_62', 1, 'eyeball_L_sdk.ry', -36])
    
    sdks.append(['eye_R_ctrl.eye_R_Left_61',  0, 'eyeball_R_sdk.ry',   0])
    sdks.append(['eye_R_ctrl.eye_R_Left_61',  1, 'eyeball_R_sdk.ry',  36])
    sdks.append(['eye_R_ctrl.eye_R_Right_62', 0, 'eyeball_R_sdk.ry',   0])
    sdks.append(['eye_R_ctrl.eye_R_Right_62', 1, 'eyeball_R_sdk.ry', -36])
    
    sdks.append(['upperLid_L_ctrl.upperLid_L_raiser_05',  0, 'upperLid_L_sdk.rz', 0])
    sdks.append(['upperLid_L_ctrl.upperLid_L_raiser_05',  1, 'upperLid_L_sdk.rz', -10])
    sdks.append(['upperLid_L_ctrl.upperLid_L_lowerer',    0, 'upperLid_L_sdk.rz', 0])
    sdks.append(['upperLid_L_ctrl.upperLid_L_lowerer',    1, 'upperLid_L_sdk.rz', 40])
    
    sdks.append(['upperLid_R_ctrl.upperLid_R_raiser_05',  0, 'upperLid_R_sdk.rz', 0])
    sdks.append(['upperLid_R_ctrl.upperLid_R_raiser_05',  1, 'upperLid_R_sdk.rz', -10])
    sdks.append(['upperLid_R_ctrl.upperLid_R_lowerer',    0, 'upperLid_R_sdk.rz', 0])
    sdks.append(['upperLid_R_ctrl.upperLid_R_lowerer',    1, 'upperLid_R_sdk.rz', 40]) 
      
    sdks.append(['lowerLid_L_ctrl.lowerLid_L_raiser',     0, 'lowerLid_L_sdk.rz', 0])
    sdks.append(['lowerLid_L_ctrl.lowerLid_L_raiser',     1, 'lowerLid_L_sdk.rz', -22])
    sdks.append(['lowerLid_L_ctrl.lowerLid_L_lowerer',    0, 'lowerLid_L_sdk.rz', 0])
    sdks.append(['lowerLid_L_ctrl.lowerLid_L_lowerer',    1, 'lowerLid_L_sdk.rz', 15])
    
    sdks.append(['lowerLid_R_ctrl.lowerLid_R_raiser',     0, 'lowerLid_R_sdk.rz', 0])
    sdks.append(['lowerLid_R_ctrl.lowerLid_R_raiser',     1, 'lowerLid_R_sdk.rz', -22])
    sdks.append(['lowerLid_R_ctrl.lowerLid_R_lowerer',    0, 'lowerLid_R_sdk.rz', 0])
    sdks.append(['lowerLid_R_ctrl.lowerLid_R_lowerer',    1, 'lowerLid_R_sdk.rz', 15])
    
    for driverAttr, driverVal, drivenAttr, drivenVal in sdks:
        pm.setDrivenKeyframe(drivenAttr, currentDriver=driverAttr, driverValue=driverVal,
                             value=drivenVal, inTangentType='linear', outTangentType='linear')

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
__rigTypeKeyword = 'blendShapeCtrl'
__blendShapeNode = ''


def __setBlen():
    blen = pm.selected(type='blendShape')
    if blen:
        for ctrl in __getCrvUI_ctrls():
            pm.addAttr(ctrl, ln="blendShapeNode", at="message")
            blen.message >> ctrl.blendShapeNode


def registBlenCtrl():
    ''' 블렌드쉐입 컨트롤러 등록 '''
    for node in pm.selected():
        if not node.hasAttr('rigType'):
            node.addAttr('rigType', dt='string')
            node.rigType.set('blendShapeCtrl')


def resetBlenCtrl():
    ''' 블렌드쉐입 컨트롤러 리셋.'''
    blendShapeCtrls = __getCrvUI_ctrls()

    for node in blendShapeCtrls:
        try:
            node.tx.set(0)
        except:
            pass
        try:
            node.ty.set(0)
        except:
            pass
        try:
            node.tz.set(0)
        except:
            pass


def resetCtrl():
    for node in pm.selected():
        for attr in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz']:
            try:
                pm.PyNode('%s.%s' % (node, attr)).set(0)
            except:
                pass


def __getCrvUI_ctrls():
    blendShapeCtrls = []
    for node in pm.ls(type='transform'):
        if node.hasAttr('rigType'):
            if node.rigType.get() == __rigTypeKeyword:
                blendShapeCtrls.append(node)
    return blendShapeCtrls


def __getCrvUI_blenAttrs():
    attrs = []
    for ctrl in __getCrvUI_ctrls():
        attrs.extend(ctrl.listAttr(userDefined=True, scalar=True))
    return attrs


def __getCrvUI_keyAttrs():
    attrs = []
    for ctrl in __getCrvUI_ctrls():
        attrs.extend(ctrl.listAttr(keyable=True))
    return attrs


def setBlendShapeNode():
    global __blendShapeNode

    sel = pm.selected(type='blendShape')
    if sel:
        __blendShapeNode = sel[0]
        pm.text(__blenTxt, e=True, l=__blendShapeNode)
        return __blendShapeNode


def connectBlen():
    if not __blendShapeNode:
        print u'select blendShapeNode'
        return

    for attr in __getCrvUI_blenAttrs():
        attrName = attr.name().split('.')[-1]
        try:
            attr >> pm.Attribute('%s.%s' % (__blendShapeNode, attrName))
        except:
            pass


def disconnectBlen():
    for attr in __getCrvUI_blenAttrs():
        outputs = attr.outputs(plugs=True)
        for destinationAttr in outputs:
            if destinationAttr.nodeType() == 'blendShape':
                attr.disconnect(destination=destinationAttr)


def poseToShelf():
    poseVals = getPoseVal()
    tmp = []
    tmp.append('import pymel.core as pm')
    for attr, val in poseVals:
        tmp.append('pm.setAttr("%s",%f)' % (attr, val))
    print '\n'.join(tmp)
    __addToShalf('\n'.join(tmp), label='pose')


def getPoseVal():
    attrs = __getCrvUI_keyAttrs()
    lib = []
    for attr in attrs:
        attr = pm.Attribute(attr)
        val = attr.get()
        lib.append([attr.name(), val])
    return lib


def __addToShalf(shelfCmd, label=''):
    '''
    update : 2015-04-28
    '''

    # 현재 쉐프탭 이름 알아옴.
    currentShelfTab = pm.shelfTabLayout(
        pm.melGlobals['gShelfTopLevel'], q=True, selectTab=True)

    # 생성
    pm.shelfButton(
        commandRepeatable=True,
        image1='commandButton.png',                    # 아이콘
        width=32,
        height=32,
        label=label,                         # 타이틀
        imageOverlayLabel=label,        # 라벨 (5글자 이하)
        font="smallPlainLabelFont",
        # "boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont", "plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont", "smallObliqueLabelFont", "fixedWidthFont", "smallFixedWidthFont".
        #overlayLabelColor     = (1, 1, .25),
        overlayLabelBackColor=(0, 0, 0, 0),  # (.15, .9, .1, .4),
        annotation=label,          # 참조글
        sourceType='python',
        command=shelfCmd,                # 명령어
        doubleClickCommand='',
        parent=currentShelfTab,
    )

def facsAttrList():
    facsAttrList = [
        'innerBrow_L_raiser_01',
        'innerBrow_L_lowerer',
        'outerBrow_L_raiser_02',
        'outerBrow_L_lowerer',
        'brow_L_lowerer_04',
        'eye_L_up_63',
        'eye_L_down_64',
        'eye_L_Left_61',
        'eye_L_Right_62',
        'upperLid_L_raiser_05',
        'upperLid_L_lowerer',
        'lowerLid_L_raiser',
        'lowerLid_L_lowerer',
        'lid_L_tighter_07',
        'nose_L_wrinkler_09',
        'nasolabial_L_deepener_11',
        'nostril_L_compressor_39',
        'nostril_L_dilator_38',
        'cheek_L_raiser_06',
        'upperLip_L_raiser_10',
        'lowerLip_L_depressor_16',
        'lips_up',
        'lips_down',
        'lips_left',
        'lips_right',
        'sharpLip_L_Puller_13',
        'lipCorner_L_depressor_15',
        'lip_L_pucker_18',
        'lip_L_stretcher_20',
        'lip_funnerler_22',
        'lip_tightener_23',
        'lip_pressor_24',
        'lip_suck_28',
        'lips_part_25',
        'cheek_L_puff_34',
        'cheek_L_suck_35',
        'dimpler_L_14',
        'jaw_clencher_31',
        'jaw_drop_26',
        'jaw_sideway_Left_30',
        'jaw_sideway_Right_30',
        'jaw_thrust_29',
        'chin_raiser_17',
        'neck_L_tightener_21'
        ]

ui()


