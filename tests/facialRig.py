# coding:utf-8
import pymel.core as pm

def snap( *objs ):
    if objs:
        pm.select(objs)
    objs = pm.ls(sl=True, flatten=True)
    if not objs: return
    
    targets = objs[:-1]
    obj = objs[-1]
    
    print objs
    print targets, obj
    pm.delete( pm.parentConstraint( targets, obj) )

def createCrvShape( shapeName ):
    crvShape = None
    if shapeName=='circle':
        crvShape = pm.curve( d=3, p=[ (-0.5, 0.0, 0.0), (-0.5, 0.0, 0.130602), (-0.391806, 0.0, 0.391806), (0.0, 0.0, 0.554097), (0.391806, 0.0, 0.391806), (0.5, 0.0, 0.130602), (0.5, 0.0, 0.0), (0.5, 0.0, -0.130602), (0.391806, 0.0, -0.391806), (0.0, 0.0, -0.554097), (-0.391806, 0.0, -0.391806), (-0.5, 0.0, -0.130602), (-0.5, 0.0, 0.0) ], k=[ 2.0, 2.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.0, 10.0 ] )

    elif shapeName=='square':
        crvShape = pm.curve( d=1, p=[ (0.5, 0.0, 0.5), (-0.5, 0.0, 0.5), (-0.5, 0.0, -0.5), (0.5, 0.0, -0.5), (0.5, 0.0, 0.5) ], k=[ 0.0, 1.0, 2.0, 3.0, 4.0 ] )

    elif shapeName=='sphere':
        crvShape = pm.curve( d=3, p=[ (-0.5, 0.0, -0.0), (-0.5, 0.130602, -0.0), (-0.391806, 0.391806, -0.0), (-0.130602, 0.5, -0.0), (0.0, 0.5, -0.0), (0.0, 0.5, 0.130602), (0.0, 0.391806, 0.391806), (0.0, 0.130602, 0.5), (0.0, -0.0, 0.5), (0.130602, -0.0, 0.5), (0.391806, -0.0, 0.391806), (0.5, -0.0, 0.130602), (0.5, -0.0, 0.0), (0.5, 0.130602, -0.0), (0.391806, 0.391806, -0.0), (0.130602, 0.5, -0.0), (0.0, 0.5, -0.0), (0.0, 0.5, -0.130602), (0.0, 0.391806, -0.391806), (-0.0, 0.130602, -0.5), (-0.0, 0.0, -0.5), (0.130602, 0.0, -0.5), (0.391806, 0.0, -0.391806), (0.5, 0.0, -0.130602), (0.5, -0.0, 0.0), (0.5, -0.130602, 0.0), (0.391806, -0.391806, 0.0), (0.130602, -0.5, 0.0), (-0.0, -0.5, 0.0), (-0.130602, -0.5, 0.0), (-0.391806, -0.391806, 0.0), (-0.5, -0.130602, 0.0), (-0.5, 0.0, -0.0), (-0.5, 0.0, -0.130602), (-0.391806, 0.0, -0.391806), (-0.130602, 0.0, -0.5), (0.0, 0.0, -0.5), (-0.0, -0.130602, -0.5), (-0.0, -0.391806, -0.391806), (-0.0, -0.5, -0.130602), (-0.0, -0.5, -0.0), (-0.0, -0.5, 0.130602), (-0.0, -0.391806, 0.391806), (0.0, -0.130602, 0.5), (0.0, -0.0, 0.5), (-0.130602, -0.0, 0.5), (-0.391806, -0.0, 0.391806), (-0.5, -0.0, 0.130602), (-0.5, 0.0, -0.0) ], k=[ 8.0, 8.0, 8.0, 9.0, 10.0, 10.0, 10.0, 11.0, 12.0, 12.0, 12.0, 13.0, 14.0, 14.0, 14.0, 15.0, 16.0, 16.0, 16.0, 17.0, 18.0, 18.0, 18.0, 19.0, 20.0, 20.0, 20.0, 21.0, 22.0, 22.0, 22.0, 23.0, 24.0, 24.0, 24.0, 25.0, 26.0, 26.0, 26.0, 27.0, 28.0, 28.0, 28.0, 29.0, 30.0, 30.0, 30.0, 31.0, 32.0, 32.0, 32.0 ] )

    elif shapeName=='gear':
        transform = pm.createNode("transform", n="curve1")
        shapes = [ pm.createNode("nurbsCurve", p=transform), pm.createNode("nurbsCurve", p=transform)]
        pm.setAttr( shapes[0]+".cc", 1, 32, 0, False, 3, (0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0), 33, 33, (1.0011971810083387, 0.0, 0.11851736617223782), (1.001197189472047, 0.0, -0.11851736720873104), (0.7355889290488739, 0.0, -0.20071021702149838), (0.6620637126011513, 0.0, -0.3782159567885748), (0.7917582433205272, 0.0, -0.6241486124667979), (0.6241494196778841, 0.0, -0.7917576310894893), (0.37821666233952056, 0.0, -0.6620632132085538), (0.20071060140046026, 0.0, -0.7355887728914914), (0.1316864834477216, 0.0, -1.0011970883447325), (-0.13168545312161806, 0.0, -1.0011970618798471), (-0.2007098254073805, 0.0, -0.7355889461733963), (-0.3782160036196437, 0.0, -0.6620636425135036), (-0.6241485423791503, 0.0, -0.7917581964894583), (-0.791757490914194, 0.0, -0.6241493260157462), (-0.6620632600396227, 0.0, -0.378216592251873), (-0.7355888665536292, 0.0, -0.20071046122516512), (-1.0011971806904272, 0.0, -0.11851767009731831), (-1.0011971306947773, 0.0, 0.11851705165536117), (-0.7355889813761758, 0.0, 0.20070995395438632), (-0.662063610535708, 0.0, 0.3782161643828788), (-0.7917578867502331, 0.0, 0.6241485719267409), (-0.6241489520030181, 0.0, 0.7917575380631745), (-0.37821645207657784, 0.0, 0.6620633537017605), (-0.2007103150767695, 0.0, 0.7355888374829058), (-0.1185174830909543, 0.0, 1.0011972042649173), (0.11851726490485413, 0.0, 1.0011972098215534), (0.2007100914610428, 0.0, 0.7355888324796637), (0.37821627265985613, 0.0, 0.6620634674533404), (0.6241487941358845, 0.0, 0.7917577817777175), (0.7917577018129599, 0.0, 0.6241488586587918), (0.6620634005328294, 0.0, 0.37821638198893026), (0.7355888200404718, 0.0, 0.20071022738773214), (1.0011971810083387, 0.0, 0.11851736617223782), type="nurbsCurve" )
        pm.setAttr( shapes[1]+".cc", 3, 10, 0, False, 3, (2.0, 2.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 6.0, 7.0, 8.0, 9.0, 10.0, 10.0, 10.0), 15, 13, (-0.5, 0.0, 0.0), (-0.5, 0.0, 0.130602), (-0.391806, 0.0, 0.391806), (0.0, 0.0, 0.554097), (0.391806, 0.0, 0.391806), (0.5, 0.0, 0.130602), (0.5, 0.0, 0.0), (0.5, 0.0, -0.130602), (0.391806, 0.0, -0.391806), (0.0, 0.0, -0.554097), (-0.391806, 0.0, -0.391806), (-0.5, 0.0, -0.130602), (-0.5, 0.0, 0.0), type="nurbsCurve" )
        crvShape = transform

    return crvShape

