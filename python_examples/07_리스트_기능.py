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
print("b에 5라는 값이 있는 지 확인:", 5 in b)

print("리스트 a와 b 더하기:", a+b)
print("리스트 a와 b를 더한 길이:", len(a+b))



a.index(22) # 기능을 안함
print("특정 값의 인덱스 구하기: " , a)

a.count(2) # 기능을 안함
print("특정 값의 개수 구하기: ", a)



a.reverse()
print("순서 뒤집기: ", a) 
a.sort()
print("오름차순 정렬하기: ", a)
a.sort(reverse=True)
print("내림차순 정렬하기: ", a)
