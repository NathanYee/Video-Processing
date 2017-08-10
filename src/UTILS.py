import os


def remove_file_contents(filepath):
    """
    clears the file located at filepath of all its contents

    :param filepath: the path to the file to be cleared
    :return: None
    """
    open(filepath, 'w').close()

def append_to_file(filepath, data):
    """
    append data to file located at filepath

    :param filepath: the file to be appended to
    :param data: the data to be appended
    :return: None
    """
    with open(filepath, 'a') as f:
        f.write(str(data) + '\n')
        
def clear_DS(file, filepath):
    """
    clears the automatically created .DS_Store files that OSX Finder creates

    :param file: the name of the file
    :type  file: string
    :param filepath: the full filepath of the file
    :type  filepath: string
    """
    if file == '.DS_Store':
        os.unlink(filepath)


def make_dir(directory):
    """
    creates directory if it does not exist

    :param directory: absolute path of target directory
    :type  directory: string
    """
    if not os.path.isdir(directory):
        os.mkdir(directory)