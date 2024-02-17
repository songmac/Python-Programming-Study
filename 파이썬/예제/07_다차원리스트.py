# 2차원 리스트 선언
a = [[10,20], [30,40], [50,60]]
print(a)

a = [[10,20], 
     [30,40], 
     [50,60]]
print(a)

print(a[0][0])
print(a[0][1])
print(a[1][1])



# 2차원 리스트 값추가
a = [[10,20], [30,40], [50,60]]
a[0].append(10)
print(a)
a[1].append(20)
print(a)
a[2].extend([1,2])
print(a)

print()


# 2차원 리스트 값 출력
## for문 사용
a = [[10,20], [30,40], [50,60]]
for x, y in a:
    # print(x)
    # print(y)
    print(x,y)


## 이중 for문 사용
a = [[10,20], [30,40], [50,60]]
for i in a:
    for j in i:
        print(j, end=' ')
    print()

## for와 range 사용
a = [[10,20], [30,40], [50,60]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()

## for와 enumerate 사용
a = [[10,20], [30,40], [50,60]]
for idx, val in enumerate(a):
    for idx2, val2 in enumerate(val):
        print(idx, idx2, val2)


# 2차원 리스트 만들기
a = []
for i in range(3):
    temp = []
    for j in range(2):
        temp.append(0)
        a.append(temp)
print(a)