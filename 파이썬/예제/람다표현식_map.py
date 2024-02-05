# map : 반복되는 자료형의 값에 대해 함수를 이용하여 값을 가공 하는 것
# 형태 : map(function, variable of data type)

## 일반함수 사용
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def f(x):
    if x % 2 == 0:
        return 0
    
    else :
        return x

result = list(map(f,a))
print(result)


## 람다표현식 사용
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda x:0 if x%2 == 0 else x, a))
print(result)