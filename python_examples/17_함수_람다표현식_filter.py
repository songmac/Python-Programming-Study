# filter : 반복되는 자료형의 값들을 함수를 이용하여 참인 것만 걸러냄

a = [2, 6, 4, 3, 6, 8, 3, 9, 6]
result = list(filter(lambda x: x>2 and x<8, a))
print(result)
