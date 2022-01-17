import numpy as np
import pandas as pd


# 공통 데이터
data = {'a' : [1,2,3], 'b' : [4,5,6]}
c = pd.Series([1,2,pd.NA,4], index=(1,2,3,4))
print(c)
print(data)


df = pd.DataFrame(data, index=(1,2,3))
print(df)

#21. ndim (pandas)
print(df.ndim)

#22. size (pandas)
print(df.size)

#23. values (pandas)
print(df.values)

#24. head (pandas)
print(df.head())

#25. tail (pandas)
print(df.tail())

#26. shape (pandas)
print(df.shape)

#27. T(Transpose) (pandas)
print(df.T)

#28. describe (pandas)
print(df.describe())

#29. notnull (pandas)
print(c[c.notnull()])

#30. get_dummies()
pd.get_dummies(df['a'])