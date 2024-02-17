# 재귀함수 : 함수안에서 자기자신을 호출하는 방식
def test():
    print("재귀함수!")
    test()

# test()
# RecursionError: maximum recursion depth exceeded 
# (continue) while calling a Python object
# 라는 문구와함께 재귀의 깊이가 일정 길이를 초과하면 오류가 남



# 재귀함수 종료조건
def test(end):
    if end == 0:
        return
    print("재귀함수")
    end -= 1
    test(end)

test(5)



# 재귀호출로 팩토리얼 구하기
def factorial(n):
    if n == 1:
        return 1
    
    return n*factorial(n-1)

print(factorial(5))