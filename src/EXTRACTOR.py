import CONSTANTS as c
import subprocess
import os

class Extractor():
    
    def __init__(self, video_name):
        """
        Initialize the extractor
        
        Args:
            video_name (string): name of the video
        """
        self.video_name       = video_name
        self.input_video_path = c.DIR_DICT[self.video_name][c.SRC_VID]
        self.output_dir       = c.DIR_DICT[self.video_name][c.IMG_DIR]
        self.seconds_counter  = 0
        self.increment        = 5
        self.video_length     = self.get_length()
        
    def get_length(self):
        """ returns the length of the video found at self.input_video_path """
        shell_string = "ffprobe -i {} -show_entries format=duration -v quiet -of csv='p=0'".format(self.input_video_path)
        result = subprocess.Popen(shell_string, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        length = result.communicate()[0]
        length = float(length.decode().strip('\n'))
        return length
    
    def get_timecode(self):
        """ converts self.seconds_counter into hh:mm:ss"""
        m, s = divmod(self.seconds_counter, 60)
        h, m = divmod(m, 60)
        return ("%02d:%02d:%02d" % (h, m, s))
    
    def extract_img(self, output_path, timecode):
        """
        extracts image from video

        Args:
            input_video_path  (string): absolute path of the video
            output_path       (string): absolute path of the output file
            time              (string): time in format hh:mm:ss
        """
        shell_string = 'ffmpeg -ss {} -i {} -frames:v 1 {}'.format(timecode, self.input_video_path, output_path)
        subprocess.call(shell_string, shell=True)
        
    def increment_seconds_counter(self):
        """ increment self.seconds_counter """
        self.seconds_counter += self.increment
        
    def process_video(self):
        """ extract all the frames from a video """
        while self.seconds_counter < self.video_length:
            timecode = self.get_timecode()
            output_path = "{}{}_{}{}".format(self.output_dir,
                                             self.video_name,
                                             timecode.replace(':', '-'),
                                             c.IMG_EXT)
            
            if not os.path.exists(output_path):
                self.extract_img(output_path, timecode)
            
            self.increment_seconds_counter()