
# coding: utf-8

# In[1]:

import os
import CONSTANTS as c
import UTILS as u
import XMLUTILS as xu


# In[2]:

class SimpleAnnotator():
    """
    simpleAnnotator will create a new simple annotation text file by
    recursively descending though directories starting at base_dir by
    processing xml annotations and image filenames
    """    
    
    def __init__(self, allowed_dirs, ann_path, base_dir=c.BASE_DIR):
        """
        initialize the SimpleAnnotator
        
        :param allowed_dirs: the target directories that will be used
        :type  allowed_dirs: list of strings
        :param ann_path: the path to store newly created simple annotations
        :type  ann_path: string
        :param base_dir: the base directory to walk
        :type  base_dir: string
        """
        self.allowed_dirs = allowed_dirs # only include if from these dirs
        self.ann_path = ann_path # path to store simple annotations
        self.processed_file = False
        self.base_dir = base_dir
    
    def process_annotation(self, annotation, img_filepath):
        """
        uses an annotation and an img_filepath to append objects to a simple
        annotation text file. You can read more about simple annotations
        here: https://github.com/yhenon/keras-frcnn
        
        :param annotation: a pascal VOC XML annotation
        :type  annotation: Element

        :param img_filepath: the filepath of the image on training machine
        :type  img_filepath: string
        """
        for object_ in annotation.findall('object'):
            name = ((object_.find('name')).text)
            corners = ([int(corner.text) for corner in list(object_.find('bndbox'))])
            data = '{},{},{},{},{},{}'.format(img_filepath, corners[0], corners[1], corners[2], corners[3], name)
            u.append_to_file(self.ann_path, data)
            
        
    def clear_annotation_path(self):
        """ clear annotation file at self.ann_path """
        u.remove_file_contents(self.ann_path)
            
        
    def file_standards(self, file, filepath):
        """
        checks to make sure that the file should be processed. In this case:
        
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
        return filepath.replace('Volumes', 'raid').replace('xmls', 'imgs').replace(c.XML_EXT, c.IMG_EXT)
        
        
    def process_files(self):
        """ walk through all files and create simple annotation """
        # first clear old annotations as we will be replacing them
        self.clear_annotation_path()
        
        for root, dirs, files in os.walk(self.base_dir):
            # set self.processed_file to false for user feedback
            self.processed_file = False
            for file in sorted(files):
                filepath = os.path.join(root, file)

                # check if file should be included in the simple_annotations
                if self.file_standards(file, filepath):
                    # set self.processed_file to true for user feedback
                    self.processed_file = True
                    annotation = xu.open_xml_file(filepath)
                    img_filepath = self.format_filepath(filepath)
                    self.process_annotation(annotation, img_filepath)
                    
            # if we've processed a file in the given root dir, notify the
            # user that the root directory has been processed
            if self.processed_file:
                print("Processed: " + root)


# In[3]:

train_annotator = SimpleAnnotator(c.TRAIN_VID_KEYS, c.ANN_PATH)
train_annotator.process_files()


# In[4]:

test_annotator = SimpleAnnotator(c.TEST_VID_KEYS, c.TEST_ANN_PATH)
test_annotator.process_files()


# In[ ]:



