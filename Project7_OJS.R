# Project7 OJS ####
# 22.01.10(월)

  # 환경설정
rm(list=ls())
getwd()
setwd('c:/rwork')

  # 라이브러리 모음
install.packages("data.table") #copy()

library(data.table)


# 공통 데이터
data1 <- array(c(1.5, 4, 2, 3))
data2 <- array(c(1:8),c(1,4,2))


# 11. sort(numpy)
data1
x11 <- sort(data1)
x11




# 12. append(numpy)
x12 <- data1
x12
x12 <- append(x12,data2)
x12




# 13. delete(numpy)
data2
data2[,,-1]
t(data2[,-c(2,4),]) #? 차원이 추가되면 전치행렬로 결과를 출력함
data2[!data2 %in% c(1,3,5)] #? 차원 유지 가능?


# 14. copy(numpy)
x = data1
y = copy(x)

x == data1
y == data1

x = data2
x == data1 # 변수내용이 data2로 바뀌자 오류발생
y == data1 # 얕은 복사를 했기때문에 x의 내용변경과는 무관




# 15. arange(numpy)
# r에서 range함수는 단지 최대 최소값만을 나타낸다.
range(1,3,6)
range(1.0:3.0,0.1)

# 파이썬과 같이 정해진 규칙으로 배열을 생성하려면 seq를 이용한다.
seq(1,3,by=1)
seq(1.0,3.0,by=1.0) # 소수단위는 생성하지 않는다.
seq(3.0,6.5) # by옵션 미설정시 기본값은 1이다.
seq(3,6,2)




# 16. read_csv(pandas)
read.csv('c:/rwork/test.csv')




# 17. unique(numpy)
names = c('Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe')
unique(names)
ints = c(3, 3, 3, 2, 2, 1, 1, 4, 4)
unique(ints)




# 18. dtype(numpy)
mode(data1)
mode(data2)
typeof(data1)
typeof(data2)




# 19. empty(numpy/pandas)
array(rep(0,10))
array(0,dim = c(3,6))
# zeros와 같은 기능은 있으나 empty와 같이 메모리 최적화를 위해 쓰레기값을 
# 넣어 배열을 만드는 함수는 발견되지 않음




# 20. dataframe(pandas)
dataframe1 <- as.data.frame(data1)
dataframe1
dataframe2 <- as.data.frame(data2)
dataframe2
## 파이썬과는 다르게 2차원의 배열을 1차원으로 묶어서 데이터 프레임을 형성하였다.
