import pandas as pd1

df=["orange","apple","mango"]

df1=pd1.DataFrame(df)

print(df1)
print(type(df1))
print(df1.info())
print(df1.shape)
print(df1.describe())

import pandas as pd

s1=pd.Series([1,2,3,4,5])

print(s1)

print(type(s1))