# coding:utf-8
'''
Created on 2016. 11. 20.

@author: kyuho_choi
'''
import os
import pymel.core as pm

def resetMesh(mesh=None):
    # 입력이 있으면 입력된 노드를 선택
    if mesh:
        pm.select(mesh)
        
    # 입력이 없어도 선택된 오브젝트로 입력 대체
    sel = pm.selected( o=True )
    
    # 입력값이 없으면 에러
    if not sel:
        raise

    # obj플러그인 로드
    if not pm.pluginInfo('objExport', q=True, loaded=True):
        pm.loadPlugin('objExport')

    # obj임시 저장 위치
    tmpfile = os.path.expanduser('~') + "/tmpObj.obj"

    # obj Export
    pm.select(mesh)
    pm.exportSelected( tmpfile, typ="OBJexport", options="groups=0;ptgroups=0;materials=0;smoothing=0;normals=0", f=True)

    # obj Import
    newMesh, newMeshShape = pm.importFile(tmpfile, rnn=True)  # @UnusedVariable

    # 임시저장 파일 삭제
    os.remove( tmpfile )
    
    pm.select(newMesh)
