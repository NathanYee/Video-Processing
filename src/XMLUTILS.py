from xml.etree import ElementTree
import CONSTANTS as c


def open_xml_file(filename):
    """
    extract root Element from xml file

    :param filename: the xml file to be opened
    :type  filename: string

    :returns: the root xml Element of the annotation file
    :rtype  : Element
    """
    with open(filename, 'rt') as f:
        tree = ElementTree.parse(f)
    annotation = tree.getroot()

    return annotation


def element_with_text(tag, text, attribute={}):
    """
    Adds text to an ElementTree Element

    :param tag: the tag for the Element
    :type  tag: string
    :param text: the text for the Element
    :type  text: string
    :param attribute: optional attributes for the Element
    
    :returns text_element: a XML Element with added text
    :rtype   text_element: Element
    """
    text_element = ElementTree.Element(tag=tag, attrib=attribute)
    text_element.text = text
    return text_element


def indent(elem, level=0):
    """
    Modifies an element in place to pretty print XML VOC style XML files

    :param elem: the root of the XML tree
    :type  elem: Element
    :param level: number of additional tabs to append
    :type  level: integer
    """
    i = "\n" + level * "\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i   


def get_truncated_value(object_):
    """

    :param object_: the data structure that contains all necessary information to create an Element object
    :return value: the value for truncated
    """
    truncated = '0'
    if object_['xmin'] == '0' or object_['ymin'] == '0' or object_['xmax'] == '960' or object_['ymax'] == '540':
        truncated = '1'
    return truncated


def create_object_element(object_):
    """

    :param object_: the data structure that contains all necessary information to create an Element object
    :return object_element:
    """
    object_element = ElementTree.Element(tag='object')
    object_element.append(element_with_text('name',  object_['name']))
    object_element.append(element_with_text('pose', c.POSE))
    object_element.append(element_with_text('truncated',  get_truncated_value(object_)))
    object_element.append(element_with_text('difficult',  c.DIFFICULT))

    bndbox_element = ElementTree.Element(tag='object')
    bndbox_element.append(element_with_text('xmin',  object_['xmin']))
    bndbox_element.append(element_with_text('ymin',  object_['ymin']))
    bndbox_element.append(element_with_text('xmax',  object_['xmax']))
    bndbox_element.append(element_with_text('ymax',  object_['ymax']))
    object_element.append(bndbox_element)

    return object_element


def generate_xml(filename, path, object_list, folder=c.IMG_DIR, database=c.DATABASE, width=c.WIDTH, height=c.HEIGHT, depth=c.DEPTH, segmented=c.SEGMENTED):
    """
    writes xml to disk with given inputs

    :param filename: the filename of the image
    :param path: the path of the image
    :param object_list: the list of object Elements
    :param folder: the name of the img folder
    :param database: the database to be specified
    :param width: the width of the video
    :param height: the height of the video
    :param depth: the number of channels in the video
    :param segmented: 1 if objects are segmented, 0 if not
    """
    new_root = ElementTree.Element(tag='annotation', attrib={'verified'='"no"'})
    new_root.append(element_with_text('folder', folder))
    new_root.append(element_with_text('filename', filename))
    new_root.append(element_with_text('path', path))

    source = ElementTree.Element(tag='source')
    source.append(element_with_text('database', database))
    new_root.append(source)

    size = ElementTree.Element(tag='size')
    size.append(element_with_text('width',  width))
    size.append(element_with_text('height', height))
    size.append(element_with_text('depth',  depth))
    new_root.append(size)

    new_root.append(element_with_text('segmented', segmented))

    for object_ in object_list:
        new_root.append(create_object_element(object_))

    indent(new_root)
    new_tree = ElementTree.ElementTree(new_root)
    xml_path = path.replace('imgs', 'xmls').replace('png', 'xml')
    new_tree.write(xml_path)
    
