#!/usr/bin/python
#-*- coding:utf8 -*-

import shutil
import os
import os.path

src="/opt/BIN/0106.log"
dst="/opt/BIN/0106-cpy.log"
dst2="/opt/BIN/0106-test.log"

dir1=os.path.dirname(src)
print("dir1:%s"%dir1)
if(os.path.exists(src)==False):
	os.makedirs(dir1)
f1=open(src,"w")
f1.write("line a\n")
f1.write("line b\n")
f1.close()

shutil.copyfile(src,dst)
shutil.copyfile(src,dst2)
f2=open(dst,"r")
for line in f2:
	print(line)
f2.close()

#复制文件夹树
try:
	srcDir="./testsrc"
	dstDir="./testdir"
	shutil.copytree(srcDir,dstDir)
except Exception as err:
	print(err)


'''
知识点：
1.shuttil.copyfile如何复制文件
2.os.path.exists如何判断文件夹是否存在
3.shutil.copytree如何复制目录树
'''

