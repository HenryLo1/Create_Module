# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:47:09 2019

@author: henry
"""

def count(list1):
    return (len(list1))

def add(list2):
    sum =0
    for i in list2:
        sum += i
    return sum

def average(list3):
    sum = 0 
    for i in list3:
        sum += i
    return sum/(len(list3))

def maximum(list4):
    return (max(list4), list4.index(max(list4)))

def minimum(list5):
    return (min(list5), list5.index(min(list5)))


#l=[1,2,3]
#print(count(l))
#print(add(l))
#print(average(l))
#print(maximum(l))
#print(minimum(l))