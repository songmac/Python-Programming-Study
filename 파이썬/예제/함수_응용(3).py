# 매개변수 초기값 설정, 변경
def func(email, name, age=20):
    print("이메일 : ", email, end="")
    print(", 이름 : ", name, end="")
    print(", 나이 : ", age)

func(email = "aa.aa.com", name = "tom")
func(email = "aa.aa.com", name = "tom", age = "18")