#!/usr/bin/python
#-*- coding:utf8 -*-
#列表类似JavaScript的数组，方便易用

#定义元组
word=['a','b','c','d','e','f','g']

#如何通过索引访问元组里面的元素
a=word[2]
print("a is :"+a)
b=word[1:3]
print("b is:")
print(b)#index 1 and 2 elements of word
c=word[:2]
print("c is :")
print(c)#index 0 and 1 elements of word
d=word[0:]
print("d is:")
print(d)#all elements of word


#元组可以合并
e=word[:2]+word[2:]
print("e is:")
print(e)#all elements of word
f=word[-1]
print("f is:")
print(f)#the last elements of word
g=word[-4:-2]
print(g)#index 3 and 4 elemnts of word
h=word[-2:]
print("h is :")
print(h)#the last two elements
i=word[:-2]
print("i is:")
print(i)#everthing except the last two characters
l=len(word)
print("length of word is:"+str(l))
print("adds new element")
word.append('h')
print(word)

#delete element
del word[0]
print(word)
del word[1:3]
print(word)

'''
知识点：
1.列表长度是动态的，可以任意添加和删除元素；
2.用索引可以很方便访问元素，甚至返回一个列表；
3.更多方法可以参考python的帮组文档
'''