def zeroGroup( objs=[], prefix='', suffix='_zro', translate=True, rotate=True, scale=False, lockAttrZro=False ):
    '''
    objs = transform nodes name
    prefix = prefix
    suffix = suffix
    translate = translate zero
    rotate = rotate zero
    scale = scale zero
    '''
    if objs:
        pm.select(objs)
    objs = pm.ls(sl=True, flatten=True)
    if not objs: return

    zeroGrps = []
    for obj in objs:
        obj = pm.PyNode(obj)

        grp = pm.group( n=prefix+obj+suffix, em=True)

        if translate : pm.delete( pm.pointConstraint(obj, grp) )
        if rotate    : pm.delete( pm.orientConstraint(obj, grp) )
        if scale     : pm.delete( pm.scaleConstraint(obj, grp) )

        parent = obj.getParent()
        if parent:
            grp.setParent(parent)

        if lockAttrZro:
            grp.t.lock()
            grp.r.lock()
            grp.s.lock()
            grp.v.lock()

        obj.setParent(grp)
        zeroGrps.append( grp )

    return zeroGrps

def negativeAttrRig( driverAttr=None, drivenAttr=None ):
    driverAttr = pm.Attribute(driverAttr)
    drivenAttr = pm.Attribute(drivenAttr)

    minus = pm.createNode('plusMinusAverage')
    minus.operation.set(2) # minus
    minus.input1D[0].set(1)

    driverAttr >> minus.input1D[1]
    minus.output1D >> drivenAttr

