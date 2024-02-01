# 함수 : 특정한 기능을 반복해서 사용해야 할 때 사용

# 함수의 구조
def func(a,b): # func은 함수 이름 # a,b는 인자(parameters) # 실제 전달되는 값은 argument라고 함
    # print("함수입니다.") # 코드블럭
    return a+b # 반환 값

func_test = func(1,2)
print(func_test)

# 다양한 형태로 작성 가능한 함수
## 인자와 반환 값이 없는 함수
def func1():
    print("Hello, Function")
func1()

## 인자는 있으나 반환 값이 없는 함수
def func2(name):
    print("Hello, " + name)
func2("spring")

## 인자와 반환 값이 있는 함수
def func3(a,b):
    return a+b
print(func3(10,10))

def func4(a,b):
    return a+b, a-b
print(func(10,5))
