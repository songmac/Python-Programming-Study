# 딕셔너리 기본
score = {"name":"Tom", "math":80, "english":70}

print(score["name"])

score["name"] = "Michael"
print(score["name"])


# 딕셔너리 타입
print(type(score))


# 딕셔너리 기능
## 키의 개수
print(len(score))

## 키가 있는지 확인
print("math" in score)
print("age" in score)

## 키-값 쌍 추가하기 : setdefault(키, 값)
score.setdefault("age", 20)
print(score)

## 키-값 수정하기 : update({키: 값}) 
score.update({"math":90})
print(score)


## 모든 키, 값 가져오기
print(score.keys()) # 결과 : dict_keys(['name', 'math', 'english', 'age'])

print(score.values()) # 결과 : dict_values(['Michael', 90, 70, 20])

print(score.items()) # 결과 : dict_items([('name', 'Michael'), ('math', 90), ('english', 70), ('age', 20)])


## 키로 딕셔너리 항목 삭제 : pop(키, 기본값)
score.pop("name")
print(score)
score.pop("age")
print(score)

# 모든 값 삭제 : clear()
score.clear()
print(score)

