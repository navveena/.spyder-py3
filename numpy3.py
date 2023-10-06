# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:00:01 2023

@author: navvn
"""

"""standard deviation is a number that describes how spread out the values are.

a low standard deviation means that most of the numbers are close to the mean (average value)

a high standard deviation means that the values are spread out over a wider rage.


"""
import numpy
age1=[100,105,98,97,90]
age=[34,12,43,23,42,78,54]

x=numpy.std(age)
x1=numpy.std(age1)
print(x1)

print(x)

x=numpy.var(age)
print(x)