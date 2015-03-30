#!/usr/bin/python
#-*- coding:utf8 -*-
#条件和循环语句
x=int(input("pls enter an integer:"))
if x<0:
	x=0
	print("negative changed to  zero")

elif x==0:
	print("zero")

else:
	print("more")

#loops list
a = ['cat','windows','defenestrate']
for x in a:
	print(x,len(x))

'''
知识点：
1.条件和循环语句
2.如何得到控制台的输入

'''
