# 정적 메서드 : 클래스 레벨에서 호출되며, 클래스나 인스턴스의 어떤 속성에도 접근하지 않음
# 클래스 메서드 : 클래스 메서드는 첫 번째 인자로 클래스 자신을 받음(cls). 이를 통해 클래스 속성에 접근


class Animal:
    type = "동물"

    @staticmethod
    def getType1():
        return Animal.type

    @classmethod
    def getType2(cls):
        return cls.type

    def __init__(self):
        self.hungry = 0


class Dog(Animal):
    type = "강아지"

    def __init__(self):
        super().__init()
    def sound(self):
        print("멍멍")


print(Dog.getType1())
print(Dog.getType2())
