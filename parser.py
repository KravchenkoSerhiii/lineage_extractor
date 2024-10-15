import xml.etree.ElementTree as ET


def parse_xml(file: str) -> ET.ElementTree:
    tree = ET.parse(file)
    return tree.getroot()
