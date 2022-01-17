# 비교 데이터 생성

# numpy 비교 데이터
data1 <- c(1.5, 4, 2, 3) 
data1

vec1 <- c(1:8)
data2 <- array(vec1, c(1, 4, 2))
data2


# pandas dataframe 비교 데이터
own <- c(1.4, 7.1, NA, 0.75)
two <- c(NA, -4.5, NA, -1.3)
df <- data.frame(own, two)
df
rownames(df) <- c('a', 'b', 'c', 'd')
df

# empty
install.packages('plyr') # empty함수를 쓰기 위한 패키지 설치
library(plyr)

# pandas 비교
empty(df)

# numpy 비교
empty(data1)
empty(data2) # 데이터 프레임이 비었는지 확인 하는 함수
# pandas의 empty의 함수와 동일하게 쓰인다.

# sum
# numpy 비교
sum(data1) # 데이터 안에 있는 모든 원소의 합
sum(data2)

# pandas 비교
sum(df$own, na.rm = T)
sum(df$two, na.rm = T)
rowSums(df, na.rm = T)
# numpy, pandas와 동일하게 쓰인다.

# mean
# numpy 비교
mean(data1) # 데이터 안에 있는 모든 원소의 평균
mean(data2)

# pandas 비교
mean(df$own, na.rm = T)
mean(df$two, na.rm = T)
rowMeans(df, na.rm = T)
# numpy, pandas와 동일하게 쓰인다.

# zeros
install.packages('phonTools')
library(phonTools)

zeros(10)
zeros(3, 6)
zeros(2, 3, 2) # 3차원 지원 출력이 안됨

# var
# numpy 비교
var(data1)
var(data2)

# pandas 비교
var(df$own, na.rm = T)
var(df$two, na.rm = T)
apply(df, 1, var, na.rm = TRUE)

# min
# numpy 비교
min(data1) # 데이터 안에 있는 원소중 제일 작은 값
min(data2)

# pandas 비교
min(df$own, na.rm = T)
min(df$two, na.rm = T)
apply(df, 1, min, na.rm = TRUE)

# max
# numpy 비교
max(data1) # 데이터 안에 있는 원소중 제일 큰 값
max(data2)

# pandas 비교
max(df$own, na.rm = T)
max(df$two, na.rm = T)
apply(df, 1, max, na.rm = TRUE)

# cumsum
# numpy 비교
cumsum(data1) # 데이터 안에 있는 원소들의 누적 합
cumsum(data2)

# pandas 비교 na값을 전처리 해야함 그래야 비교가능
is.na(df)
df1 <- na.omit(df)
cumsum(df1$own)
cumsum(df1$two)
apply(df1, 1, cumsum)
# numpy, pandas와 동일하게 쓰인다.

# random
rnorm(n=3, mean=0, sd=2)

# sqrt
# numpy 비교
sqrt(data1)
sqrt(data2)

# pandas 비교
sqrt(df$own)
sqrt(df$two)
apply(df, 1, sqrt)
