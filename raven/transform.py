# coding:utf-8
'''
Created on 2016. 11. 11.

@author: kyuho_choi
'''

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

class SymmetryRig2(object):
    def __init__(self, inputNode=None, outputNode=None, orientNode=None, axis='x'):
        '''
        target, constraint, orient 순으로 선택
        
        '''
        self.create()
       
        if   axis == 'x':
            self.axis.set(1,0,0)
        elif axis == 'y':
            self.axis.set(0,1,0)
        elif axis == 'z':
            self.axis.set(0,0,1)            
        else:
            raise AttributeError(u"axis입력이 잘못됐습니다.")
        
        sel = ['','','']
        if inputNode:
            sel[0] = inputNode
            
        if outputNode:
            sel[1] = outputNode
            
        if orientNode:
            sel[3] = orientNode
            
        if sel:
            pm.select(sel)
            
        if sel[0]:
            self.setInput(sel[0])
            
        if sel[1]:
            self.setInput(sel[1])
        
        if sel[2]:
            self.setInput(sel[2])
        
    def create(self):        
        # 노드 생성
        root           = pm.group(n='root',           em=True)
        input          = pm.group(n='input',          em=True)  # @ReservedAssignment
        output         = pm.group(n='output',         em=True)
        orient         = pm.group(n='orient',         em=True)
        axisIn         = pm.group(n='axisIn',         em=True)
        axisCalc       = pm.group(n='axisCalc',       em=True)
        axisOut_Offset = pm.group(n='axisOut_offset', em=True)
        axisOut        = pm.group(n='axisOut',        em=True)
        const_grp      = pm.group(n='const_grp',      em=True)
       
        # 어트리뷰트 추가
        root.addAttr( 'axis', at='double3' )
        root.addAttr( 'axisX', at='double', parent='axis', keyable=True, dv=1, min=0, max=1 )
        root.addAttr( 'axisY', at='double', parent='axis', keyable=True, dv=0, min=0, max=1 )
        root.addAttr( 'axisZ', at='double', parent='axis', keyable=True, dv=0, min=0, max=1 )
        root.addAttr( 'matchOrient',     at='double', keyable=True, dv=1, min=0, max=1 )
        root.addAttr( 'showLocalAxis',   at='bool', keyable=True, dv=False )
        root.addAttr( 'inTranslate',  at='double3' )
        root.addAttr( 'inTranslateX', at='double', parent='inTranslate', keyable=True )
        root.addAttr( 'inTranslateY', at='double', parent='inTranslate', keyable=True )
        root.addAttr( 'inTranslateZ', at='double', parent='inTranslate', keyable=True )
        root.addAttr( 'inRotate', at='double3' )
        root.addAttr( 'inRotateX', at='double', parent='inRotate', keyable=True )
        root.addAttr( 'inRotateY', at='double', parent='inRotate', keyable=True )
        root.addAttr( 'inRotateZ', at='double', parent='inRotate', keyable=True )
        root.addAttr( 'inRotateOrder', attributeType='enum', enumName='xyz:yzx:zxy:xzy:yxz:zyx' )
        root.addAttr( 'inScale', at='double3' )
        root.addAttr( 'inScaleX', at='double', parent='inScale', keyable=True )
        root.addAttr( 'inScaleY', at='double', parent='inScale', keyable=True )
        root.addAttr( 'inScaleZ', at='double', parent='inScale', keyable=True )
        root.addAttr( 'outTranslate', at='double3' )
        root.addAttr( 'outTranslateX', at='double', parent='outTranslate', keyable=True )
        root.addAttr( 'outTranslateY', at='double', parent='outTranslate', keyable=True )
        root.addAttr( 'outTranslateZ', at='double', parent='outTranslate', keyable=True )
        root.addAttr( 'outRotate', at='double3' )
        root.addAttr( 'outRotateX', at='double', parent='outRotate', keyable=True )
        root.addAttr( 'outRotateY', at='double', parent='outRotate', keyable=True )
        root.addAttr( 'outRotateZ', at='double', parent='outRotate', keyable=True )
        root.addAttr( 'outRotateOrder', attributeType='enum', enumName='xyz:yzx:zxy:xzy:yxz:zyx' )
        root.addAttr( 'outScale', at='double3' )
        root.addAttr( 'outScaleX', at='double', parent='outScale', keyable=True )
        root.addAttr( 'outScaleY', at='double', parent='outScale', keyable=True )
        root.addAttr( 'outScaleZ', at='double', parent='outScale', keyable=True )
        root.setAttr( 'tx', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'ty', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'tz', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'rx', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'ry', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'rz', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'sx', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'sy', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'sz', keyable=False, lock=True, channelBox=False)
        root.setAttr(  'v', keyable=False, lock=True, channelBox=False)
        
        # Hiarachy
        pm.parent( axisOut_Offset, axisOut )
        pm.parent( axisOut, axisCalc )
        pm.parent( axisIn, axisCalc, const_grp, orient )
        pm.parent( input,output,orient, root)
        pm.parent( axisIn, axisCalc, const_grp )
        axisIn.t  >> axisOut.t
        axisIn.r  >> axisOut.r
        axisIn.s  >> axisOut.s
        axisIn.ro >> axisOut.ro
        
        # Constraint
        consts = []
        consts.append( pm.pointConstraint(input,axisIn) )
        consts.append( pm.orientConstraint(input,axisIn) )
        consts.append( pm.scaleConstraint(input,axisIn) )
        consts.append( pm.pointConstraint(axisOut,output) )
        consts.append( pm.scaleConstraint(axisOut,output) )
        ori = pm.orientConstraint(axisOut,axisOut_Offset, output)
        consts.append( ori )
        pm.parent( consts, const_grp )
        
        # matchOrient
        pm.setDrivenKeyframe( ori.axisOut_offsetW1, currentDriver='root.matchOrient', dv=1, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( ori.axisOutW0,        currentDriver='root.matchOrient', dv=1, v=  0, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( ori.axisOutW0,        currentDriver='root.matchOrient', dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( ori.axisOut_offsetW1, currentDriver='root.matchOrient', dv=0, v=  0, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleX,      currentDriver='root.axisX',       dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleX,      currentDriver='root.axisX',       dv=1, v= -1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisOut_Offset.rx,    currentDriver='root.axisX',       dv=0, v=  0, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisOut_Offset.rx,    currentDriver='root.axisX',       dv=1, v=180, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleY,      currentDriver='root.axisY',       dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleY,      currentDriver='root.axisY',       dv=1, v= -1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisOut_Offset.ry,    currentDriver='root.axisY',       dv=0, v=  0, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisOut_Offset.ry,    currentDriver='root.axisY',       dv=1, v=180, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleZ,      currentDriver='root.axisZ',       dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleZ,      currentDriver='root.axisZ',       dv=1, v= -1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisOut_Offset.rz,    currentDriver='root.axisZ',       dv=0, v=  0, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisOut_Offset.rz,    currentDriver='root.axisZ',       dv=1, v=180, inTangentType='linear', outTangentType='linear' )
        
        # input output
        root.inTranslate   >> input.t
        root.inRotate      >> input.r
        root.inScale       >> input.s
        root.inRotateOrder >> input.ro
        output.t  >> root.outTranslate
        output.r  >> root.outRotate
        output.s  >> root.outScale
        output.ro >> root.outRotateOrder
        
        root.showLocalAxis >> input.displayLocalAxis
        root.showLocalAxis >> output.displayLocalAxis
        root.showLocalAxis >> orient.displayLocalAxis
        #input.displayLocalAxis.set(True)
        #output.displayLocalAxis.set(True)
        #orient.displayLocalAxis.set(True)
        const_grp.hiddenInOutliner.set(True)
        
        # dv
        root.inTranslate.set(5,5,5)
        
        # 인스턴스 어트리뷰트 등록
        self.input  = input
        self.output = output
        self.orient = orient
        self.root   = root
        
        for item in root.listAttr( ud=True ):
            self.__setattr__( item.split('.')[-1], item )

    def setInput(self, transformNode ):
        inputNode = pm.PyNode(transformNode)
        inputNode.t  >> self.root.inTranslate
        inputNode.r  >> self.root.inRotate
        inputNode.s  >> self.root.inScale
        inputNode.ro >> self.root.inRotateOrder
        
    def setOutput(self, transformNode ):
        outputNode = pm.PyNode(transformNode)
        self.root.outTranslate   >> outputNode.t
        self.root.outRotate      >> outputNode.r
        self.root.outScale       >> outputNode.s
        self.root.outRotateOrder >> outputNode.ro
        
    def setOrient(self, transformNode):
        orientNode = pm.PyNode(transformNode)
        pm.parentConstraint( orientNode, self.orient )

class SymmetryRig(object):
    def __init__(self, *objs, **kwargs):
        '''
        target, constraint, orient 순으로 선택
        
        inputNode=None, 
        outputNode=None, 
        orientNode=None, 
        axis='x'
        
        '''
        # default
        inputNode = None
        outputNode = None
        orientNode = None
        axis='x'        
        
        # *objs
        if objs:
            pm.select(objs)
        sel = pm.selected()

        if sel[0]: inputNode  = sel[0]
        if sel[1]: outputNode = sel[1]
        if sel[2]: orientNode = sel[2]
        print "1.", inputNode, outputNode, orientNode, axis
        
        # **kwargs
        inputNode  = kwargs.get('inputNode',  inputNode)
        outputNode = kwargs.get('outputNode', outputNode)
        orientNode = kwargs.get('orientNode', orientNode)
        axis       = kwargs.get('axis',       axis)    
        print "2.", inputNode, outputNode, orientNode, axis

        self.create()
           
        if sel[0]: self.setInput(inputNode)
        if sel[1]: self.setOutput(outputNode)
        if sel[2]: self.setOrient(orientNode)
        if axis  : self.setAxis(axis)
        
    def create(self):        
        # 노드 생성
        root           = pm.group(n='root',           em=True)
        input          = pm.group(n='input',          em=True)  # @ReservedAssignment
        output         = pm.group(n='output',         em=True)
        orient         = pm.group(n='orient',         em=True)
        axisIn         = pm.group(n='axisIn',         em=True)
        axisCalc       = pm.group(n='axisCalc',       em=True)
        offset         = pm.group(n='offset', em=True)
        axisOut        = pm.group(n='axisOut',        em=True)
        const_grp      = pm.group(n='const_grp',      em=True)
       
        # 어트리뷰트 추가
        root.addAttr( 'axis', at='double3' )
        root.addAttr( 'axisX', at='double', parent='axis', keyable=True, dv=1, min=0, max=1 )
        root.addAttr( 'axisY', at='double', parent='axis', keyable=True, dv=0, min=0, max=1 )
        root.addAttr( 'axisZ', at='double', parent='axis', keyable=True, dv=0, min=0, max=1 )
        root.addAttr( 'rotateOffset', at='double3' )
        root.addAttr( 'rotateOffsetX', at='double', parent='rotateOffset', keyable=True )
        root.addAttr( 'rotateOffsetY', at='double', parent='rotateOffset', keyable=True )
        root.addAttr( 'rotateOffsetZ', at='double', parent='rotateOffset', keyable=True )      
        root.setAttr( 'tx', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'ty', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'tz', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'rx', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'ry', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'rz', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'sx', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'sy', keyable=False, lock=True, channelBox=False)
        root.setAttr( 'sz', keyable=False, lock=True, channelBox=False)
        root.setAttr(  'v', keyable=False, lock=True, channelBox=False)
        
        # Hiarachy
        pm.parent( offset, axisOut )
        pm.parent( axisOut, axisCalc )
        pm.parent( axisIn, axisCalc, const_grp, orient )
        pm.parent( input,output,orient, root)
        pm.parent( axisIn, axisCalc, const_grp )
        axisIn.t  >> axisOut.t
        axisIn.r  >> axisOut.r
        axisIn.s  >> axisOut.s
        axisIn.ro >> axisOut.ro        
        root.rotateOffset >> offset.r
        
        # Constraint
        consts = []
        consts.append( pm.pointConstraint(input,axisIn) )
        consts.append( pm.orientConstraint(input,axisIn) )
        consts.append( pm.scaleConstraint(input,axisIn) )
        consts.append( pm.pointConstraint(axisOut,output) )
        consts.append( pm.scaleConstraint(input,output) )
        ori = pm.orientConstraint(offset, output)
        ori.interpType.set(2) # shortest
        consts.append( ori )
        pm.parent( consts, const_grp )
        
        # matchOrient
        pm.setDrivenKeyframe( axisCalc.scaleX,      currentDriver='root.axisX',       dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleX,      currentDriver='root.axisX',       dv=1, v= -1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleY,      currentDriver='root.axisY',       dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleY,      currentDriver='root.axisY',       dv=1, v= -1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleZ,      currentDriver='root.axisZ',       dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleZ,      currentDriver='root.axisZ',       dv=1, v= -1, inTangentType='linear', outTangentType='linear' )

        # dv
        input.t.set(5,5,5)
        
        # 인스턴스 어트리뷰트 등록
        self.input  = input
        self.output = output
        self.orient = orient
        self.root   = root
        self.offset = offset
        self.__const_grp = const_grp
        
        # Display
        input.displayLocalAxis.set(True)
        output.displayLocalAxis.set(True)
        orient.displayLocalAxis.set(True)
        #const_grp.hiddenInOutliner.set(True)

    def setInput(self, transformNode ):
        ''' input 설정 '''
        const = pm.parentConstraint( transformNode, self.input )
        pm.parent( const, self.__const_grp )
        
    def setOutput(self, transformNode ):
        ''' output 설정 '''
        const = pm.parentConstraint( self.output, transformNode )
        pm.parent( const, self.__const_grp )
        
    def setOrient(self, transformNode):
        ''' orient 설정 '''
        const = pm.parentConstraint( transformNode, self.orient )
        pm.parent( const, self.__const_grp )
        
    def setAxis(self, axis):
        ''' Axis 설정 '''
        if   axis == 'x':
            self.root.axis.set(1,0,0)
            
        elif axis == 'y':
            self.root.axis.set(0,1,0)
            
        elif axis == 'z':
            self.root.axis.set(0,0,1) 
                       
        else:
            raise AttributeError(u"axis입력이 잘못됐습니다.")
        