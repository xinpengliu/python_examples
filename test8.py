#!/usr/bin/python
s=input("input your age:")
if s=="":
	raise Exception("input must no be empty.")

try:
	i=int(s)
except Exception as err:
	print(err)

finally:#clean up action
	print("goodbye!")
