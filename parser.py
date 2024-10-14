import xml.etree.ElementTree as ET


def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    return root
