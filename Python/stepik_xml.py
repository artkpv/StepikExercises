from xml.etree import ElementTree
import sys

xml = sys.stdin.read().strip()
if not xml.startswith('<'):
    xml = xml[3:]

colors = { 'red' : 0 , 'green' : 0, 'blue' : 0 }
def traverse(el, level):
    c = el.attrib['color']
    colors[c] += level
    for child in el :
        traverse(child, level + 1)

root = ElementTree.fromstring(xml)
traverse(root, 1)

print(colors['red'], colors['green'], colors['blue'])




