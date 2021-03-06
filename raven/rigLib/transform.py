# coding:utf-8
'''
Created on 2016. 11. 11.

@author: kyuho_choi
'''

import pymel.core as pm
import pymel.core.datatypes as dt

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
    

def snap( *objs, **kwargs):
    # 가변인수 처
    if objs:
        pm.select(objs)
    sel = pm.selected()
    if len(sel)<1:
        raise AttributeError(u"두개 이상의 오브젝트를 선택해주세요.")
        
    # 가변 키워드인수 처
    constType = kwargs.get('constType','parent')
    
    # PyNode 리캐스팅
    const = sel.pop(-1)
    target = sel
    
    # 롹 걸린 어트리뷰트 파악
    lockedAttrs = const.listAttr( locked=True )
    
    # 롹을 잠깐 풀고
    for attr in lockedAttrs:
        attr.unlock()
        
    # 위치 맞춘다음
    if constType=='parent':
        pm.delete( pm.parentConstraint( target, const) )
    elif constType=='point':
        pm.delete( pm.pointConstraint( target, const) )
    
    # 다시 롹
    for attr in lockedAttrs:
        attr.lock()


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
    lockAttrZro = kwargs.get('lockZroAttr',False) 

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
        # 그룹 생성
            
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
        
        # 리그 그룹 존재 유무 확인
        pm.parent( root, self.symmetryRig_grp() )
        
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

    def symmetryRig_grp(self):
        ''' 노드가 모이는 그룹 세팅 '''
        node = 'symmetryRig_grp'
        
        if pm.objExists(node):
            node = pm.PyNode( node )
        else:
            node = pm.group( n=node, em=True )
            
        return node

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


