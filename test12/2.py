#!/usr/bin/python
#-*- coding:utf8 -*-
import os.path

#常用函数有三种：分割路径，找出文件名，找出盘符，找出文件的扩展名
#根据实际情况修改下面的参数
spath="/opt/BIN/0106.log"

#case 1:
p,f=os.path.split(spath);
print("dir is:"+p)
print("file is:"+f)

#case 2:
drv,left=os.path.splitdrive(spath)
print("driver is:"+drv)
print("left is:"+left)

#case 3:
f,ext=os.path.splitext(spath)
print("fis is:"+f)
print("ext is:"+ext)


'''
知识点：这三个函数返回二元组
case1 分割目录和文件名
case2 分割盘符和文件名
case3 分割文件和扩展名
'''
