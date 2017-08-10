# # Training Mean
# 
# This notebook calculates the mean (by color channel) of the training images.
# This value is used in the keras-frcnn config.py file for network training and testing.

import os
import CONSTANTS as c
import IMAGEUTILS as im
import XMLUTILS as xu
import numpy as np


class MeanFinder():
    """
    calculates the mean (by color channel, RGB) of the specifed directories.
    This value put in the keras-frcnn config.py file for network training
    and testing. 
    """
    
    def __init__(self, allowed_dirs):
        """
        initializes the MeanFinder, assigning allowed_dirs to an attribute
        
        :param allowed_dirs: the target directories that will be used
        :type  allowed_dirs: list of strings
        """
        self.allowed_dirs = allowed_dirs # only include if from these dirs
        
    
    def process_img_filepath(self, img_filepath):
        """
        computes the mean of the image at img_filepath
        
        :param annotation: a pascal VOC XML annotation
        :type  annotation: Element

        :param img_filepath: the filepath of the image on training machine
        :type  img_filepath: string
        """
        return np.mean(im.imread(img_filepath), axis=(0,1))
        
            
    def file_standards(self, file, filepath):
        """
        checks to make sure that the file should be processed further. In
        this case:
        
        The file must be an xml file
        The filepath must not be from xml_preds
        One of the allowed directory names must be in the filepath
        
        :param file: the name of the file
        :type  file: string
        :param filepath: the full filepath of the file
        :type  filepath: string
        
        :returns: whether or not the file/filepath should be included
        :rtype  : bool
        """
        is_xml   = bool(file[-4:] == c.XML_EXT)
        not_pred = bool('xml_preds' not in filepath)
        allowed_dir = any([dir_ in filepath for dir_ in self.allowed_dirs])
        return (all([is_xml, not_pred, allowed_dir]))
        
        
    def format_filepath(self, filepath):
        """
        change from xml file to img file
        
        :returns: the formatted filepath
        :rtype  : string
        """
        return filepath.replace('xmls', 'imgs').replace(c.XML_EXT, c.IMG_EXT)
        
        
    def process_files(self):
        """
        walk through all files and calculate the image mean. We make sure 
        that each image is 
        
        :returns: the mean of the images
        :rtype  : ndarray
        """
        means = []
        #iterate through all files
        for root, dirs, files in os.walk(c.BASE_DIR):
            for file in sorted(files):
                filepath = os.path.join(root, file)

                # only allow images in the standardized format that have been annotated
                if self.file_standards(file, filepath):
                    # open_xml_file is called here instead of in file_standards
                    # to reduce unessessary xml processing
                    annotation = xu.open_xml_file(filepath)
                    
                    # only process images that contain objects
                    if xu.contains_objects(annotation):
                        img_filepath = self.format_filepath(filepath)
                        means.append(self.process_img_filepath(img_filepath))
        
        return(np.mean(means, axis=(0)))


if __name__ == '__main__':
    train_mean = MeanFinder(c.TRAIN_VID_KEYS)
    print("Train mean: " + str(train_mean.process_files()))
