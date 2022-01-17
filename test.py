import numpy as np

array2 = np.array([[1,2,3],
                   [4,5,6]])
array2

print('array 2의 타입은:', type(array2))

random_array = np.random.randn(3, 3) # 3by3 생성
print("무작위 3by3행렬 만들기 : \n",random_array)



seq_array = np.arange(10)
print(seq_array)
print(seq_array.dtype,seq_array.shape,seq_array.size)