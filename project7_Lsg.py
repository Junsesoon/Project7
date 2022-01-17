## Project7
# Numpy/Pandas 와 R 비교

# 환경설정
import numpy

all = [var for var in globals() if var[0] != "_"]
for var in all:
    del globals()[var]

import numpy as np
import pandas as pd

# 공통 데이터
data1 = [1.5, 4.0, 2.0, 3.0]
data1
data2 = [[1, 2, 3, 4],[5, 6, 7, 8]]
data2

# 1. empty(numpy)
data1 = np.empty((2, 2)) # 2*2 배열함수 생성 함수
data1
np.empty((2, 4, 5))

# empty(pandas)
df_empty = pd.DataFrame({'A' : []}) # 인덱스가 비어있는것을 확인하는 함수
df_empty
df_empty.empty

df = pd.DataFrame({'A' : [np.nan]}) # 인덱스에 nan만 있으면 비어있는것으로 간주 하지 않는다.
df
df.empty
df.dropna().empty # NA를 삭제하면 인덱스가 비워진 상태로 출력

# 2. sum(numpy)
np.sum(data1) # 데이터 안에 들어있는 모든 원소의 합 추출 함수
np.sum(data2)
# sum(pandas)
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
              [np.nan, np.nan], [0.75, -1.3]],
                index=['a', 'b', 'c', 'd'],
                columns=['one', 'two'])
df

df.sum()
df.sum('index')
df.sum('columns') # nan = 0으로 자동변환

# 3. mean(numpy)
np.mean(data1) # 데이터 안에 있는 모든 원소의 평균
np.mean(data2)
# mean(pandas)
df
df.mean()
df.mean('index')
df.mean('columns')

# 4. zeros(numpy)
np.zeros(10) # 주어진 길이나 모양에 0이라는 값으로 배열 생성
np.zeros((3, 6))
np.zeros((2, 3, 2))
# zeros(pandas)
a = pd.DataFrame(np.zeros(10))
b = pd.DataFrame(np.zeros((3, 6)))
c = pd.DataFrame(np.zeros(2,3,2)) # 3차원 부터는 출력의 지원이 안된다.
print(a)
print(b)

# 5. var(numpy)
np.var(data1, ddof=1) # 데이터 안에 있는 원소들의 분산 값 / ddof=1 (표준편차를 계산할 때, n-1로 나누라는 의미)
np.var(data2, ddof=1) # https://www.abbreviationfinder.org/ko/acronyms/ddof.html#aim
# var(pandas)
df.var()
df.var('index')
df.var('columns')

# 6. min(numpy)
np.min(data1)
np.min(data2)
# min(pandas)
df.min()
df.min('index')
df.min('columns')

# 7. max(numpy)
np.max(data1)
np.max(data2)
# max(pandas)
df.max()
df.max('index')
df.max('columns')

# 8. cumsum(numpy)
np.cumsum(data1) # 데이터 안에 있는 원소들의 누적 합의 추출 함수 (sum과는 별개)
np.cumsum(data2)
# cumsum(pandas)
df
df.cumsum('index')
df.cumsum('columns')

# 9. random(numpy)
data = np.random.randn(2, 3) # 난수 생성
data

# random(pandas)
df1 = pd.DataFrame(np.random.randn(2, 3))
df1

# 10. sqrt(numpy)
np.sqrt(data1)
np.sqrt(data2)
# sqrt(pandas)
df.dropna(axis=0)
df.dropna(axis=1)
df.transform('sqrt')
