'''
Created on 2016. 10. 10.

@author: kyuho_choi
'''

blenList = [
    # 01 Brows
    'innerBrow_raiser_01__LR',
    'outerBrow_raiser_02__LR',
    'brow_lowerer_04__LR',
    
    # 02 Eyes
    'eyes_closed_43__LR',
    'upperLid_raiser_05__LR',
    'eyes_left_61__LR',
    'eyes_right_62__LR',
    'eyes_up_63__LR',
    'eyes_down_64__LR',
    'lid_tightener_07__LR',
    'cheek_raiser_06__LR',       # 0303
    
    'squeeze__43_07_06'

    # 03 Nose
    'nose_wrinkler_09__LR',      # 0301
    'nasolabial_deepener_11__LR',# 0302
    'nostril_dilator_38__LR',    # 0304
    'nostril_compressor_39__LR', # 0305
    
    # 04 Mouth
    'lips_part_25',              # 0401
    'lip_stretcher_20__LR',      # 0402
    'lip_pucker_18__LR',         # 0403
    'sharpLip_puller_13__LR',    # 0404
    'lipCorner_lowerer__LR',     # 0405
    'lipCorner_puller_12__LR__comb',# 0406
    'lipCorner_depressor_15__LR__comb',# 0407
    'upperLip_raiser_10__LR',    # 0408
    'lowerLip_depressor_16__LR', # 0409
    'lowerLip_up__RL',           # 0410
    'lips_left',                 # 0411
    'lips_right',                # 0412
    'lips_up',                   # 0413
    'lips_down',                 # 0414
    'dimpler_14__LR',            # 0415
 
    'lip_funnerler_22__UDLR',    # 0431
    'lip_pressor_24__UDLR',      # 0432
    'lip_tightener_23__UDLR',    # 0433
    'lip_bite_32__UDLR',         # 0434
    'lip_suck_28__UDLR',         # 0435

    'cheek_blow_33__LR'          # 0451
    'cheek_puff_34__LR'          # 0452
    'cheek_suck_35__LR'          # 0453

    
    # 05 Jaw
    'jaw_drop_26',               # 0501
    'jaw_sideway_left_30',       # 0502
    'jaw_sideway_right_30',      # 0503
    'jaw_thrust_29',             # 0504
    'jaw_clencher_31',           # 0505
    'chin_raiser_17',            # 0506
    'jaw_drop_26__min__lips_part__25'
    
    # 06 Neck
    'neck_tightener_21__LR',     # 0601
    'neck_swallow_80'            # 0602

]


import random

'''
FACS.items()
FACS.keys()
FACS.values()
FACS.viewitems()
FACS.viewkeys()
FACS.viewvalues()
FACS.get(25)
FACS.fromkeys([25,2,6])
FACS.has_key(25)    
'''

FACS = {
    1:'Inner Brow Raiser',
    2:'Outer Brow Raiser',
    4:'Brow Lowerer',
    5:'Upper Lid Raiser',
    6:'Cheek Raiser and Lid Compressor',
    7:'Lid Tightener',
    8:'Lips Toward Each Other',
    9:'Nose Wrinkler',
    10:'Upper Lip Raiser',
    11:'Nasolabial Furrow Deepener',
    12:'Lip Corner Puller',
    13:'Sharp Lip Puller',
    14:'Dimpler',
    15:'Lip Corner Depressor',
    16:'Lower Lip Depressor',
    17:'Chin Raiser',
    18:'Lip Pucker',
    20:'Lip Stretcher',
    21:'Neck Tightener',
    22:'Lip Funneler',
    23:'Lip Tightener',
    24:'Lip Presser',
    25:'Lips Part',
    26:'Jaw Drop',
    28:'Lips Suck',
    29:'Jaw Thrust',
    30:'Jaw Sideways',
    31:'Jaw Clencher',
    32:'Bite',
    33:'Blow',
    34:'Puff',
    35:'Suck',
    38:'Nostril Dilator',
    39:'Nostril Compressor',
    43:'Eye Closure',
    51:'Head Turn Left',
    52:'Head Turn Right',
    53:'Head Up',
    54:'Head Down',
    55:'Head Tilt Left',
    56:'Head Tilt Right',
    57:'Head Forward',
    58:'Head Back',
    61:'Eyes Turn Left',
    62:'Eyes Turn Right',
    63:'Eyes Up',
    64:'Eyes Down',
    80:'Swallow'
    }


def FACS_numTester():
    myFACS = FACS.copy()
    myFACS_num = len( myFACS )
    score = 0
    questionNum = 0

    # 다 맞을 때까지 문제는 끝나지 않음
    while myFACS:

        # 랜덤 번호 생성
        num=len( myFACS )
        randID = random.randrange( num )

        # 랜덤으로 뽑아냄
        auNum = myFACS.keys()[randID]
        auName = myFACS[auNum]

        # 질문
        try:
            print "(%02d/%02d)" % ( len( myFACS ), myFACS_num ),
            result = raw_input(" %02d "%auNum)
        except:
            break 
            
        # 질문 한 개수
        questionNum +=1
        
        # 평가용 스트링으로 변환
        inputVal = result.lower().replace(' ','')
        inputAuName = auName.lower().replace(' ','')

        # 판단
        if inputAuName == inputVal:
            # 점수 올려주고 
            score += 1
            
            # 맞은 문제는 문제에서 삭제
            myFACS.pop(auNum)       
            
            cond = 'Success!'
        else:
            cond = "Fail~ (%s)" % result
                  
        # 결과
        print "%s : %s" % ( auName, cond )

    print "\n Score : %02d/%02d %d%%"%(score, myFACS_num, int( float(score)/myFACS_num * 100 ))

FACS_numTester()
