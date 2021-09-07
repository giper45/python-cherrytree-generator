from utils import *
import copy
import xml.etree.ElementTree as ET

NODE_TAG= "node"
base_cherry = """<?xml version="1.0" encoding="UTF-8"?><cherrytree><bookmarks list=""/></cherrytree>"""

def open(n):
    tree = ET.parse(n)
    root = tree.getroot()
    return root

def create(ct, name):
    tree = ET.ElementTree(ct)
    tree.write(name)




def newlink_str(l):
    return "<rich_text link=\"webs {}\">{}</rich_text>".format(l, l)

def newtext_str(t):
    return "<rich_text>{}</rich_text>".format(t)

def newtext(t):
    return ET.fromstring(newtext_str(l))
    
def new_link(l):
    return ET.fromstring(newlink_str(l))

def newimg_str(l):
    return '<encoded_png char_offset="0" justification="left" link=""></encoded_png>'

def newimg(l):
    return ET.fromstring(newimg_str(l))

def newnode_str(name, ts):
    return '<node name="{}" unique_id="1" prog_lang="custom-colors" tags="" readonly="0" custom_icon_id="0" is_bold="0" foreground="" ts_creation="{}" ts_lastsave="{}"></node>'.format(name, ts, ts)

def newnode(l):
    return ET.fromstring(newnode_str(l, timestamp()))

def newdoc(root_name):
    root = ET.fromstring(base_cherry)
    root.append(newnode(root_name))
    return root


def ids(ct):
    return [int(c.attrib['unique_id']) for c in ct.iter() if 'unique_id' in c.keys()]
def new_id(ids):
    # find major and up + 1
    return max(ids) + 1



def isnode(n):
    return n.tag == NODE_TAG

def getnode(ct, name):
    ret = ""
    for c in ct.iter('node'):
        if c.attrib['name'] == name:
            ret = c

    return ret if ret != "" else False

def addnode(ct, parent_name, newnode_name):
    new_ct = copy.deepcopy(ct)
    parent = getnode(new_ct, parent_name)
    newnode_ele = newnode(newnode_name)
    parent.append(newnode_ele)
    return new_ct