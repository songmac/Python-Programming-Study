# 어떠한 코드를 반복해야 할 때 사용 (지정된 범위만큼)

# 숫자 반복
i_list = []
for i in range(0, 10):
    i_list.append(i)
    print(f"{i}번째 i출력 후 리스트에 추가: ", i_list)

j_list = []
for j in range(10, 0, -1):
    j_list.append(j)
    print(f"{j}번째 j출력 후 리스트에 추가: ", j_list)



# 다양한 자료형으로의 반복 : range함수는 int형 반복에만 사용, 그 외에는 in 구문 사용
# 문자형
for i in "Orange":
    print(i, end=" ")
print()

## 딕셔너리
a = {"name":"tom", "math":80, "english":70}
for i in a:
    print(i, end=" ") # key 출력
    print(a[i]) # value 출력

## 리스트
### 반복문으로 리스트 요소 출력
a = [1, 2, 3, 4, 5, 6, 7]
for i in a :
    print(i)

### enumerate 사용하여 index 접근
a = [1, 2, 3, 4, 5, 6, 7]
for idx, val in enumerate(a):
    print(idx, val, sep=",")



# 입력한 횟수만큼 반복
count = int(input("반복할횟수: "))
for i in range(count):
    print("바보", i)


# 반복문 중첩
for i in range(1, 6):
    print("********************", i)
    for j in range(1, 6):
        print("j: ", j)