def createReverseTransform( prefix = '' ):   
    '''
    update : 2015-04-28
    '''
    origin  = pm.group(n='origin__parentMeToRivet_orientConstMeToLocalSpace',em=True)
    reverse = pm.group(n='reverse',em=True)
    anim    = pm.curve(n='anim__connectMeToCluster',d=3, p=[ (-0.5, 0.0, -0.0), (-0.5, 0.130602, -0.0), (-0.391806, 0.391806, -0.0), (-0.130602, 0.5, -0.0), (0.0, 0.5, -0.0), (0.0, 0.5, 0.130602), (0.0, 0.391806, 0.391806), (0.0, 0.130602, 0.5), (0.0, -0.0, 0.5), (0.130602, -0.0, 0.5), (0.391806, -0.0, 0.391806), (0.5, -0.0, 0.130602), (0.5, -0.0, 0.0), (0.5, 0.130602, -0.0), (0.391806, 0.391806, -0.0), (0.130602, 0.5, -0.0), (0.0, 0.5, -0.0), (0.0, 0.5, -0.130602), (0.0, 0.391806, -0.391806), (-0.0, 0.130602, -0.5), (-0.0, 0.0, -0.5), (0.130602, 0.0, -0.5), (0.391806, 0.0, -0.391806), (0.5, 0.0, -0.130602), (0.5, -0.0, 0.0), (0.5, -0.130602, 0.0), (0.391806, -0.391806, 0.0), (0.130602, -0.5, 0.0), (-0.0, -0.5, 0.0), (-0.130602, -0.5, 0.0), (-0.391806, -0.391806, 0.0), (-0.5, -0.130602, 0.0), (-0.5, 0.0, -0.0), (-0.5, 0.0, -0.130602), (-0.391806, 0.0, -0.391806), (-0.130602, 0.0, -0.5), (0.0, 0.0, -0.5), (-0.0, -0.130602, -0.5), (-0.0, -0.391806, -0.391806), (-0.0, -0.5, -0.130602), (-0.0, -0.5, -0.0), (-0.0, -0.5, 0.130602), (-0.0, -0.391806, 0.391806), (0.0, -0.130602, 0.5), (0.0, -0.0, 0.5), (-0.130602, -0.0, 0.5), (-0.391806, -0.0, 0.391806), (-0.5, -0.0, 0.130602), (-0.5, 0.0, -0.0) ], k=[ 8.0, 8.0, 8.0, 9.0, 10.0, 10.0, 10.0, 11.0, 12.0, 12.0, 12.0, 13.0, 14.0, 14.0, 14.0, 15.0, 16.0, 16.0, 16.0, 17.0, 18.0, 18.0, 18.0, 19.0, 20.0, 20.0, 20.0, 21.0, 22.0, 22.0, 22.0, 23.0, 24.0, 24.0, 24.0, 25.0, 26.0, 26.0, 26.0, 27.0, 28.0, 28.0, 28.0, 29.0, 30.0, 30.0, 30.0, 31.0, 32.0, 32.0, 32.0 ] )
    pm.parent(anim,reverse)
    pm.parent(reverse,origin)
    md = pm.createNode('multiplyDivide',n='reverse_md')
    md.input2.set(-1,-1,-1)
    anim.t >> md.input1
    md.output >> reverse.t
    
    if prefix:
        for node in [origin, reverse, anim, md]:
            node.rename( node.split('__')[0])
            node.rename( '%s_%s'%(prefix,node) )
            
    return [origin,reverse,anim]


# 컨스트레인 그룹
facialConst_grp = 'facialConst_grp'
if pm.objExists(facialConst_grp):
    facialConst_grp = pm.PyNode(facialConst_grp)
else:
    facialConst_grp = pm.group( n=facialConst_grp, em=True )

jnt = 'eyeBall_L'
ctrlName = 'eyeBall_L_anim'
scale = (0.03, 0.03, 0.03)
offset = (0.2,0,0)

jnt = 'eyeBall_R'
ctrlName = 'eyeBall_R_anim'
scale = (0.03, 0.03, 0.03)
offset = (0.2,0,0)

jnt = 'upperLid_L'
ctrlName = 'upperLid_L_anim'
scale = (0.03, 0.03, 0.03)
offset = (0.2,0,0)

