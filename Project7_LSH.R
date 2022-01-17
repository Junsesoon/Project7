# 임성현

# 공통데이터
a = c(1,2,3)
b = c(4,5,6)
df = data.frame(a, b)
df
c = c(1,2,NA,4)

#21 ndim ; 차원만 따로 보여주는 기능을 못찾아서 dim으로 대체
dim(df)

#22 size
nrow(df)*ncol(df)

#23 values
array(c(a,b), dim = c(3,2,1))

#24 head
head(df)

#25 tail
tail(df)

#26 shape
dim(df)

#27 T
t(df)

#28 describe
summary(df)

#29 notnull
na.omit(c)

#30 get_dummies
table(df$a)





