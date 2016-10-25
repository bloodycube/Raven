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
    #  NUM: FACS name                            Attribute name                      Divide part
         1:['Inner Brow Raiser',                'innerBrow_raiser',                 ('L','R')],
         2:['Outer Brow Raiser',                'outerBrow_raiser',                 ('L','R')],
         4:['Brow Lowerer',                     'brow_lowerer',                     ('L','R')],
         5:['Upper Lid Raiser',                 'upperLid_raiser',                  ('L','R')],
         6:['Cheek Raiser and Lid Compressor',  'cheek_raiser_n_lid_compressor',    ('L','R')],
         7:['Lid Tightener',                    'lid_tightener',                    ('L','R')],
         8:['Lips Toward Each Other',           'lip_towardEachOther',              ('UL', 'UR', 'DL', 'DR')],
         9:['Nose Wrinkler',                    'nose_wrinkler',                    ('L','R')],
        10:['Upper Lip Raiser',                 'upperLip_raiser',                  ('L','R')],
        11:['Nasolabial Furrow Deepener',       'nasolabialFurrow_deepener',        ('L','R')],
        12:['Lip Corner Puller',                'lipCorner_puller',                 ('L','R')],
        13:['Sharp Lip Puller',                 'sharpLip_puller',                  ('L','R')],
        14:['Dimpler',                          'dimpler',                          ('L','R')],
        15:['Lip Corner Depressor',             'lipCorner_depressor',              ('L','R')],
        16:['Lower Lip Depressor',              'lowerLip_depressor',               ('L','R')],
        17:['Chin Raiser',                      'chin_raiser',                      ()],
        18:['Lip Pucker',                       'lip_pucker',                       ('L','R')],
        20:['Lip Stretcher',                    'lip_stretcher',                    ('L','R')],
        21:['Neck Tightener',                   'neck_tightener',                   ('L','R')],
        22:['Lip Funneler',                     'lip_funneler',                     ('UL', 'UR', 'DL', 'DR')],
        23:['Lip Tightener',                    'lip_tightener',                    ('UL', 'UR', 'DL', 'DR')],
        24:['Lip Presser',                      'lip_presser',                      ('UL', 'UR', 'DL', 'DR')],
        25:['Lips Part',                        'lips_part',                        ()],
        26:['Jaw Drop',                         'jaw_drop',                         ()],
        28:['Lips Suck',                        'lip_suck',                         ('UL', 'UR', 'DL', 'DR')],
        29:['Jaw Thrust',                       'jaw_thrust',                       ()],
        30:['Jaw Sideways',                     'jaw_sideways',                     ('L','R')],
        31:['Jaw Clencher',                     'jaw_clencher',                     ()],
        32:['Bite',                             'lip_bite',                         ('UL', 'UR', 'DL', 'DR')],
        33:['Blow',                             'cheek_blow',                       ('L','R')],
        34:['Puff',                             'cheek_puff',                       ('L','R')],
        35:['Suck',                             'cheek_suck',                       ('L','R')],
        38:['Nostril Dilator',                  'nostril_dilator',                  ('L','R')],
        39:['Nostril Compressor',               'nostril_compressor',               ('L','R')],
        43:['Eye Closure',                      'eye_closure',                      ('L','R')],
        51:['Head Turn Left',                   'head_turn_left',                   ()],
        52:['Head Turn Right',                  'head_turn_right',                  ()],
        53:['Head Up',                          'head_up',                          ()],
        54:['Head Down',                        'head_down',                        ()],
        55:['Head Tilt Left',                   'head_tilt_left',                   ()],
        56:['Head Tilt Right',                  'head_tilt_right',                  ()],
        57:['Head Forward',                     'head_forward',                     ()],
        58:['Head Back',                        'head_back',                        ()],
        61:['Eyes Turn Left',                   'eye_left',                         ('L','R')],
        62:['Eyes Turn Right',                  'eye_right',                        ('L','R')],
        63:['Eyes Up',                          'eye_up',                           ('L','R')],
        64:['Eyes Down',                        'eye_down',                         ('L','R')],
        80:['Swallow',                          'swallow',                          ()],
        }