jnt = 'upperLid_R'
ctrlName = 'upperLid_R_anim'
scale = (0.03, 0.03, 0.03)
offset = (0.2,0,0)

jnt = 'lowerLid_L'
ctrlName = 'lowerLid_L_anim'
scale = (0.03, 0.03, 0.03)
offset = (0.2,0,0)

jnt = 'lowerLid_R'
ctrlName = 'lowerLid_R_anim'
scale = (0.03, 0.03, 0.03)
offset = (0.2,0,0)

jnt = 'jaw'
ctrlName = 'jaw_anim'
scale = (0.03, 0.03, 0.03)
offset = (0,0,0)

jnt = 'neck'
ctrlName = 'neck_anim'
scale = (0.1, 0.1, 0.1)
offset = (0,0,0)

jnt = 'head'
ctrlName = 'head_anim'
scale = (0.1, 0.1, 0.1)
offset = (0,0,0)

jnt = 'upperTeeth'
ctrlName = 'upperTeeth_anim'
scale = (0.1, 0.1, 0.1)
offset = (0,0,0)

jnt = 'lowerTeeth'
ctrlName = 'lowerTeeth_anim'
scale = (0.1, 0.1, 0.1)
offset = (0,0,0)

# 컨트롤러 생성
anim = pm.curve( d=3, p=[ (-0.5, 0.0, -0.0), (-0.5, 0.130602, -0.0), (-0.391806, 0.391806, -0.0), (-0.130602, 0.5, -0.0), (0.0, 0.5, -0.0), (0.0, 0.5, 0.130602), (0.0, 0.391806, 0.391806), (0.0, 0.130602, 0.5), (0.0, -0.0, 0.5), (0.130602, -0.0, 0.5), (0.391806, -0.0, 0.391806), (0.5, -0.0, 0.130602), (0.5, -0.0, 0.0), (0.5, 0.130602, -0.0), (0.391806, 0.391806, -0.0), (0.130602, 0.5, -0.0), (0.0, 0.5, -0.0), (0.0, 0.5, -0.130602), (0.0, 0.391806, -0.391806), (-0.0, 0.130602, -0.5), (-0.0, 0.0, -0.5), (0.130602, 0.0, -0.5), (0.391806, 0.0, -0.391806), (0.5, 0.0, -0.130602), (0.5, -0.0, 0.0), (0.5, -0.130602, 0.0), (0.391806, -0.391806, 0.0), (0.130602, -0.5, 0.0), (-0.0, -0.5, 0.0), (-0.130602, -0.5, 0.0), (-0.391806, -0.391806, 0.0), (-0.5, -0.130602, 0.0), (-0.5, 0.0, -0.0), (-0.5, 0.0, -0.130602), (-0.391806, 0.0, -0.391806), (-0.130602, 0.0, -0.5), (0.0, 0.0, -0.5), (-0.0, -0.130602, -0.5), (-0.0, -0.391806, -0.391806), (-0.0, -0.5, -0.130602), (-0.0, -0.5, -0.0), (-0.0, -0.5, 0.130602), (-0.0, -0.391806, 0.391806), (0.0, -0.130602, 0.5), (0.0, -0.0, 0.5), (-0.130602, -0.0, 0.5), (-0.391806, -0.0, 0.391806), (-0.5, -0.0, 0.130602), (-0.5, 0.0, -0.0) ], k=[ 8.0, 8.0, 8.0, 9.0, 10.0, 10.0, 10.0, 11.0, 12.0, 12.0, 12.0, 13.0, 14.0, 14.0, 14.0, 15.0, 16.0, 16.0, 16.0, 17.0, 18.0, 18.0, 18.0, 19.0, 20.0, 20.0, 20.0, 21.0, 22.0, 22.0, 22.0, 23.0, 24.0, 24.0, 24.0, 25.0, 26.0, 26.0, 26.0, 27.0, 28.0, 28.0, 28.0, 29.0, 30.0, 30.0, 30.0, 31.0, 32.0, 32.0, 32.0 ] )

# 간단리깅!
anim.rename(ctrlName)
snap( jnt, anim )
zeroGroup( anim )

anim.s.set(scale)
pm.makeIdentity( t=1, r=1, s=1, n=1, apply=True )
pm.move( anim.cv, offset, r=True, os=True, wd=False)

const = pm.parentConstraint(anim,jnt)
pm.parent( const, facialConst_grp )

pm.select(anim)





eyeball_L_jnt = 'eyeball_L'
eyeball_R_jnt = 'eyeball_R'
lookAt_L_ctrlName = 'lookAt_L_anim'
lookAt_L_ctrlShape = 'circle'
lookAt_L_ctrlRotate = (0, 0, 90)
lookAt_L_ctrlScale = (0.1, 0.1, 0.1)
lookAt_L_ctrlShapeOffset = (0,0,0)
lookAt_R_ctrlName = 'lookAt_R_anim'
lookAt_R_ctrlShape = 'circle'
lookAt_R_ctrlRotate = (0, 0, 90)
lookAt_R_ctrlScale = (0.1, 0.1, 0.1)
lookAt_R_ctrlShapeOffset = (0,0,0)
lookAt_C_ctrlName = 'lookAt_C_anim'
lookAt_C_ctrlShape = 'square'
lookAt_C_ctrlRotate = (0, 0, 90)
lookAt_C_ctrlScale = (0.1, 0.1, 0.1)
lookAt_C_ctrlShapeOffset = (0,0,0)
LookAt_L_grpName = 'LookAt_L_grp'
LookAt_R_grpName = 'LookAt_R_grp'
LookAt_aimVec = (1,0,0)
LookAt_upVec = (0,1,0)
LookAt_L_upObj = 'eye_L_zro'
LookAt_R_upObj = 'eye_R_zro'

# 간단리깅!
lookAt_L_anim = createCrvShape( lookAt_L_ctrlShape )
lookAt_R_anim = createCrvShape( lookAt_R_ctrlShape )
lookAt_L_anim.rename( lookAt_L_ctrlName )
lookAt_R_anim.rename( lookAt_R_ctrlName )
snap( eyeball_L_jnt, lookAt_L_anim )
snap( eyeball_R_jnt, lookAt_R_anim )
lookAt_L_zro = zeroGroup( lookAt_L_anim )
lookAt_R_zro = zeroGroup( lookAt_R_anim )
lookAt_L_anim.r.set(lookAt_L_ctrlRotate)
lookAt_R_anim.r.set(lookAt_R_ctrlRotate)
lookAt_L_anim.s.set(lookAt_L_ctrlScale)
lookAt_R_anim.s.set(lookAt_R_ctrlScale)
pm.makeIdentity( lookAt_L_anim, t=1, r=1, s=1, n=1, apply=True )
pm.makeIdentity( lookAt_R_anim, t=1, r=1, s=1, n=1, apply=True )
lookAt_anim = createCrvShape( lookAt_C_ctrlShape )
lookAt_anim.rename( lookAt_C_ctrlName )
snap( eyeball_L_jnt, eyeball_R_jnt, lookAt_anim )
lookAt_zro = zeroGroup( lookAt_anim )
lookAt_anim.r.set(lookAt_R_ctrlRotate)
lookAt_anim.s.set(lookAt_C_ctrlScale)
pm.makeIdentity( lookAt_anim, t=1, r=1, s=1, n=1, apply=True )
pm.parent( lookAt_L_zro, lookAt_R_zro, lookAt_anim )
pm.select(lookAt_zro)

# Aim Rig
LookAt_L_grp = pm.group(n=LookAt_L_grpName, em=True)
LookAt_R_grp = pm.group(n=LookAt_R_grpName, em=True)
snap( eyeball_L_jnt, LookAt_L_grp )
snap( eyeball_R_jnt, LookAt_R_grp )
LookAt_L_aimConst = pm.aimConstraint( lookAt_L_anim, LookAt_L_grp, aim=LookAt_aimVec, u=LookAt_upVec, wut='objectrotation', wuo=LookAt_L_upObj )
LookAt_R_aimConst = pm.aimConstraint( lookAt_R_anim, LookAt_R_grp, aim=LookAt_aimVec, u=LookAt_upVec, wut='objectrotation', wuo=LookAt_R_upObj )

# Auto Follow Rig
eye_L_zro = 'eye_L_zro'
eye_R_zro = 'eye_R_zro'
eyeball_L_anim = 'eyeball_L_anim'
eyeball_R_anim = 'eyeball_R_anim'
upperLid_L_autoEyeFollow_grpName = 'upperLid_L_autoEyeFollow_grp'
upperLid_R_autoEyeFollow_grpName = 'upperLid_R_autoEyeFollow_grp'
lowerLid_L_autoEyeFollow_grpName = 'lowerLid_L_autoEyeFollow_grp'
lowerLid_R_autoEyeFollow_grpName = 'lowerLid_R_autoEyeFollow_grp'

