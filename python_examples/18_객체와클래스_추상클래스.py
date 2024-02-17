# 추상클래스(abstract class) : 상속받는 클래스의 메서드 구현을 강제
# 사용하는 이유? 추상클래스를 사용하는 주된 이유는 다형성(polymorphism)을 지원하고, 상속받는 클래스들이 일관된 인터페이스를 따르도록 강제하기 위함
# (계속) 이를 통해 코드의 유지보수성과 확장성이 향상


# 부모클래스
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self):
        self.hungry = 0

    @abstractmethod
    def sound(self):
        pass

    def eat(self):
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
        super().walk()
        print("멍멍")

    def eat(self):
        super().eat()
        print("왈왈")  # Dog 클래스의 추가적인 동작을 나타냄



dog = Dog()
dog.sound()
dog.eat()