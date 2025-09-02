import xml.etree.ElementTree as ET

def xml_to_dict(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    def elem_to_dict(elem):
        d = {}
        for child in elem:
            # Recursively convert child elements
            if len(child):
                d[child.tag] = elem_to_dict(child)
            else:
                d[child.tag] = child.text
        return d
    
    return elem_to_dict(root)