# Video-Processing
A repository for that preprocesses [MBARI](http://www.mbari.org/) video data for use in [keras-frcnn](https://github.com/yhenon/keras-frcnn)


* CONSTANTS.py - Contains the constants that are shared between all the python files
* IMAGEUTILS.py - An alias for scipy image utilities
* UTILS.py - General utilities. Mostly file processing helper functions
* XMLUTILS.py - XML related utilites

* deinterlace_images.py - deinterlaces images that are extracted from MBARI video data
* dir_creation.py - creates all necessary directories used by various python scripts
* done.pkl - stores with files have been deitnerlaced, probably needs to be renamed
* ffmpeg_extractor.py - uses ffmpeg and python subprocess calls to extract images from videos
* image_mean.py - calculates the mean image channels from images that are used in the training data
* simple_annotations.py - creates annotations in the "simple annotation" format of the training and testing data
