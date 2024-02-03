# 인자값에 리스트 사용 (언패킹)
def func(a,b,c):
    print(a,b,c)
x = [1,2,3]
func(*x)



# 가변인수
def func(*args):
    for arg in args:
        print(arg)
func(1)
func(1,2,3,4,5) 



# 가변인수와 고정인수 같이사용 (함수의 가독성, 변수 설정 의도 명확히 제공)
## 이점 : 고정인수를 지정하여 명확한 변수 설정이 가능
## (계속) 가변 인수를 지정하면 추가 인수를 받을 수 있어, 더 유연한 함수 설계가 가능
def concat(base_str, *words):
    result = base_str
    for word in words:
        result += word
    return result

print(concat("Hello"))
print(concat("Hello", " ", "World"))
print(concat("Base", "String", "With", "Multiple", "Words"))
