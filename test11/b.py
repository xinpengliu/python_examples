#!/usr/bin/python
#-*- coding:utf8 -*-
#b.py
from a import add_func #also can be import a
print("import add_func from module a")
print("result of 1 plus 2 is:")

print(add_func(1,2)) 
#if using "import a",then here should be "a.add_func" 
