# 키워드 인수 & 딕셔너리 언패킹

def func(email, name):
    print("이메일 : ", email, end="")
    print(", 이름 : ", name)

func(email = "aa@aa.com", name = "tom")

x = {"email" : "bb@bb.com", "name" : "michael"}
func(**x)



# 가변 키워드인수
def func(**kwargs):
    print("이메일 : ", kwargs["email"], end="")
    print(", 이름 : ", kwargs["name"])

func(email = "cc@cc.com", name = "drake")