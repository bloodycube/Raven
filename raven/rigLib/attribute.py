'''
Created on 2016. 11. 14.

@author: kyuho_choi
'''
import pymel.core as pm

def getAttrsFromChannelbox():
    '''
    채널박스에서 선택된 어트리뷰트 이름 리턴
    블렌드 쉐입은 잘 안됨..ㅠㅠㅠ
    @return: 어트리뷰트 리스트 리턴
    '''
    mainObjs     = pm.channelBox( pm.melGlobals['gChannelBoxName'], q=True, mainObjectList=True )
    mainAttrs    = pm.channelBox( pm.melGlobals['gChannelBoxName'], q=True, selectedMainAttributes=True )
    shapeObjs    = pm.channelBox( pm.melGlobals['gChannelBoxName'], q=True, shapeObjectList =True)
    shapeAttrs   = pm.channelBox( pm.melGlobals['gChannelBoxName'], q=True, selectedShapeAttributes=True)
    histObjs     = pm.channelBox( pm.melGlobals['gChannelBoxName'], q=True, historyObjectList =True)
    histAttrs    = pm.channelBox( pm.melGlobals['gChannelBoxName'], q=True, selectedHistoryAttributes=True)
    outputObjs   = pm.channelBox( pm.melGlobals['gChannelBoxName'], q=True, outputObjectList =True)
    outputAttrs  = pm.channelBox( pm.melGlobals['gChannelBoxName'], q=True, selectedOutputAttributes=True)

    # 짧은 이름
    shortNames = []
    for pair in ((mainObjs, mainAttrs), (shapeObjs, shapeAttrs), (histObjs, histAttrs), (outputObjs, outputAttrs)):
        objs, attrs = pair
        #print pair
        if attrs:
            for obj in objs:
                for attr in attrs:
                    shortNames.append('%s.%s' %(obj,attr) )


    # 긴이름
    longNames = []
    for pair in ((mainObjs, mainAttrs), (shapeObjs, shapeAttrs), (histObjs, histAttrs), (outputObjs, outputAttrs)):
        objs, attrs = pair
        #print pair
        if attrs is not None:
            for node in objs:
                result = [ objs[0] +'.' + pm.attributeQuery( attr, n=node, ln=True) for attr in attrs ]
                longNames.extend( result )

    longNames = list(set(longNames))
    
    return shortNames

def reversAttrRig( driverAttr=None, drivenAttr=None ):
    ''' Attribute Reverse Rig '''
    if not driverAttr and not drivenAttr:
        driverAttr,drivenAttr = getAttrsFromChannelbox()
        
    if not driverAttr and not drivenAttr:
        raise AttributeError (u"")
        
    driverAttr = pm.PyNode( driverAttr )
    drivenAttr = pm.PyNode( drivenAttr )
    pm.setDrivenKeyframe( drivenAttr, currentDriver=driverAttr, dv=0, v= 1, inTangentType='linear', outTangentType='linear' )
    pm.setDrivenKeyframe( drivenAttr, currentDriver=driverAttr, dv=1, v= 0, inTangentType='linear', outTangentType='linear' )