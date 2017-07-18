

BASE_DIR   = '/Volumes/nyee/datasets/frcnn_data/'
SOURCE_DIR = '/Volumes/M3_temp/DeepLearningTests/benthic/'

CLASSES    = ['BENTHOCODON','ECHINOCREPIS','PENIAGONE_SP_1','PENIAGONE_SP_2',
              'PENIAGONE_SP_A','PENIAGONE_VITRAE','SCOTOPLANES_GLOBOSA','ELPIDIA']

VID_EXT    = '.mov'
IMG_EXT    = '.png'
XML_EXT    = '.xml'

DIR_DICT   = {}
VID_KEYS   = ['D008_03HD', 'D0232_04HD', 'D0442_06HD', 'D0443_05HD', 'D0673_04HD', 'D0772_09HD']

# keys for the dict of each video
VID_DIR    = 'video_dir'
IMG_DIR    = 'imgs'
XML_DIR    = 'xmls'
IMG_PRED_DIR   = 'img_preds'
XML_PRED_DIR   = 'xml_preds'
DIR_KEYS   = [VID_DIR, IMG_DIR, XML_DIR, IMG_PRED_DIR, XML_PRED_DIR]

SRC_VID    = 'source_video_path'

# build DIR_DICT
for VID in VID_KEYS:
    DIR_DICT[VID]          = {}
    DIR_DICT[VID][VID_DIR] = '{}{}/'.format(BASE_DIR, VID)
    DIR_DICT[VID][IMG_DIR] = '{}{}/{}/'.format(BASE_DIR, VID, IMG_DIR)
    DIR_DICT[VID][XML_DIR] = '{}{}/{}/'.format(BASE_DIR, VID, XML_DIR)
    DIR_DICT[VID][IMG_PRED_DIR] = '{}{}/{}/'.format(BASE_DIR, VID, IMG_PRED_DIR)
    DIR_DICT[VID][XML_PRED_DIR] = '{}{}/{}/'.format(BASE_DIR, VID, XML_PRED_DIR)
    DIR_DICT[VID][SRC_VID] = '{}{}/{}{}'.format(SOURCE_DIR, VID, VID, VID_EXT)

# resulting simple annotation for Keras frcnn
ANN_PATH   = BASE_DIR + 'simple_annotations.txt'

# xml constants
DATABASE='Unknown'
WIDTH='960'
HEIGHT='540'
DEPTH='3'
SEGMENTED='0'

POSE = 'Unspecified'
DIFFICULT = '0'
