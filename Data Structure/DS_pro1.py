# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:09:04 2019

@author: My Laptop
"""

'''file = open("in.txt","w") 
 
file.write("10000") 
file.write("first fit") 
file.write("allocate(500,m1)") 
file.write("allocate(5000,m2)") 
file.write("allocate(200,m3)")
file.write("free(m2)")
file.write("allocate(400,m4)")
 
file.close()'''
import re
class Node:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        self.next = None
        
file = open("in.txt","r") 
x=file.readlines()
n=len(x)
size= int(x[0])
mode=x[1]
memory=Node(0,size)

for i in range(3,n+1):
    list=[int(s) for s in re.findall( r'\d+',x[1])]
    if len(list)==2:s
        free()
    
    
