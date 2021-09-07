from cherry import *

ct = open("files/test_valid.ctd")




def test_newlink_str(): 
    assert newlink_str("https://google.com")  == '<rich_text link="webs https://google.com">https://google.com</rich_text>'


def test_newnode_str():
    assert newnode_str("newnode", 1111) == '<node name="newnode" unique_id="1" prog_lang="custom-colors" tags="" readonly="0" custom_icon_id="0" is_bold="0" foreground="" ts_creation="1111" ts_lastsave="1111"></node>'


def test_getnode():
    n = getnode(ct, 'jenkins') 
    n2 = getnode(ct, 'notexistent') 
    assert n.attrib['name'] == 'jenkins'
    assert n2 == False


def test_ids():
    c_ids = ids(ct)
    c_ids.sort()
    assert c_ids == [1, 2, 3, 4, 5, 6]

def test_newid():
    c_ids = ids(ct)
    assert new_id(c_ids) == 7

def test_new():
    ct = newdoc("mytest")
    all = []
    for child in ct:
        all.append(child)
    assert all[0].tag == "bookmarks"
    assert all[1].tag == "node"
    assert all[1].attrib['name'] == "mytest"


def test_newnode():
    new_ct = addnode(ct, "jenkins", "newsubnode")
    assert getnode(new_ct, "newsubnode") != None

    # create(ct, "newfile")

