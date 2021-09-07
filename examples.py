from cherry import *
from os import path
DIR_EXAMPLE = "examples"
FIRST_EXAMPLE = path.join(DIR_EXAMPLE, "first.ctd")
ct = newdoc("root")
ct = addnode(ct, "root", "192.168.1.1")
ct = addnode(ct, "root", "192.168.1.2")

ct = addnode(ct, "192.168.1.1", "22 dropbear ssh")
ct = addnode(ct, "192.168.1.1", "21 pureFTPd")

create(ct, FIRST_EXAMPLE)


