import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import tools.CONSTANTS as c
import tools.IMAGEUTILS as im
import tools.XMLUTILS as xu
import numpy as np


class Cropper():
    """
    crops out the animals using the ground truth xml files
    """

    def __init__(self, allowed_dirs):
        """
        initializes the MeanFinder, assigning allowed_dirs to an attribute
        
        :param allowed_dirs: the target directories that will be used
        :type  allowed_dirs: list of strings
        """
        self.allowed_dirs = allowed_dirs
            
        
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
        format the filepath for the other computer. We also change make the
        change from xml file to img file
        
        :returns: the formatted filepath
        :rtype  : string
        """
        return filepath.replace('xmls', 'imgs').replace(c.XML_EXT, c.IMG_EXT)
    
    
    def extract_rects(self, annotation):
        """
        Extracts and returns the corners of the bounding boxes in a list called rects

        :param annotation: a pascal VOC XML annotation
        
        :returns rects: the list containing the corners of the bounding boxes
        :returns names: the names (classes) of the annotated objects
        """
        objects = [element for element in list(annotation) if element.tag == 'object']

        rects = []
        names = []
        for object_ in objects:
            for item in list(object_):
                if item.tag == 'bndbox':
                    corners = {}
                    for corner in list(item):
                        corners[corner.tag] = int(corner.text)
                    rects.append([(corners['xmin'], corners['ymin']), (corners['xmax'], corners['ymax'])])
                if item.tag == 'name':
                    names.append(item.text)
        return rects, names
        
    def crop_image(self, img, rect):
        """
        draws the rects and names onto an image
        
        :param img: image data
        :param rect: the rectangle that should be cropped
        :returns image_crop: the cropped image data
        """
        img_crop = img[rect[0][1]:rect[1][1], rect[0][0]:rect[1][0]]
        return img_crop
    
    def process_file_filepath(self, file, filepath):
        """
        Checks whether or not to process the file and filepath, if so, crop 
        the animals out of the image at filepath and save them to the correct
        directories
        
        :param file: the name of the file
        :param filepath: the filepath of the file
        """
        # check if image should be included in self.file_standards
        if self.file_standards(file, filepath):
            annotation = xu.open_xml_file(filepath)
            rects, names = self.extract_rects(annotation)
            img_filepath = self.format_filepath(filepath)
            img = im.imread(img_filepath)

            counter = 0
            for rect, name in zip(rects, names):
                img_crop = self.crop_image(img, rect)
                directory = os.path.join(c.CROP_DIR, name)
                filename = file.replace(c.XML_EXT, "_{}{}".format(counter, c.IMG_EXT))
                im.imsave(os.path.join(directory, filename), img_crop)
                counter += 1
        
    def process_files(self):
        """ walk through all files and create simple annotation """
        # first clear old annotations as we will be replacing them
        for root, dirs, files in os.walk(c.BASE_DIR):
            self.processed_file = False
            for file in sorted(files):
                filepath = os.path.join(root, file)
                self.process_file_filepath(file, filepath)


if __name__ == '__main__':
    cropper = Cropper(c.VID_KEYS)
    cropper.process_files()
