# pickle 모듈을 이용하여 다양한자료형 저장하기
import pickle

name = "tom"
age = 24
address ="서울시 마포구"
scores = {"python":90, "deeplearning":95, "database":85}

with open("data2.p", "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)



# pickle 모듈을 이용하여 다양한자료형 불러오기
import pickle

with open("data2.p", "rb") as file:
    name2 = pickle.load(file)
    age2 = pickle.load(file)
    address2 = pickle.load(file)
    scores2 = pickle.load(file)

print(name2)
print(age2)
print(address2)
print(scores2)

