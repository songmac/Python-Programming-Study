# 리스트의 가장큰수 가장작은수 구하기
a = [32, 45, 2, 5, 76]

## 기본 : 가장작은수
small = a[0]
for i in a:
    if i < small:
        small = i
print(small)

## 기본 : 가장큰수
large = a[0]
for i in a:
    if i > large:
        large = i 
print(large)

## sort를 이용하여 구하기
a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])

## 함수를 이용하여 구하기
print(min(a))
print(max(a))



# 합계구하기
a = [32, 45, 2, 5, 76]
b = 0 

## 기본
for i in a:
    b += i
print(b)

## 함수를 이용하여 구하기
print(sum(a))




# split, join 함수