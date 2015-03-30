#!/usr/bin/python
#-*- coding:utf8 -*-
def sum(a,b):
	return a+b

func = sum
r = func(5,6)
print(r)

#提供默认值
def add(a,b=2):
	return a+b
r=add(1)
print(r)
r=add(1,5)
print(r)


#the range() function the system provide
a = range(1,10)
for i in a:
	print(i)
a = range(-2,-11,-3) #the 3rd parameter stands for step
for i in a:
	print(i)

'''
知识点：
1.python不用{}来控制程序结构，他强迫你用缩进来写程序，使代码清晰
2.定义函数方便简单
3.方便好用的range函数

'''

