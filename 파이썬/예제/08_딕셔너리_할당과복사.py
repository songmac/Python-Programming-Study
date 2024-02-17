# 딕셔너리 복사 : copy()
a = {"a":0, "b":1}
b = a.copy()
print(a)
print(b)

# 중첩 딕셔너리의 경우 : deepcopy()
import copy
a = {"a":{"c":0,"d":0}, "b":{"e":0, "f":0}}
b = copy.deepcopy(a)
b.update({"b":{"g":1, "h":1}})
# b.update({"g":1, "h":1}) # 기존에 없었던 값, 추가하기 기능으로도 이용
print(a)
print(b)
