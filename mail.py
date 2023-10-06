# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:17:42 2023

@author: navvn
"""

import pandas as pd

df=pd.read_csv("c:\\iris.csv")
pd.set_option('display.max_rows',None)
print(df)


"""

pd.set_option('display.max_columns',None) # or 1000
pd.set_option('display.max_rows',None) # or 1000
pd.set_option('display.max_colwidth',-1) # or 199

"""