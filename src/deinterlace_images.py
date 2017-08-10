import os
import CONSTANTS as c
import IMAGEUTILS as im
import UTILS as u
import pickle
from time import sleep


class Deinterlacer():
    
    def __init__(self, deint_pkl_file='done.pkl', base_dir=c.BASE_DIR):
        """
        all images must be deinterlaced before being used in the neural
        network. This slightly improves accuracy and vastly reduces file
        size. Note that the deinterlacer will never deinterlace a unique
        filename twice, a user must manually delete the deint_pkl_file.
        
        
        :param deint_pkl_file: the filename of the pickled set of all
                               deinterlaced files
        :type  deint_pkl_file: string
        :param base_dir: the base directory to walk
        :type  base_dir: string
        """
        self.deint_pkl_file = deint_pkl_file
        self.deinterlaced_files = self.get_deinterlaced_files()
        self.sleep_time = 30 # the number of seconds to wait after
                             # deinterlacing all files
        self.base_dir = base_dir
        
        
    def get_deinterlaced_files(self):
        """
        unpickles the set of deinterlaced files if it exists. Otherwise, 
        create the set from scratch
        
        :returns: the set of deinterlaced files
        :rtype  : set
        """
        try:
            with open(self.deint_pkl_file, 'rb') as f:
                deinterlaced_files = pickle.load(f)
        except:
            print("Exception - will create new deinterlaced files set")
            deinterlaced_files = set()
        return deinterlaced_files
    
    
    def pickle_deinterlaced_files(self):
        """ pickle the process_files set """
        with open(self.deint_pkl_file, 'wb') as f:
            pickle.dump(self.deinterlaced_files, f)
    
    
    def de_interlace(self, img):
        """
        de-interlaces an image by taking every other row and every other colum

        :param img: the image data
        :type  img: ndarray
        
        :returns de_interlaced_image: the de-interlaced image
        :rtype   de_interlaced_image: ndarray
        """
        de_interlaced_img = img[::2, 1::2]
        return de_interlaced_img
    
    
    def process_file(self, filepath):
        """
        reads in filepath, de-interlaces, and writes new image
        
        :param filepath: the filename of the image to be operated on
        :type  filepath: string
        :returns: True if the file has already been deinterlaced
        """
        img = im.imread(filepath)
        if img.shape != (1080, 1920, 3):
            return True
        de_interlaced_img = self.de_interlace(img)
        im.imsave(filepath, de_interlaced_img)
        
        
    def file_standards(self, file, filepath):
        """
        checks to make sure that the file should be processed. In this case:
        
        The file must have the IMG extension
        The file must not have already been processed
        The file must be larger then 2MB. Interlaced images are around 10MB,
        while deinterlaced images are are ound 850KB.
        
        :param file: the name of the file
        :type  file: string
        :param filepath: the full filepath of the file
        :type  filepath: string
        
        :returns: whether or not the file/filepath should be included
        :rtype  : bool
        """
        is_xml   = bool(file[-4:] == c.IMG_EXT)
        not_done = bool(filepath not in self.deinterlaced_files)
        is_large = bool(os.path.getsize(filepath) > 2*(10**6))
        return (all([is_xml, not_done, is_large]))
    
    
    def process_files(self):
        """ Walk through all files and try to deinterlace every image """
        while True:
            #iterate through all files
            for root, dirs, files in os.walk(self.base_dir):
                for file in sorted(files):
                    filepath = os.path.join(root, file)

                    # check that it is an image file created by ffmpeg and not already processed
                    if self.file_standards(file, filepath):
                        self.process_file(filepath)
                        self.deinterlaced_files.add(filepath)
                        print(filepath + ": done")
                        
                self.pickle_deinterlaced_files()

            sleep(self.sleep_time)


deinterlacer = Deinterlacer()
deinterlacer.process_files()