upperLid_L_autoEyeFollow_grp = pm.group(n=upperLid_L_autoEyeFollow_grpName, em=True)
upperLid_R_autoEyeFollow_grp = pm.group(n=upperLid_R_autoEyeFollow_grpName, em=True)
lowerLid_L_autoEyeFollow_grp = pm.group(n=lowerLid_L_autoEyeFollow_grpName, em=True)
lowerLid_R_autoEyeFollow_grp = pm.group(n=lowerLid_R_autoEyeFollow_grpName, em=True)
snap( eyeball_L_jnt, upperLid_L_autoEyeFollow_grp )
snap( eyeball_R_jnt, upperLid_R_autoEyeFollow_grp )
snap( eyeball_L_jnt, lowerLid_L_autoEyeFollow_grp )
snap( eyeball_R_jnt, lowerLid_R_autoEyeFollow_grp )

upperLid_L_autoEyeFollow_oriConst = pm.orientConstraint( eye_L_zro, eyeball_L_anim, upperLid_L_autoEyeFollow_grp, skip=("x","y"))
upperLid_R_autoEyeFollow_oriConst = pm.orientConstraint( eye_R_zro, eyeball_R_anim, upperLid_R_autoEyeFollow_grp, skip=("x","y"))
lowerLid_L_autoEyeFollow_oriConst = pm.orientConstraint( eye_L_zro, eyeball_L_anim, lowerLid_L_autoEyeFollow_grp, skip=("x","y"))
lowerLid_R_autoEyeFollow_oriConst = pm.orientConstraint( eye_R_zro, eyeball_R_anim, lowerLid_R_autoEyeFollow_grp, skip=("x","y"))

upperLid_L_weightAttrs = upperLid_L_autoEyeFollow_oriConst.getWeightAliasList()
upperLid_R_weightAttrs = upperLid_R_autoEyeFollow_oriConst.getWeightAliasList()
lowerLid_L_weightAttrs = lowerLid_L_autoEyeFollow_oriConst.getWeightAliasList()
lowerLid_R_weightAttrs = lowerLid_R_autoEyeFollow_oriConst.getWeightAliasList()
negativeAttrRig(upperLid_L_weightAttrs[1],upperLid_L_weightAttrs[0])
negativeAttrRig(upperLid_R_weightAttrs[1],upperLid_R_weightAttrs[0])
negativeAttrRig(lowerLid_L_weightAttrs[1],lowerLid_L_weightAttrs[0])
negativeAttrRig(lowerLid_R_weightAttrs[1],lowerLid_R_weightAttrs[0])

#lid_autoEyeFollow_ctrl = createCrvShape( 'gear' )
lid_autoEyeFollow_ctrl = pm.PyNode('lookAt_C_anim')
lid_autoEyeFollow_ctrl.addAttr('upperLid_autoEyeFollow_L', dv=.9, keyable=True, min=0, max=1)
lid_autoEyeFollow_ctrl.addAttr('upperLid_autoEyeFollow_R', dv=.9, keyable=True, min=0, max=1)
lid_autoEyeFollow_ctrl.addAttr('lowerLid_autoEyeFollow_L', dv=.5, keyable=True, min=0, max=1)
lid_autoEyeFollow_ctrl.addAttr('lowerLid_autoEyeFollow_R', dv=.5, keyable=True, min=0, max=1)
lid_autoEyeFollow_ctrl.upperLid_autoEyeFollow_L >> upperLid_L_weightAttrs[1]
lid_autoEyeFollow_ctrl.upperLid_autoEyeFollow_R >> upperLid_R_weightAttrs[1]
lid_autoEyeFollow_ctrl.lowerLid_autoEyeFollow_L >> lowerLid_L_weightAttrs[1]
lid_autoEyeFollow_ctrl.lowerLid_autoEyeFollow_R >> lowerLid_R_weightAttrs[1]

pm.parent(upperLid_L_autoEyeFollow_grp, eye_L_zro)
pm.parent(upperLid_R_autoEyeFollow_grp, eye_R_zro)
pm.parent(lowerLid_L_autoEyeFollow_grp, eye_L_zro)
pm.parent(lowerLid_R_autoEyeFollow_grp, eye_R_zro)

#
# Auto Eye Close Rig
#

