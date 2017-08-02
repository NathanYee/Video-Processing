import os

# basic constants
CLASSES    = ['BENTHOCODON','ECHINOCREPIS','PENIAGONE_SP_1','PENIAGONE_SP_2',
              'PENIAGONE_SP_A','PENIAGONE_VITRAE','SCOTOPLANES_GLOBOSA','ELPIDIA']

VID_CLASSES= ['BENTHOCODON','ECHINOCREPIS','PENIAGONE_SP_2', 'PENIAGONE_PAPILLATA',
              'PENIAGONE_SP_A','PENIAGONE_VITRAE','SCOTOPLANES_GLOBOSA']

ALL_CLASSES= ['ELPIDIA','PENIAGONE_PAPILLATA','ECHINOCREPIS','SCOTOPLANES_GLOBOSA',
              'ONEIROPHANTA_MUTABILIS_COMPLEX','PENIAGONE_SP_1','LONG_WHITE',
              'SYNALLACTIDAE','PENIAGONE_VITRAE','FUNGIACYATHUS_MARENZELLERI',
              'CYSTECHINUS_LOVENI','PENIAGONE_SP_A','BENTHOCODON','TJALFIELLA',
              'PENIAGONE_SP_2','FISH']

VID_EXT    = '.mov'
IMG_EXT    = '.png'
XML_EXT    = '.xml'

# constant to start building directory tree
BASE_DIR   = '/Volumes/nyee/datasets/frcnn_data/'
SOURCE_DIR = '/Volumes/M3_temp/DeepLearningTests/benthic/' # ideally, source dir would be the same as base dir but I only
                                                           # have 160GB in my network drive and can't store the videos
DIR_DICT   = {}
VID_KEYS   = ['D008_03HD', 'D0232_03HD', 'D0232_04HD', 'D0442_06HD',
              'D0443_05HD', 'D0673_04HD', 'D0772_09HD', 'D0772_10HD',
              'D0904_D3HD']
TRAIN_VID_KEYS = ['D008_03HD', 'D0232_04HD', 'D0442_06HD', 'D0443_05HD',
                  'D0673_04HD', 'D0772_09HD', 'D0904_D3HD']
TEST_VID_KEYS  = ['D0232_03HD', 'D0772_10HD']


# keys for the dict of each video
VID_DIR    = 'video_dir'
IMG_DIR    = 'imgs'
XML_DIR    = 'xmls'
IMG_PRED_DIR   = 'img_preds'
XML_PRED_DIR   = 'xml_preds'
DIR_KEYS   = [VID_DIR, IMG_DIR, XML_DIR, IMG_PRED_DIR, XML_PRED_DIR]

# key for video source
SRC_VID    = 'source_video_path'

# build DIR_DICT
for VID in VID_KEYS:
    DIR_DICT[VID]               = {}
    DIR_DICT[VID][VID_DIR]      = '{}{}/'.format(BASE_DIR, VID)
    DIR_DICT[VID][IMG_DIR]      = '{}{}/{}/'.format(BASE_DIR, VID, IMG_DIR)
    DIR_DICT[VID][XML_DIR]      = '{}{}/{}/'.format(BASE_DIR, VID, XML_DIR)
    DIR_DICT[VID][IMG_PRED_DIR] = '{}{}/{}/'.format(BASE_DIR, VID, IMG_PRED_DIR)
    DIR_DICT[VID][XML_PRED_DIR] = '{}{}/{}/'.format(BASE_DIR, VID, XML_PRED_DIR)
    DIR_DICT[VID][SRC_VID]      = '{}{}/{}{}'.format(SOURCE_DIR, VID, VID, VID_EXT)
    
# path for simple annotation for Keras frcnn
ANN_PATH = BASE_DIR + 'simple_annotations.txt'
TEST_ANN_PATH = BASE_DIR + 'test_simple_annotations.txt'

# crop directories
CROP_DIR = os.path.join(BASE_DIR, 'crops')
CROP_CLASS_DIRS = [os.path.join(CROP_DIR, CLASS) for CLASS in ALL_CLASSES]

# xml constants
DATABASE='Unknown'
WIDTH='960'
HEIGHT='540'
DEPTH='3'
SEGMENTED='0'

POSE = 'Unspecified'
DIFFICULT = '0'
