# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:28:37 2023

@author: navvn
"""

import numpy as np

arr1=np.array([1,2,3,4,5,6,7,8,9])
res=np.square(arr1)
print(res)


import numpy as np
arr1=np.array([[36,25,49],[16,64,81]])
res=np.sqrt(arr1)
print(res)



import numpy as np

arr1=np.array([[36,25,49],[16,64,81]])
res=np.square(arr1)
print(res)
new_res=np.sum(res)
print(new_res)

"""
we have created a numpy array using the function np.array and square the values of the given array after that use lin .alg. norm function to calculate the size of the vector.
"""

import numpy as np

arr=np.array([[2,4,6],[2,2,3]])

e=np.square(arr)
print(e)
d=np.linalg.norm(e,ord=1,axis=1)
print(d)