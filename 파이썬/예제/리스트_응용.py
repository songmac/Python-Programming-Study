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
## 문자를 리스트로 만들기
fruit = "사과,배,옥수수,당근"
fruit_list = fruit.split(",")
print(fruit_list)

## 리스트를 문자로 만들기
fruit_list = ['사과','배','옥수수','당근']
fruit= "".join(fruit_list)
print(fruit)

fruit_list = ['사과','배','옥수수','당근']
fruit= " ".join(fruit_list)
print(fruit)

fruit_list = ['사과','배','옥수수','당근']
fruit= ",".join(fruit_list)
print(fruit)



