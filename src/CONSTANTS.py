

BASE_DIR     = '/Volumes/nyee/datasets/frcnn_data/'
CLASSES      = ['BENTHOCODON','ECHINOCREPIS','PENIAGONE_SP_1','PENIAGONE_SP_A','PENIAGONE_VITRAE','SCOTOPLANES_GLOBOSA','ELPIDIA']

VID_NAMES  = ['D008_03HD', 'D0232_04HD', 'D0442_06HD', 'D0443_05HD', 'D0673_04HD', 'D0772_09HD']
VID_DIRS   = ['{}{}/'.format(BASE_DIR, VID_NAME) for VID_NAME in VID_NAMES]
VID_EXT    = '.mov'

IMG_DIR_NAME = 'imgs'
IMG_DIRS     = ['{}{}/'.format(VID_DIR, IMG_DIR_NAME) for VID_DIR in VID_DIRS]
IMG_EXT      = '.png'

XML_DIR_NAME = 'xmls'
XML_DIRS     = ['{}{}/'.format(VID_DIR, XML_DIR_NAME) for VID_DIR in VID_DIRS]
XML_EXT      = '.xml'

ANN_PATH     = BASE_DIR + 'simple_annotations.txt'