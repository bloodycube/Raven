'''
Created on 2016. 10. 11.

@author: kyuho_choi
'''

import pymel.core as pm

def getShapeEditorTreeviewSelection( scope ):
    '''
    mel:
        C:/Program Files/Autodesk/Maya2017/scripts/others/getShapeEditorTreeviewSelection.mel
    
    Description:
          Get selections from shape editor tree view
    
    Input Arguments:
          int $scope - Scope of tree view selection:
    
          Simple Scopes:
            0: Selected blend shape deformer group indices.                 e.g. {"-1", "-2", "-3"}
            1: Selected blend shape deformers.                              e.g. {"blendShape1", "blendShape2", "blendShape3", "blendShape4"}
            2: Blend shape deformers in selected groups.                    e.g. {"blendShape1", "blendShape2"}
            3: Selected target group indices with blend shape name prefix.  e.g. {"blendShape1.-1", "blendShape1.-2", "blendShape2.-1", "blendShape2.-2"}
            4: Selected target indices with blend shape name prefix.        e.g. {"blendShape1.0", "blendShape1.1", "blendShape1.2"}
            5: Targets in selected groups with blend shape name prefix.     e.g. {"blendShape2.0", "blendShape2.1"}
            6: Inbetween targets.                                           e.g. {"blendShape2.0.5500", "blendShape2.1.5800"}
            7: Purely selected blend shape deformer (groups).               e.g. {"-1", "2", "blendshape1", "blendshap2", "-3"}
            8: Purely selected target (groups).                             e.g. {"blendshape1.1", "blendshape1.-1", "blendshape2.2", "blendshape2.-2"}
            9: Purely selected target (groups) within one BSD.              e.g. {"blendshape1.1", "blendshape1.-1"}
    
          Only one type of item is selected:
            10: Purely selected blend shape deformer group indices:, return {} for mixed selection
            11: Purely selected blend shape deformers:, return {} for mixed selection
            12: Blend shape deformers in purely selected of groups:, return {} for mixed selection
            13: Purely selected target group indices:, return {} for mixed selection
            14: Purely selected targets:, return {} for mixed selection
            15: Target in purely selected of groups, return {} for mixed selection
            16: Purely selected in-between targets. return {} for mixed selection
    
          Last Selected Item
            20: Last selection
    
          Only one type and its group type of item are selected:
            21: Purely selected blend shape deformers and the ones in group without duplicates, return {} for mixed selection.
            24: Purely selected target and the ones in group without duplicates, return {} for mixed selection.
    
          Flags:
            30: If selection contains reference item. return {"1"} if true; {"0"} if false;
            31: First selection item 
    
    Return Value:
        String array of given scope
    '''
    return pm.mel.getShapeEditorTreeviewSelection( scope )  # @UndefinedVariable
    