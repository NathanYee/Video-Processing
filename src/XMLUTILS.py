from xml.etree import ElementTree

def open_xml_file(filename):
    """
    extract root Element from xml file

    Args:
        filename (string): the xml file to be opened

    Returns:
        annotation (Element): the root xml Element of the annotation file
    """
    with open(filename, 'rt') as f:
        tree = ElementTree.parse(f)
    annotation = tree.getroot()

    return annotation