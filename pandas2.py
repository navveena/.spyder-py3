# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:46:51 2023

@author: navvn
"""

import pandas as pd
import numpy as np
info=np.array(['c','a','d','d','c','a','e'])
a=pd.Series(info)
print(a)


import pandas as pd
#a list of strings
x=['sundara','pandian','caddcae']

#calling dataframe constructor on list
df=pd.DataFrame(x)
print(df)


import pandas as pd
import numpy as np
d1={'x':0.,'y':1.,'z':2.}
a=pd.Series(d1)
print(a)