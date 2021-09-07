# python-cherrytree-generator
Cherry-tree is a wonderful tool used to take notes. Is is commonly used during Penetration Testing activities. 
This project is a simple Python API that creates dtd cherry tree files (basically, xml files). 
It can be useful to use cherrytree in automation steps.


## Usage   
See `test` and `example` to see how it works:      
` git clone https://github.com/giper45/python-cherrytree-generator`

### Quick example:    
```   
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

``` 
## API   
### open(filename)   
Open a ctd element

### create(ct, name)   
Create a new cherrytree    

### new_link(link)   
Generate a new link node   
### new_text(text)   
Generate a new text node   

### newimg(i)   
Generate a new image   

### newnode(l)   
Create a new node with name    

### newdoc(root_name)  
Create a new ctd data document   
### add_ele(ct, node_name, newele)   
Add a new element to cherry tree document   

### add_node(ct, parent_name, newnode_name)   
Add a new node to parent   


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

