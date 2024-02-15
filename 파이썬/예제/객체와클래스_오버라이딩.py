# 오버라이딩 : 부모의 기능을 물려받고 일부기능 수정

# 부모클래스
class Animal:
    def __init__(self):
        self.hungry = 0
    def eat(self): # 수정 전
        self.hungry -= 10
        print("밥먹음", self.hungry)
    def walk(self):
        self.hungry += 10
        print("산책", self.hungry)

# 자식클래스
class Dog(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        print("멍멍")
    def eat(self): # 수정 후 
        super().eat()
        print("왈왈")


dog = Dog()
dog.eat()