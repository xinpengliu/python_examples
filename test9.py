#!/usr/bin/python
#-*- coding:utf8 -*-
spath="./test.txt"
f=open(spath,"w")#oepns file for writing ,create new file if the file not exist
f.write("First line 1.\n")
f.writelines("First line 2.")
f.close()

f=open(spath,"r")#open file for reading

for line in f:
	print("每一行数据是：%s"%line)

f.close

'''
知识点：
1.open的参数，r表示读，w写数据（在写之前会清空之前的数据）a表示追加内容
2.打开文件后记得关闭

'''
