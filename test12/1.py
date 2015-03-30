#!/usr/bin/python
#-*- coding:utf8 -*-
import os
import os.path
rootdir="."
for parent,dirnames,filenames in os.walk(rootdir):
		#case 1:
		for dirname in dirnames:
			print("parent is:"+parent)
			print("dirname is:"+dirname)
		#case 2:
		for filename in filenames:
			print("parent is:"+parent)
			print("filename with full path:"+os.path.join(parent,filename))

'''
知识点：
1.os.walk 返回三元组，其中dirnames是所有文件夹名字（不包含路径），
filenames是所有文件的名字（不包含路径），parent表示父目录
2.case1，演示了如何遍历所有目录；
case2.演示了如何遍历所有文件
3.os.path.join（dirname，filename）：连接为长目录格式

'''
