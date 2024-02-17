# 람다표현식 : 익명함수를 만드는 방법
# (계속) 함수를 간단하게 작성할 수 있어 다른 함수의 인수로 넣을때 주로 사용


## 일반적인 함수표현
def plus_ten(x):
    return x + 10
print(plus_ten(1))



## 람다 표현식(1)
plus_ten = lambda x:x+10
print(plus_ten(1))



## 람다 표현식(2) : 바로 호출하기
print((lambda x:x+10)(1))



## 람다 표현식(3) : 람다표현식 내에 변수는 사용할 수 없지만 바깥에 있는 변수는 사용가능
y = 10
print((lambda x:x+y)(1))

