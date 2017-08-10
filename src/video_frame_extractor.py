import CONSTANTS as c
import multiprocessing
import subprocess
import os


class Extractor():
    def __init__(self, video_name, increment=5):
        """
        the Extractor class contains all the necessary information to extract
        images from a video using ffmpeg. By default, it will extract a frame 
        every increment (5) seconds from the video
        
        :param video_name: name of the video
        :type  video_name: string
        :param increment: extract a frame every 'increment' seconds
        :type  increment: int
        
        :Example:
        
        Extractor('D008_03HD', 5)
        """
        self.video_name       = video_name
        self.input_video_path = c.DIR_DICT[self.video_name][c.SRC_VID]
        self.output_dir       = c.DIR_DICT[self.video_name][c.IMG_DIR]
        self.seconds_counter  = 0
        self.increment        = increment
        self.video_length     = self.get_length()
        
    
    def get_length(self):
        """
        gets the length of a video in seconds using ffprobe
        
        :returns length: length of video in seconds found at self.input_video_path
        :rtype   length: float
        """
        shell_string = "ffprobe -i {} -show_entries format=duration -v quiet -of csv='p=0'".format(self.input_video_path)
        result = subprocess.Popen(shell_string,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT,
                                  shell=True)
        length = result.communicate()[0]
        length = float(length.decode().strip('\n'))
        return length
    
    
    def get_timecode(self):
        """ converts self.seconds_counter into hh:mm:ss """
        m, s = divmod(self.seconds_counter, 60)
        h, m = divmod(m, 60)
        return ("%02d:%02d:%02d" % (h, m, s))
    
    
    def extract_img(self, output_path, timecode):
        """
        extracts image from video at timecode and saves it to output_path
        
        :param output_path: absolute path of the output file
        :param    timecode: time in format hh:mm:ss 
        :type output_path: string
        :type    timecode: string
        
        :Example:
        
        self.extract_img('/Volumes/nyee/datasets/frcnn_data/D008_03HD/imgs/D008_03HD_00-11-40.png', '00:11:40')
        """
        shell_string = 'ffmpeg -ss {} -i {} -frames:v 1 {}'.format(timecode,
                                                                   self.input_video_path,
                                                                   output_path)
        subprocess.call(shell_string, shell=True)
    
    
    def increment_seconds_counter(self):
        """ increment self.seconds_counter by self.increment """
        self.seconds_counter += self.increment
    
    
    def process_video(self):
        """ extract all the frames from video_name specified in __init__ """
        try:
            while self.seconds_counter < self.video_length:
                timecode = self.get_timecode()
                output_path = "{}{}_{}{}".format(self.output_dir,
                                                 self.video_name,
                                                 timecode.replace(':', '-'),
                                                 c.IMG_EXT)

                if not os.path.exists(output_path):
                    self.extract_img(output_path, timecode)

                self.increment_seconds_counter()
            return True
        except:
            return False


class Manager():
    def __init__(self):
        """
        initialize the manager. Note that we intentionally don't set pool as 
        an attribute here
        """
        pass

    def processes_video(self, video_name):
        """
        processes a video given its the name of the video

        :param video_name: the name of the video to be processed
        :type  video_name: string

        :returns result: True is success, False is exception
        :rtype   result: Bool

        :Example:
        process_video('D008_03HD')
        """
        print("Starting: " + video_name)
        extractor = Extractor(video_name)
        result = extractor.process_video()
        print("Finished: " + video_name)
        return result

    def processes_videos(self):
        """ process all videos """
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count() - 1)
        self.results = pool.map(self.processes_video, c.VID_KEYS)


manager = Manager()
manager.processes_videos()
