# # dir_creation
# 
# Creates the directories of frcnn_data if they do not exist

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tools.CONSTANTS as c
import tools.UTILS as u


if __name__ == '__main__':
	for VID in c.VID_KEYS:
	    for DIR in c.DIR_KEYS:
	        directory = c.DIR_DICT[VID][DIR]
	        u.make_dir(directory)

	u.make_dir(c.CROP_DIR)

	for CROP_DIR in c.CROP_CLASS_DIRS:
	    u.make_dir(CROP_DIR)
