# 전역변수(global variable)와 지역변수(local variable)


## 경우 1
a = 5 # 전역변수

def func1():
    a = 1 # func1 에서만 사용
    print(a)

func1() # 1 출력
print(a) # 5 출력



## 경우 2
a = 5 # 전역변수

def func2():
    print(a)

func2() # 5 출력



## 경우 3
a = 5 # 전역변수

def func3():
    global a # 전역변수 사용
    a = 1 # 전역변수 변경
    print(a)

func3() # 1 출력
print(a) # 1 출력

