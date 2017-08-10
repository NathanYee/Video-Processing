# # dir_creation
# 
# Creates the directories of frcnn_data if they do not exist

import os
import CONSTANTS as c


def make_dir(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)


for VID in c.VID_KEYS:
    for DIR in c.DIR_KEYS:
        directory = c.DIR_DICT[VID][DIR]
        make_dir(directory)

make_dir(c.CROP_DIR)

for CROP_DIR in c.CROP_CLASS_DIRS:
    make_dir(CROP_DIR)
