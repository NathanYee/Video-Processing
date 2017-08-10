
# coding: utf-8

# # dir_creation
# 
# Creates the directories of frcnn_data if they do not exist

# In[1]:

import os
import CONSTANTS as c


# In[2]:

def make_dir(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)


# In[3]:

for VID in c.VID_KEYS:
    for DIR in c.DIR_KEYS:
        directory = c.DIR_DICT[VID][DIR]
        make_dir(directory)


# In[4]:

make_dir(c.CROP_DIR)

for CROP_DIR in c.CROP_CLASS_DIRS:
    make_dir(CROP_DIR)


# In[ ]:



