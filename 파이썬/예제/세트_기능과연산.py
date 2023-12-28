# 기본
animal = {"dog", "cat", "monkey", "horse"}
print(type(animal))



# 기능
## 특정값 확인
print("cat" in animal)

## 세트 만들기
a = set("animal")
b = set("fish")
c = set("ABCDEF")
d = set(range(1,6,1))
e = {10, 20, 30}
f = {30, 40, 50}
print(a, b, c)
print(d, e, f)

## 추가하기
a.add("world")
print(a)
f.add(2030)
print(f)

## 삭제하기
a.remove("a")
a.discard("i")
print(a)



# 연산
## 합집합 : union
print(a|b)
print(set.union(a,b))

## 교집합 : intersection
print(e&f)
print(set.intersection(e,f))

## 차집합 : difference
print(e-f)
print(set.difference(e,f))

## 대칭차집합 : 교집합의 여집합
print(e^f)
print(set.symmetric_difference(e,f))

## 부분집합 : issubset
print(d <= {1, 2, 3})
print(d.issubset({1, 2, 3}))

## 상위집합 : issuperset
print(d >= {1, 2, 3})
print(d.issuperset({1, 2, 3}))

## 겹치는 요소가 없는지 확인(부정문) : 겹치지 않으면 True, 겹치면 False
print(d.isdisjoint({6, 7, 8, 9, 10}))
print(e.isdisjoint({6, 7, 8, 9, 10}))


