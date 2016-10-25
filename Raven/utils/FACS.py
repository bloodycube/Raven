'''
Created on 2016. 10. 10.

@author: kyuho_choi
'''

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
