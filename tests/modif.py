import pymel.core as pm
import raven.jointBaseRig as rig
reload(rig)

#===============================================================================
# 
#  file 오픈, 수정 저장
#
#===============================================================================
eye = rig.Eye()
eye.open_jntFile()
eye.open_layFile()
eye.save_jntFile()
eye.save_layFile()

head = rig.Head()
head.open_jntFile()
head.open_layFile()
head.save_jntFile()
head.save_layFile()

jaw = rig.Jaw()
jaw.open_jntFile()
jaw.save_jntFile()
jaw.open_layFile()
jaw.save_layFile()

#===============================================================================
# 
# 선택리스트 출력
#
#===============================================================================
trans = pm.ls(sl=True, type='transform', o=True)
const = pm.ls(sl=True, type='constraint')
loc = [loc.getParent() for loc in pm.ls(sl=True, type='locator', dag=True)]
result = list(set(trans)-set(const)-set(loc))
pm.select(result)

sel = pm.ls(sl=True)
varStr = []
varStr.append('"NodeList":[')
for node in sel:
    varStr.append('"%s",'%node)
varStr.append(']')
print ' '.join(varStr)



#zeroGroup(lock=False)
#snap(type='parent')
#rigCurveConnect()
#rigCurveConnect(delete=True)

# 조인트 오리엔트 연결
sel = pm.selected()
jo, jnt = sel[0], sel[1]
jo.r >> jnt.jo

# 조인트 타입 설정
sel = pm.selected()
for node in sel:
    node.typ.set(18)
    typeName = node.name().split('__SIDE__')[0]
    node.otherType.set(typeName)

# 아웃라이너 붉게
sel = pm.selected()
for node in sel:
    pm.setAttr( node.useOutlinerColor, True )
    pm.setAttr( node.outlinerColor, 1,0,0 )

# 아웃라이너 노랑    
sel = pm.selected()
for node in sel:
    pm.setAttr( node.useOutlinerColor, True )
    pm.setAttr( node.outlinerColor, 1,1,0 )

# 아웃라이너 중간노랑    
sel = pm.selected()
for node in sel:
    pm.setAttr( node.useOutlinerColor, True )
    pm.setAttr( node.outlinerColor, .5,.5,0 )

# 회색    
sel = pm.selected()
for node in sel:
    col = .5
    pm.setAttr( node.useOutlinerColor, True )    
    pm.setAttr( node.outlinerColor, col,col,col )

# 아웃라이너 컬러 리셋
sel = pm.selected()
for node in sel:
    pm.setAttr( node.useOutlinerColor, False )
    pm.setAttr( node.outlinerColor, 0,0,0 )
    
    
sym = pm.createNode('symmetryConstraint')