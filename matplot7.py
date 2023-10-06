# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:21:15 2023

@author: navvn
"""


import matplotlib.pyplot as plt

apple=[100,200,300,306,400]

plt.boxplot(apple)

plt.show()

plt.boxplot(apple,showmeans=True,notch=True)
plt.show()

plt.boxplot(apple,showmeans=True,notch=False)

plt.show()
