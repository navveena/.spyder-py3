# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:28:00 2023

@author: navvn
"""

import pandas as pd

raw={
     'name':['darell','darell','lilith','lilith','tran','tran','tran','tran','john','darell','darell','darell'],
     'position':[2,1,1,4,2,4,3,1,3,2,4,3],
     'year':[2009,2010,2009,2010,2010,2010,2011,2012,2011,2013,2013,2012],
     'marks':[408,398,422,376,401,380,396,388,356,402,368,378]}

df=pd.DataFrame(raw)

group=df.groupby('year')
print(group.get_group(2011))

import pandas as pd

d={
   'subject_id':['1','2','3','4','5'],
   'student_name':['mark','khalid','deborah','trevon','raven']}

df1=pd.DataFrame(d,columns=['sunject_id','student_name'])
print(df1)


import pandas as pd

data={  'subject_id':['4','5','6','7','8'],
  'student_name':['eric','imani','cece','darius','andre']
      }

df2=pd.DataFrame(data,columns=['sunject_id','student_name'])
print(df2)

pd.merge(df1,df2,on='subject_id')


