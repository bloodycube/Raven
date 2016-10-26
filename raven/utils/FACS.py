# coding:utf-8
'''
Created on 2016. 10. 10.

@author: kyuho_choi

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
import random

class FACS(object):
    '''FACS 관련 데이터 리턴    
    '''
    __DATA = [
        [ 1,  'Inner Brow Raiser',               101, 'brows', 'innerBrow_raiser',              ('L', 'R') ],
        [ 2,  'Outer Brow Raiser',               102, 'brows', 'outerBrow_raiser',              ('L', 'R') ],
        [ 4,  'Brow Lowerer',                    103, 'brows', 'brow_lowerer',                  ('L', 'R') ],
        [ 5,  'Upper Lid Raiser',                207, 'eyes',  'upperLid_raiser',               ('L', 'R') ],
        [ 6,  'Cheek Raiser and Lid Compressor', 208, 'eyes',  'cheek_raiser_n_lid_compressor', ('L', 'R') ],
        [ 7,  'Lid Tightener',                   206, 'eyes',  'lid_tightener',                 ('L', 'R') ],
        [ 8,  'Lips Toward Each Other',          401, 'mouth', 'lip_towardEachOther',           ('UL', 'UR', 'DL', 'DR') ],
        [ 9,  'Nose Wrinkler',                   301, 'nose',  'nose_wrinkler',                 ('L', 'R') ],
        [ 10, 'Upper Lip Raiser',                401, 'mouth', 'upperLip_raiser',               ('L', 'R') ],
        [ 11, 'Nasolabial Furrow Deepener',      302, 'nose',  'nasolabialFurrow_deepener',     ('L', 'R') ],
        [ 12, 'Lip Corner Puller',               401, 'mouth', 'lipCorner_puller',              ('L', 'R') ],
        [ 13, 'Sharp Lip Puller',                401, 'mouth', 'sharpLip_puller',               ('L', 'R') ],
        [ 14, 'Dimpler',                         401, 'mouth', 'dimpler',                       ('L', 'R') ],
        [ 15, 'Lip Corner Depressor',            401, 'mouth', 'lipCorner_depressor',           ('L', 'R') ],
        [ 16, 'Lower Lip Depressor',             401, 'mouth', 'lowerLip_depressor',            ('L', 'R') ],
        [ 17, 'Chin Raiser',                     401, 'mouth', 'chin_raiser',                   ()],
        [ 18, 'Lip Pucker',                      401, 'mouth', 'lip_pucker',                    ('L', 'R') ],
        [ 20, 'Lip Stretcher',                   401, 'mouth', 'lip_stretcher',                 ('L', 'R') ],
        [ 21, 'Neck Tightener',                  501, 'neck',  'neck_tightener',                ('L', 'R') ],
        [ 22, 'Lip Funneler',                    401, 'mouth', 'lip_funneler',                  ('UL', 'UR', 'DL', 'DR') ],
        [ 23, 'Lip Tightener',                   401, 'mouth', 'lip_tightener',                 ('UL', 'UR', 'DL', 'DR') ],
        [ 24, 'Lip Presser',                     401, 'mouth', 'lip_presser',                   ('UL', 'UR', 'DL', 'DR') ],
        [ 25, 'Lips Part',                       401, 'mouth', 'lips_part',                     () ],
        [ 26, 'Jaw Drop',                        401, 'mouth', 'jaw_drop',                      () ],
        [ 28, 'Lips Suck',                       401, 'mouth', 'lip_suck',                      ('UL', 'UR', 'DL', 'DR') ],
        [ 29, 'Jaw Thrust',                      401, 'mouth', 'jaw_thrust',                    () ],
        [ 30, 'Jaw Sideways',                    401, 'mouth', 'jaw_sideways',                  ('L', 'R') ],
        [ 31, 'Jaw Clencher',                    401, 'mouth', 'jaw_clencher',                  () ],
        [ 32, 'Bite',                            401, 'mouth', 'lip_bite',                      ('UL', 'UR', 'DL', 'DR') ],
        [ 33, 'Blow',                            401, 'mouth', 'cheek_blow',                    ('L', 'R') ],
        [ 34, 'Puff',                            401, 'mouth', 'cheek_puff',                    ('L', 'R') ],
        [ 35, 'Suck',                            401, 'mouth', 'cheek_suck',                    ('L', 'R') ],
        [ 38, 'Nostril Dilator',                 303, 'nose',  'nostril_dilator',               ('L', 'R') ],
        [ 39, 'Nostril Compressor',              304, 'nose',  'nostril_compressor',            ('L', 'R') ],
        [ 43, 'Eye Closure',                     205, 'eyes',  'eye_closure',                   ('L', 'R') ],
        [ 51, 'Head Turn Left',                  503, 'head',  'head_turn_left',                () ],
        [ 52, 'Head Turn Right',                 504, 'head',  'head_turn_right',               () ],
        [ 53, 'Head Up',                         505, 'head',  'head_up',                       () ],
        [ 54, 'Head Down',                       506, 'head',  'head_down',                     () ],
        [ 55, 'Head Tilt Left',                  507, 'head',  'head_tilt_left',                () ],
        [ 56, 'Head Tilt Right',                 508, 'head',  'head_tilt_right',               () ],
        [ 57, 'Head Forward',                    509, 'head',  'head_forward',                  () ],
        [ 58, 'Head Back',                       510, 'head',  'head_back',                     () ],
        [ 61, 'Eyes Turn Left',                  201, 'eyes',  'eye_left',                      ('L', 'R') ],
        [ 62, 'Eyes Turn Right',                 202, 'eyes',  'eye_right',                     ('L', 'R') ],
        [ 63, 'Eyes Up',                         203, 'eyes',  'eye_up',                        ('L', 'R') ],
        [ 64, 'Eyes Down',                       204, 'eyes',  'eye_down',                      ('L', 'R') ],
        [ 80, 'Swallow',                         502, 'neck',  'swallow',                       () ],
        ]    
    
    def __init__(self):
        pass
    
    def getDict(self):
        ''' 데이터를 딕셔너리 타입으로 리턴 '''
        result = []
        for item in sorted( self.__DATA ):            
            result.append( {'auNum':item[0], 'auName':item[1], 'attrNum':item[2], 'attrGrp':item[3], 'attrName':item[4], 'divPart':item[5]} )
   
    def getAttrs(self, attrNum=False, attrGrp=False, attrName=True, splitAttrName=False, splitPart=False, auNum=False, auName=False):
        ''' 어트리뷰트 이름들 리턴
        
        :param auNums: Action Unit Number 포함
        :type auNums: bool
        
        '''
        result = []
        for item in sorted( self.__DATA, key=lambda x:x[2] ):
            
            tmp = []
            if attrNum: tmp.append(item[2])
            if attrGrp: tmp.append(item[3])
            if attrName: tmp.append(item[4])
            if splitPart: tmp.append(item[5])
            if splitAttrName:
                sl=[]
                if not item[5]:
                    # 중앙만 존재하는 어트리뷰트
                    sl.append( item[4] )
                
                else:
                    # 분리가 되야하는 어트리뷰트
                    for part in item[5]:
                        sl.append( '%s_%s'%(item[4],part) )
                tmp.append(sl)                  
            
            if auNum: tmp.append(item[0])
            if auName: tmp.append(item[1])
            
            result.append( tmp )
            
        return result
    
    def getActionUnitName(self, *auNums):
        ''' 번호를 입력하면 해당 facs 이름을 받음
        
        :param auNums: Action Unint Numbers
        :type auNums: int, int,...
        
        :return: [attrName,...] 어트리뷰트 이름들
        :rtype: list
        
        :Example:
        >>> f=FACS()
        >>> f.getAuName(1,2,4)
        ['Inner Brow Raiser', 'Outer Brow Raiser', 'Brow Lowerer']
        '''
        result = []
        for auNum in auNums:
            for item in self.__DATA:
                if item[0] == auNum:
                    result.append( item[1] )
        return result
    
    def game(self):
        ''' FACS ActionUnit 암기용 게임 
        시작 후 번호가 출력되면 대응하는 ActionUnit 이름을 입력해야 함
        '''
        myFACS = { item[0]:item[1] for item in self.__DATA}
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




