## Project7
# Numpy/Pandas 와 R 비교

# 환경설정
all = [var for var in globals() if var[0] != "_"]
for var in all:
    del globals()[var]

import numpy as np

import pandas as pd

# 공통 데이터
data1 = [1.5, 4, 2, 3]
data1
data2 = [[1, 2, 3, 4],[5, 6, 7, 8]]
data2


# 11. sort(numpy)
data1
sortData1 = np.sort(data1)
sortData1

# 12. append(numpy)
## numpy append는 내장 append와는 다르게 차원의 수가 맞지 않으면 이어붙일 수 없다.
arr = np.array(
    [
        [
            [1, 1],
            [2, 2]
        ],
        [
            [3, 3],
            [4, 4]
         ]
    ])
    item = np.array([
        [5, 5],
        [6, 6]
    ]
)

print(arr.shape)
print(item.shape)

append1 = np.append(arr, item.reshape(1, 2), axis=0)
append2 = np.append(arr, item.reshape(1, 2, 2), axis=0)
print(append1)
print(append2)


# 13. delete(numpy)
# 형식) np.delete(arr, obj, axis=None)
# The axis along which to delete the subarray defined by obj.
# If axis is None, obj is applied to the flattened array.
arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
arr
np.delete(arr, 1, 0)
np.delete(arr, np.s_[::2], 1)
np.delete(arr, [1,3,5], None)



# 14. copy(numpy)
## 형식)np.copy(data, order='K', subok=False)
x = data1
y = np.copy(data1)

x == data1
y == data1

## np.copy는 얕은복사이기 때문에 x의 내용이 data2로 바뀌어도
 # 기존에 복사했던 data1의 데이터를 그대로 갖고 있는다.
x = data2
x == data1
y == data1




# 15. arange(numpy)
## 형식)numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
### 내장 함수인 range와 동일한 기능이지만, 결과는 list가 아닌 ndarray로 생성된다.
np.arange(3)
np.arange(3.0)
np.arange(3,7)
np.arange(3,7,2)




# 16. read_csv(pandas)
pd.read_csv('data1.csv')




# 17. unique(Numpy)(axis -> 변경)
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names) #dtype을 따로 표기해주는 이유: 숫자형이 아니기 때문으로 예상됨
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
np.unique(ints)



# 18. dtype(numpy)
# ndarray는 동종 데이터를 위한 일반 다차원 컨테이너이다.
# 즉, 모든 요소는 동일한 유형이어야 한다.
# 모든 배열은 모양, 각 차원의 크기를 나타내는 튜플 및 배열의 데이터 유형을 설명하는 객체인 dtype을 가진다.
npdata1 = np.array(data1)
npdata1.dtype
npdata2 = np.array(data2)
npdata2.dtype




# 19. empty(numpy/pandas)
# 새 메모리를 할당하여 새 배열을 생성한다.
# zeros와 달리 배열의 값들을 초기화 하지 않기 때문에 더 빠르지만,
# 메모리가 초기화되지 않고 할당되기 때문에 예상치 못한 값이 들어있을 수 있다.
## numpy
np.zeros(10)
np.zeros((3,6))
np.empty((2,3,4))

## pandas
df_empty = pd.DataFrame({'A' : []})
df_empty
df_empty.empty

### cf)NaN이 들어가 있을 경우 비어 있지 않은 것으로 간주한다.
dfNaN = pd.DataFrame({'A' : [np.nan]})
dfNaN
dfNaN.empty




# 20. dataframe(pandas)
# 형식)pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
## parameters
### data: ndarray, dict, dataframe
    # => data가 dict개체라면 열순서는 입력순서를 따른다.
### index: 결과에 사용할 인덱스. none으로 설정하면 데이터의 인덱싱 정보 부분 및 인덱스가 제공되지 않음
### columns: 데이터에 열 레이블이 없는 경우 결과 프레임에 사용할 열 레이블,
            # 범위 인덱스로 기본값 설정(0,1,2,...,n) 데이터에 열 레이블이 포함된 경우 대신 열 선택을 수행한다.
### dtype: 강제 적용할 데이터 유형. 단 하나의 타입만 허용된다.
### copy: true or false로 설정 가능하며, None의 기본값은 false이다.
pd.DataFrame(data1,index=(1,2,3,4), columns=None, dtype=None, copy=None)
pd.DataFrame(data2,index=(1,2), columns=None, dtype=None, copy=None)