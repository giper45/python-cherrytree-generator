from cherry import *
from os import path
DIR_EXAMPLE = "examples"
FIRST_EXAMPLE = path.join(DIR_EXAMPLE, "first.ctd")
ct = newdoc("root")
ct = addnode(ct, "root", "192.168.1.1")
ct = addnode(ct, "root", "192.168.1.2")

ct = addnode(ct, "192.168.1.1", "22 dropbear ssh")
ct = addnode(ct, "192.168.1.1", "21 pureFTPd")

link = new_link("https://google.com")
text = newtext("Hello world")

ct = add_ele(ct, "192.168.1.1", text)
ct = add_ele(ct, "192.168.1.2", link)

create(ct, FIRST_EXAMPLE)


