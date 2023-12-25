# 리스트, 튜플 : 시퀀스 자료형 : 연속된 여러값들을 한 변수에 저장

a = list(range(-10, 10, 2))
b = list(range(5, 0, -1))

print("리스트 a 정의:", a)
print("리스트 a를 튜플로 변환:", tuple(a))

print("리스트 b 정의:", b)
print("리스트 b의 -1번째 인덱스의 값:", b)
print("b[:3] 값: ", b)
print("b[3:] 값: ", b)

del b[1:2]
print("b[1:2] 삭제: ", b)
print("b*3 결과: ", b*3)
print("b에 4라는 값이 있는 지 확인:", 4 in b)
print("b에 5라는 값이 있는 지 확인:", 4 in b)

print("리스트 a와 b 더하기:", a+b)
print("리스트 a와 b를 더한 길이:", len(a+b))


a.append(20)
print(a)
a.extend([22,25])
print(a)

a.pop(0) # () 안의 인덱스에 해당하는 요소 삭제
print(a)
a.pop() # 맨 마지막 요소 삭제
print(a)

a.insert(0, 100) # insert(인덱스, 값) # 특정 인덱스에 해당하는 요소 추가
print(a)
a.remove(100) # 요소 삭제
print(a)
a.index(-8) # 특정 요소의 인덱스 구하기
print(a)

a.count(2) # 특정 요소의 개수 구하기
print(3)

a.reverse() # 순서 뒤집기
print(a) 
a.sort() # 오름차순 정렬하기
print(a)
a.sort(reverse=True) # 내림차순 정렬하기
print(a)
