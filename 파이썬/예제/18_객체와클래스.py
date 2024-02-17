# 객체 : 속성(변수, instance)과 행동(함수, method)으로 구성된 대상
# 클래스 : 객체를 만들기 위한 도구(문법)

class Dog:
    def __init__(self, name, color): #생성자 함수
        self.hungry = 0 # 인스턴스 속성
        self.name = name
        self.color = color
    def eat(self): # 인스턴스 매서드
        self.hungry -= 10
        print("밥먹음", self.hungry)
    def walk(self):
        self.hungry += 10
        print("산책", self.hungry)


choco = Dog("choco", "black")
jjong = Dog("jjong", "white")

choco.eat()
choco.eat()
choco.walk()
print(choco.hungry)
print(jjong.hungry)