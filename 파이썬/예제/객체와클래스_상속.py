# 상속 : 공통되는 내용은 부모 클래스로 만들고 클래스(자식)를 만들때 공통되는 내용을 부모클래스로부터 상속

# 예시

"""
    
class 부모클래스 :
    코드

class 자식클래스(부모클래스명):
    코드
    
"""

# 부모 클래스
class Animal:
    def __init__(self):
        self.hungry = 0
    def eat(self):
        self.hungry -= 10
        print("밥먹음", self.hungry)
    def walk(self):
        self.hungry += 10
        print("산책", self.hungry)

# 자식 클래스
class Dog(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        print("멍멍")

class Cat(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        print("야옹")


dog = Dog()
dog.sound()
dog.walk()
dog.walk()


cat = Cat()
cat.sound()
cat.walk()