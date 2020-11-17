#BUILD-IN MODULE (os)

#WORKING WITH DIRECTORY

#1.getcwd()....(get current working directory)
import os
print(os.getcwd())

#2.mkdir()...(make dir)
os.mkdir('New_dir')
    #for making child dir inside the New_dir
    os.mkdir('New_dir/child_dir')
    """
    if parent dir not present gives error
    """
#rmdir()....remove directory
os.rmdir('my')                 #remove the parent dir
     #removing child directory (your1 will be deleted)
     os.rmdir('my/your1')

#3.makedirs()....make directories inside directories
os.makedirs('parent/child_dir/grand_child')
"""
does not gives error even if parent dir is not present it will create dir with new dir
"""

#removedirs()....remove directories
os.removedirs('parent/child/grand_child')

#chdir()...change working dir
print(os.getcwd())
os.chdir('parent')
print(os.getcwd())
"""op--
D:\Python
D:\Python\parent
"""

import os
print(os.getcwd())
os.chdir('E:/py')
print(os.getcwd())
"""op--
D:\Python
E:\py
"""

#rename('old_dir','new_dir').....rename dir
os.rename('parent','Parent_dir')

#walk()
"""
walk () generates the file names in a directory tree by walking the tree either top-down or bottom-up.
Following is the syntax for walk () method − top − Each directory rooted at directory, yields 3-tuples, i.e., (dirpath, dirnames, filenames)

syntax
    os.walk(path,topdown=True,onerror=None,followlinks=Flase)
    1.path               -it represent dir name. we can write (.) to specify current dir
    2.topdown            -if True(traverse top-down) if False(traverse bottom-up)
    3.onerror            -we can give function, what to do when an error is dectected.
    4.followlink         -
"""
w=os.walk('.')
for i in w:
    print(i)

"""
gives all files and folder in current working dir
"""

import os
w=os.walk('walk method')
for i in w:
    print(i)
"""op---
('walk method', ['parent'], [])
('walk method\\parent', ['child'], ['file.txt.txt'])
('walk method\\parent\\child', [], [])
               |                 |   |
      represent dir                  |    ----------------------------represent file=
                                represent folder

"""

#listdir(it will give the list of all folders and files)
import os
print(os.listdir('D://Python'))


#os.path

#isfile()....(check file exist or not)
#isdir
import os
s=os.path.isfile('file.txt')
print(s)
"""
True
"""

#exists
import os
print(os.path.exists('Makedir'))

#for dir
print(os.path.isdir('__pycache__'))

#
import os
s=os.path.isfile('D:/Python/my/file.txt')
print(s)

#
import os
f=input('Enter file name:')
if os.path.isfile(f):
    print(f,'File exist:')
else:
    print(f,'Not exist:')
"""op--
Enter file name:file.txt
file.txt File exist:
"""
