# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:40:29 2023

@author: navvn
"""

import pandas 
import matplotlib.pyplot as plt
import matplotlib.colors
url="https://raw.githubsercontent.com/jbrownlee/datasets/master/iris.csv"
names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=pandas.read_csv(url,names=names)
print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
#class distribution
print(dataset.groupby('class').size())
dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
plt.show()
dataset.hist()
plt.show()