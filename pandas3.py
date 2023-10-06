# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:56:47 2023

@author: navvn
"""

import pandas as pd


df=pd.DataFrame([[10,20,30,40],[7,14,21,28],[55,15,8,12],[15,14,1,8],[7,1,1,8],[5,4,9,2]],columns=['apple','orange','banana','pear'],index=['basket1','basket2','basket3','basket4','basket5','basket6'])

print("\n----------minimum--------\n")
print(df[['apple','orange','banana','pear']].min())

print("\n----------maximum--------\n")
print(df[['apple','orange','banana','pear']].max())

print("\n----------standard deviation--------\n")
print(df[['apple','orange','banana','pear']].std())

print("\n----------mean--------\n")
print(df[['apple','orange','banana','pear']].mean())

print("\n----------variance--------\n")
print(df[['apple','orange','banana','pear']].var())

print(df)
print(df.shape)
print(df.describe())
print(df.info())
print(df.head())
print(df.tail())



