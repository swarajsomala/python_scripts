#import xml.etree.ElementTree as ET
#tree = ET.parse('13.arxml')
#root = tree.getroot()
#print(root)
#for child in root:
#     print(child.tag, child.attrib)
from xml.etree import ElementTree

with open('data.xml', 'rt') as f:
    tree = ElementTree.parse(f)
#for node in tree.iter():
#    print(node.tag, node.attrib)
for node in tree.iter('country'):
	name=node.attrib.get('year') 
	print(name)