# 필요노드 등록
eye_L_zro = 'eye_L_zro'
eye_R_zro = 'eye_R_zro'
upperLid_L_anim = 'upperLid_L_anim'
lowerLid_L_anim = 'lowerLid_L_anim'
upperLid_R_anim = 'upperLid_R_anim'
lowerLid_R_anim = 'lowerLid_R_anim'

# 노드 생성
upperLid_L_autoEyeClose_openTgt = pm.spaceLocator( n='upperLid_L_autoEyeClose_openTgt' )
upperLid_R_autoEyeClose_openTgt = pm.spaceLocator( n='upperLid_R_autoEyeClose_openTgt' )
lowerLid_L_autoEyeClose_openTgt = pm.spaceLocator( n='lowerLid_L_autoEyeClose_openTgt' )
lowerLid_R_autoEyeClose_openTgt = pm.spaceLocator( n='lowerLid_R_autoEyeClose_openTgt' )
upperLid_L_autoEyeClose_closeTgt = pm.spaceLocator( n='upperLid_L_autoEyeClose_closeTgt' )
upperLid_R_autoEyeClose_closeTgt = pm.spaceLocator( n='upperLid_R_autoEyeClose_closeTgt' )
lowerLid_L_autoEyeClose_closeTgt = pm.spaceLocator( n='lowerLid_L_autoEyeClose_closeTgt' )
lowerLid_R_autoEyeClose_closeTgt = pm.spaceLocator( n='lowerLid_R_autoEyeClose_closeTgt' )
upperLid_L_autoEyeClose_grp = pm.group(n='upperLid_L_autoEyeClose_grp', em=True)
upperLid_R_autoEyeClose_grp = pm.group(n='upperLid_R_autoEyeClose_grp', em=True)
lowerLid_L_autoEyeClose_grp = pm.group(n='lowerLid_L_autoEyeClose_grp', em=True)
lowerLid_R_autoEyeClose_grp = pm.group(n='lowerLid_R_autoEyeClose_grp', em=True)

# 어트리뷰트 추가
upperLid_L_autoEyeClose_grp.addAttr('close', min=0, max=1, keyable=True)
upperLid_R_autoEyeClose_grp.addAttr('close', min=0, max=1, keyable=True)
lowerLid_L_autoEyeClose_grp.addAttr('close', min=0, max=1, keyable=True)
lowerLid_R_autoEyeClose_grp.addAttr('close', min=0, max=1, keyable=True)
upperLid_L_autoEyeClose_grp.addAttr('closeValue', keyable=True)
upperLid_R_autoEyeClose_grp.addAttr('closeValue', keyable=True)
lowerLid_L_autoEyeClose_grp.addAttr('closeValue', keyable=True)
lowerLid_R_autoEyeClose_grp.addAttr('closeValue', keyable=True)
upperLid_L_autoEyeClose_grp.closeValue.set(-20)
upperLid_R_autoEyeClose_grp.closeValue.set(-20)
lowerLid_L_autoEyeClose_grp.closeValue.set(-20)
lowerLid_R_autoEyeClose_grp.closeValue.set(-20)

# 히아라키조정
pm.parent( upperLid_L_autoEyeClose_closeTgt, eye_L_zro, r=True )
pm.parent( lowerLid_L_autoEyeClose_closeTgt, eye_L_zro, r=True )
pm.parent( upperLid_R_autoEyeClose_closeTgt, eye_R_zro, r=True )
pm.parent( lowerLid_R_autoEyeClose_closeTgt, eye_R_zro, r=True )
pm.parent( upperLid_L_autoEyeClose_openTgt, upperLid_L_anim, r=True )
pm.parent( lowerLid_L_autoEyeClose_openTgt, lowerLid_L_anim, r=True )
pm.parent( upperLid_R_autoEyeClose_openTgt, upperLid_R_anim, r=True )
pm.parent( lowerLid_R_autoEyeClose_openTgt, lowerLid_R_anim, r=True )
pm.parent( upperLid_L_autoEyeClose_grp, upperLid_L_anim, r=True )
pm.parent( lowerLid_L_autoEyeClose_grp, lowerLid_L_anim, r=True )
pm.parent( upperLid_R_autoEyeClose_grp, upperLid_R_anim, r=True )
pm.parent( lowerLid_R_autoEyeClose_grp, lowerLid_R_anim, r=True )

