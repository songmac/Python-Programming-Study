# pickle 모듈을 이용하여 리스트를 파일에 저장
import pickle
    
text = ["First File", "Second Line"]

with open("data.p", "wb") as file:
    pickle.dump(text, file)



# pickle 모듈을 이용하여 리스트를 파일에서 불러오기
import pickle

with open("data.p", "rb") as file :
    data = pickle.load(file)

print(data)
