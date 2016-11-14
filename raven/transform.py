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


class SymmetryRig(object):
    def __init__(self, *objs, **kwargs):
        '''
        target, constraint, orient 순으로 선택
        
        inputNode=None, 
        outputNode=None, 
        orientNode=None, 
        axis='x'
        offset = (0,0,0)
        '''
        # default
        inputNode = None
        outputNode = None
        orientNode = None
        axis='x'
        offset=(0,0,0)        
        
        # *objs
        if objs:
            pm.select(objs)
        sel = pm.selected()

        if len(sel)>0: inputNode  = sel[0]
        if len(sel)>1: outputNode = sel[1]
        if len(sel)>2: orientNode = sel[2]
        
        # **kwargs
        self.inputNode  = kwargs.get('inputNode',  inputNode)
        self.outputNode = kwargs.get('outputNode', outputNode)
        self.orientNode = kwargs.get('orientNode', orientNode)
        self.axis       = kwargs.get('axis',       axis)
        self.offset     = kwargs.get('offset',     offset)

        # Rig 생성
        self.create()
           
        # 입력값 처리
        if self.inputNode  : self.setInput()
        if self.outputNode : self.setOutput()
        if self.orientNode : self.setOrient()
        if self.axis       : self.setAxis()
        if self.offset     : self.setOffset()
        
    def create(self):        
        # 노드 생성
        root           = pm.group(n='root',      em=True)
        input          = pm.group(n='input',     em=True)  # @ReservedAssignment
        output         = pm.group(n='output',    em=True)
        orient         = pm.group(n='orient',    em=True)
        axisIn         = pm.group(n='axisIn',    em=True)
        axisCalc       = pm.group(n='axisCalc',  em=True)
        offset         = pm.group(n='offset',    em=True)
        axisOut        = pm.group(n='axisOut',   em=True)
        const_grp      = pm.group(n='const_grp', em=True)
       
        # 어트리뷰트 추가
        root.addAttr( 'axis', at='double3' )
        root.addAttr( 'axisX', at='double', parent='axis', keyable=True, dv=1, min=0, max=1 )
        root.addAttr( 'axisY', at='double', parent='axis', keyable=True, dv=0, min=0, max=1 )
        root.addAttr( 'axisZ', at='double', parent='axis', keyable=True, dv=0, min=0, max=1 )
        root.addAttr( 'rotateOffset', at='double3' )
        root.addAttr( 'rotateOffsetX', at='double', parent='rotateOffset', keyable=True )
        root.addAttr( 'rotateOffsetY', at='double', parent='rotateOffset', keyable=True )
        root.addAttr( 'rotateOffsetZ', at='double', parent='rotateOffset', keyable=True )  
        
        root.addAttr( 'inputNode',  at='message' )
        root.addAttr( 'outputNode', at='message' )
        root.addAttr( 'orientNode', at='message' )
        root.addAttr( 'constrinatFor_input',  at='message', multi=True, indexMatters=False )
        root.addAttr( 'constrinatFor_output', at='message', multi=True, indexMatters=False )
        root.addAttr( 'constrinatFor_orient', at='message', multi=True, indexMatters=False )
            
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
        
        # SDK
        pm.setDrivenKeyframe( axisCalc.scaleX, currentDriver='root.axisX', dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleX, currentDriver='root.axisX', dv=1, v= -1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleY, currentDriver='root.axisY', dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleY, currentDriver='root.axisY', dv=1, v= -1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleZ, currentDriver='root.axisZ', dv=0, v=  1, inTangentType='linear', outTangentType='linear' )
        pm.setDrivenKeyframe( axisCalc.scaleZ, currentDriver='root.axisZ', dv=1, v= -1, inTangentType='linear', outTangentType='linear' )

        # dv
        input.t.set(5,5,5)
        
        # 인스턴스 어트리뷰트 등록
        self.input  = input
        self.output = output
        self.orient = orient
        self.root   = root
        self.__const_grp = const_grp
        
        # Display
        #input.displayLocalAxis.set(True)
        #output.displayLocalAxis.set(True)
        #orient.displayLocalAxis.set(True)
        const_grp.hiddenInOutliner.set(True)

    def setInput(self, transformNode=None ):
        ''' input 설정 '''
        if transformNode:
            self.inputNode = transformNode

        # 이미 연결된 컨스트레인이 있으면 컨스트레인 삭제
        consts = self.root.constrinatFor_input.get()
        if consts:
            pm.delete( consts )
 
        # 컨스트레인
        parenConst = pm.parentConstraint( self.inputNode, self.input )
        parenConst.enableRestPosition.set(0) # inputNode가 삭제 됐을때 input이 restPosition으로 돌아가지 않도록 세팅
        scaleConst = pm.scaleConstraint( self.inputNode, self.input )
        scaleConst.enableRestPosition.set(0)
        consts = [parenConst,scaleConst]
        
        # 메세지 노드로 root에 연결
        self.inputNode.message >> self.root.inputNode
        for const in consts: 
            pm.connectAttr( const.message, self.root.constrinatFor_input, nextAvailable=True  )
        
        # 컨스트레인을 const_grp에 페어런트
        pm.parent( consts, self.__const_grp )
        
        # rootNode 이름 변경
        self.__setRename()
        
        # 노드 선택
        pm.select(self.inputNode)
        
    def setOutput(self, transformNode=None ):
        ''' output 설정 '''
        if transformNode:
            self.outputNode = transformNode
            
        # 이미 연결된 컨스트레인이 있으면 컨스트레인 삭제
        consts = self.root.constrinatFor_output.get()
        if consts:
            pm.delete( consts )

        # 잠긴 어트리뷰트 파악
        lockedAttr = self.outputNode.listAttr( locked=True )

        skipTr = []
        skipRt = []
        skipSc = []
        for attr in ['tx','ty','tz','rx','ry','rz','sx','sy','sz']:
            if self.outputNode.attr(attr) in lockedAttr:
                if   attr[0] == 't':
                    skipTr.append( attr[-1] )
                elif attr[0] == 'r':
                    skipRt.append( attr[-1] )
                elif attr[0] == 's':
                    skipSc.append( attr[-1] )
        
        # 컨스트레인
        parenConst = pm.parentConstraint( self.output, self.outputNode, skipTranslate=skipTr, skipRotate=skipRt )
        scaleConst = pm.scaleConstraint(  self.output, self.outputNode, skip=skipSc )
        consts = [parenConst,scaleConst]
        
        # inputNode가 삭제 됐을때 input이 restPosition으로 돌아가지 않도록 세팅
        for const in consts:
            const.enableRestPosition.set(0)
        
        # 메세지 노드로 root에 연결 (삭제용)
        self.outputNode.message >> self.root.outputNode
        for const in consts: 
            pm.connectAttr( const.message, self.root.constrinatFor_output, nextAvailable=True  )
        
        # 컨스트레인을 const_grp에 페어런트
        pm.parent( consts, self.__const_grp )

        # rootNode 이름 변경
        self.__setRename()
        
        # 노드 선택
        pm.select(self.outputNode)
        
    def setOrient(self, transformNode=None ):
        ''' orient 설정 '''
        # 입력이 있으면 orientNode로 등록
        if transformNode:
            self.orientNode = transformNode
        
        # 이미 연결된 컨스트레인이 있으면 컨스트레인 삭제
        const = self.root.constrinatFor_orient.get()
        if const:
            pm.delete( const )
        
        # 컨스트레인
        const = pm.parentConstraint( self.orientNode, self.orient ) 
        
        # inputNode가 삭제 됐을때 input이 restPosition으로 돌아가지 않도록 세팅
        const.enableRestPosition.set(0)
        
        # 메세지 노드로 root에 연결 (삭제용)
        const.message >> self.root.constrinatFor_orient
        
        # 컨스트레인을 const_grp에 페어런트
        pm.parent( const, self.__const_grp ) 

        # rootNode 이름 변경
        self.__setRename()
        
        pm.select(self.orientNode)
        
    def setAxis(self, axis='' ):
        ''' Axis 설정 '''
        if axis:
            self.axis = axis
            
        if   self.axis == 'x':
            self.root.axis.set(1,0,0)
            self.setOffset( 180,0,0 )
            
        elif self.axis == 'y':
            self.root.axis.set(0,1,0)
            self.setOffset( 0,180,0 )
            
        elif self.axis == 'z':
            self.root.axis.set(0,0,1)
            self.setOffset( 0,0,180 )
                       
        else:
            raise AttributeError(u"axis입력이 잘못됐습니다.")
    
        # rootNode 이름 변경
        self.__setRename()
    
    def setOffset(self, *offset ):
        ''' offset 세팅 '''
        if offset:
            if not len(offset)==3:
                raise AttributeError (u'입력이 잘못되었습니다. .setOffset( 180,0,0 ) 형식으로 입력 하세요.')
            self.offset = offset
            
        self.root.rotateOffset.set( self.offset )
 
    def __setRename(self):
        ''' root노드 이름 변경 '''
        newName = 'symmetryRig__TARGET__CONSTRAINT__ORIENT__AXIS'
        
        if self.inputNode : 
            newName = newName.replace('TARGET',     self.inputNode.name().replace('_','') )
            
        if self.outputNode : 
            newName = newName.replace('CONSTRAINT', self.outputNode.name().replace('_','') )
            
        if self.orientNode: 
            newName = newName.replace('ORIENT',     self.orientNode.name().replace('_','') )
            
        if self.axis: 
            newName = newName.replace('AXIS',       self.axis )
        
        # 이름 변경
        self.root.rename(newName)
        
        
        
        
        
        