# 컨스트레인
upperLid_L_autoEyeClose_oriConst = pm.orientConstraint( upperLid_L_autoEyeClose_openTgt, upperLid_L_autoEyeClose_closeTgt, upperLid_L_autoEyeClose_grp, skip=("x","y"))
lowerLid_L_autoEyeClose_oriConst = pm.orientConstraint( lowerLid_L_autoEyeClose_openTgt, lowerLid_L_autoEyeClose_closeTgt, lowerLid_L_autoEyeClose_grp, skip=("x","y"))
upperLid_R_autoEyeClose_oriConst = pm.orientConstraint( upperLid_R_autoEyeClose_openTgt, upperLid_R_autoEyeClose_closeTgt, upperLid_R_autoEyeClose_grp, skip=("x","y"))
lowerLid_R_autoEyeClose_oriConst = pm.orientConstraint( lowerLid_R_autoEyeClose_openTgt, lowerLid_R_autoEyeClose_closeTgt, lowerLid_R_autoEyeClose_grp, skip=("x","y"))

upperLid_L_weightAttrs = upperLid_L_autoEyeClose_oriConst.getWeightAliasList()
lowerLid_L_weightAttrs = lowerLid_L_autoEyeClose_oriConst.getWeightAliasList()
upperLid_R_weightAttrs = upperLid_R_autoEyeClose_oriConst.getWeightAliasList()
lowerLid_R_weightAttrs = lowerLid_R_autoEyeClose_oriConst.getWeightAliasList()
negativeAttrRig(upperLid_L_weightAttrs[1],upperLid_L_weightAttrs[0])
negativeAttrRig(lowerLid_L_weightAttrs[1],lowerLid_L_weightAttrs[0])
negativeAttrRig(upperLid_R_weightAttrs[1],upperLid_R_weightAttrs[0])
negativeAttrRig(lowerLid_R_weightAttrs[1],lowerLid_R_weightAttrs[0])
upperLid_L_autoEyeClose_grp.close >> upperLid_L_weightAttrs[1]
lowerLid_L_autoEyeClose_grp.close >> lowerLid_L_weightAttrs[1]
upperLid_R_autoEyeClose_grp.close >> upperLid_R_weightAttrs[1]
lowerLid_R_autoEyeClose_grp.close >> lowerLid_R_weightAttrs[1]

upperLid_L_autoEyeClose_grp.closeValue >> upperLid_L_autoEyeClose_closeTgt.rz
lowerLid_L_autoEyeClose_grp.closeValue >> lowerLid_L_autoEyeClose_closeTgt.rz
upperLid_R_autoEyeClose_grp.closeValue >> upperLid_R_autoEyeClose_closeTgt.rz
lowerLid_R_autoEyeClose_grp.closeValue >> lowerLid_R_autoEyeClose_closeTgt.rz

upperLid_L_jntConst = pm.group(n='upperLid_L_jntConst', em=True)
upperLid_R_jntConst = pm.group(n='upperLid_R_jntConst', em=True)
lowerLid_L_jntConst = pm.group(n='lowerLid_L_jntConst', em=True)
lowerLid_R_jntConst = pm.group(n='lowerLid_R_jntConst', em=True)
pm.parent( upperLid_L_jntConst, upperLid_L_autoEyeClose_grp, r=True )
pm.parent( upperLid_R_jntConst, upperLid_R_autoEyeClose_grp, r=True )
pm.parent( lowerLid_L_jntConst, lowerLid_L_autoEyeClose_grp, r=True )
pm.parent( lowerLid_R_jntConst, lowerLid_R_autoEyeClose_grp, r=True )

pm.parentConstraint( upperLid_L_jntConst, 'upperLid_L' )
pm.parentConstraint( lowerLid_L_jntConst, 'lowerLid_L' )
pm.parentConstraint( upperLid_R_jntConst, 'upperLid_R' )
pm.parentConstraint( lowerLid_R_jntConst, 'lowerLid_R' )

# UI와 연결
pm.Attribute('eye_closed_L_ctrl.eyes_closed_43_L') >> upperLid_L_autoEyeClose_grp.close
pm.Attribute('eye_closed_L_ctrl.eyes_closed_43_L') >> lowerLid_L_autoEyeClose_grp.close
pm.Attribute('eye_colsed_R_ctrl.eyes_closed_43_R') >> upperLid_R_autoEyeClose_grp.close
pm.Attribute('eye_colsed_R_ctrl.eyes_closed_43_R') >> lowerLid_R_autoEyeClose_grp.close
