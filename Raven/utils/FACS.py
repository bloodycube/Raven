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
class FACS(object):
    FACS = {
    #  NUM: FACS name                            Attribute name                                  Divide part
         1:['Inner Brow Raiser',                'innerBrow_raiser',                 'brows',    ('L','R')],
         2:['Outer Brow Raiser',                'outerBrow_raiser',                 'brows',    ('L','R')],
         4:['Brow Lowerer',                     'brow_lowerer',                     'brows',    ('L','R')],
         5:['Upper Lid Raiser',                 'upperLid_raiser',                  'eyes',     ('L','R')],
         6:['Cheek Raiser and Lid Compressor',  'cheek_raiser_n_lid_compressor',    'eyes',     ('L','R')],
         7:['Lid Tightener',                    'lid_tightener',                    'eyes',     ('L','R')],
         8:['Lips Toward Each Other',           'lip_towardEachOther',              'mouth',    ('UL', 'UR', 'DL', 'DR')],
         9:['Nose Wrinkler',                    'nose_wrinkler',                    'nose',     ('L','R')],
        10:['Upper Lip Raiser',                 'upperLip_raiser',                  'mouth',    ('L','R')],
        11:['Nasolabial Furrow Deepener',       'nasolabialFurrow_deepener',        'brows',    ('L','R')],
        12:['Lip Corner Puller',                'lipCorner_puller',                 'mouth',    ('L','R')],
        13:['Sharp Lip Puller',                 'sharpLip_puller',                  'mouth',    ('L','R')],
        14:['Dimpler',                          'dimpler',                          'mouth',    ('L','R')],
        15:['Lip Corner Depressor',             'lipCorner_depressor',              'mouth',    ('L','R')],
        16:['Lower Lip Depressor',              'lowerLip_depressor',               'mouth',    ('L','R')],
        17:['Chin Raiser',                      'chin_raiser',                      'mouth',    ()],
        18:['Lip Pucker',                       'lip_pucker',                       'mouth',    ('L','R')],
        20:['Lip Stretcher',                    'lip_stretcher',                    'mouth',    ('L','R')],
        21:['Neck Tightener',                   'neck_tightener',                   'neck',     ('L','R')],
        22:['Lip Funneler',                     'lip_funneler',                     'mouth',    ('UL', 'UR', 'DL', 'DR')],
        23:['Lip Tightener',                    'lip_tightener',                    'mouth',    ('UL', 'UR', 'DL', 'DR')],
        24:['Lip Presser',                      'lip_presser',                      'mouth',    ('UL', 'UR', 'DL', 'DR')],
        25:['Lips Part',                        'lips_part',                        'mouth',    ()],
        26:['Jaw Drop',                         'jaw_drop',                         'mouth',    ()],
        28:['Lips Suck',                        'lip_suck',                         'mouth',    ('UL', 'UR', 'DL', 'DR')],
        29:['Jaw Thrust',                       'jaw_thrust',                       'mouth',    ()],
        30:['Jaw Sideways',                     'jaw_sideways',                     'mouth',    ('L','R')],
        31:['Jaw Clencher',                     'jaw_clencher',                     'mouth',    ()],
        32:['Bite',                             'lip_bite',                         'mouth',    ('UL', 'UR', 'DL', 'DR')],
        33:['Blow',                             'cheek_blow',                       'mouth',    ('L','R')],
        34:['Puff',                             'cheek_puff',                       'mouth',    ('L','R')],
        35:['Suck',                             'cheek_suck',                       'mouth',    ('L','R')],
        38:['Nostril Dilator',                  'nostril_dilator',                  'brows',    ('L','R')],
        39:['Nostril Compressor',               'nostril_compressor',               'brows',    ('L','R')],
        43:['Eye Closure',                      'eye_closure',                      'brows',    ('L','R')],
        51:['Head Turn Left',                   'head_turn_left',                   'head',    ()],
        52:['Head Turn Right',                  'head_turn_right',                  'head',    ()],
        53:['Head Up',                          'head_up',                          'head',    ()],
        54:['Head Down',                        'head_down',                        'head',    ()],
        55:['Head Tilt Left',                   'head_tilt_left',                   'head',    ()],
        56:['Head Tilt Right',                  'head_tilt_right',                  'head',    ()],
        57:['Head Forward',                     'head_forward',                     'head',    ()],
        58:['Head Back',                        'head_back',                        'head',    ()],
        61:['Eyes Turn Left',                   'eye_left',                         'eyes',    ('L','R')],
        62:['Eyes Turn Right',                  'eye_right',                        'eyes',    ('L','R')],
        63:['Eyes Up',                          'eye_up',                           'eyes',    ('L','R')],
        64:['Eyes Down',                        'eye_down',                         'eyes',    ('L','R')],
        80:['Swallow',                          'swallow',                          'neck',    ()],
        }


