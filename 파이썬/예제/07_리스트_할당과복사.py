# 리스트 할당
a = [1, 2, 3, 4, 5]
b = a
print(a is b)

b[0] = 10
print(a) # a도 같이 변함



# 리스트 복사 : copy() 이용
a = [1, 2, 3, 4, 5]
b = a.copy()
print(a is b)

b[0]
print(a) # a 는 그대로 



# 리스트 다차원 복사 : copy.deepcopy() 이용
## copy()를 사용했을 때
a = [[1, 2], [3, 4], [5, 6]]
b = a.copy()
b[0][0] = 10
print(a) # a 가 복사되지 않음

## copy.deepcopy()를 사용했을 때
import copy
a = [[1, 2], [3, 4], [5, 6]]
b = copy.deepcopy(a)
b[0][0] = 10
print(a) # a 가 복사됨
