# 리스트 할당
a = [1, 2, 3, 4, 5]
b = a
print(a is b)

b[0] = 10
print(a)

# 리스트 복사 : copy() 함수 사용
a = [1, 2, 3, 4, 5]
b = a.copy()
print(a is b)

b[0]
print(a)