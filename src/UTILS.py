def remove_file_contents(filepath):
    """ clears file """
    open(filepath, 'w').close()

def append_to_file(filepath, data):
    with open(filepath, 'a') as f:
        f.write(data + '\n')