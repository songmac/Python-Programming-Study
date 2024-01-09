# 리스트 컴프리핸션(list comprehension) 
## for문 : 식 for 변수 in 리스트
a = [i for i in range(10)]
print(a)

a = [i+5 for i in range(10)]
print(a)

a = [i*3 for i in range(10)]
print(a)


## if문 : 식 for 변수 in 리스트 if 조건
a = [i for i in range(10) if i % 2 == 0]
print(a)

a = [i for i in range(10) if i % 2 == 1]
print(a)



# 이중 for문 : 식 for 변수 in 리스트 for 변수 in 리스트 
a = [i * j for i in range(2, 10) for j in range(1, 10)] # 구구단
print(a)



# 리스트를 딕셔너리로 변경
keys = ["name", "age", "address"]
users = ["tom", "20", "incheon"]
dicdic = {keys[i]: users[i] for i in range(0, 3)}
print(dicdic)



# ZIP : zip(리스트1, 리스트2)
## 딕셔너리 만들기
keys = ["name", "age", "address"]
users = ["michael", "30", "seoul"]
dic = dict(zip(keys, users))
print(dic)

## 리스트 만들기
lis = list(zip(keys, users))
print(lis)
