#!/usr/bin/python
#-*- coding:utf8 -*-
word="abcdefg"
a=word[2]
print("a is:"+a)
b=word[1:3]
print("b is:"+b)
c=word[:2]
print("c is:"+c)
d=word[0:]
print("d is:"+d)
e=word[:2]+word[2:]
print("e is:"+e)
f=word[-1]
print("f is:"+f)
g=word[-4:-2]
print("g is:"+g)

h=word[-2:]
print("h is:"+h)
i=word[:-2]
print("i is:"+i)
l=len(word)
print("length of word is:"+str(l))


s=input("input your name:")
print("your name is:"+s)
l=len(s)
print("you name lengthis:"+str(l))


'''
知识点：
类似java，在python3里所有字符串都是unicode 所以长度一致


'''
