# 정적 메서드(static method, class method) : 객체없이 클래스명으로 접근가능
# (계속)인스턴스 속성, 인스턴스 메서드 접근 불가

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

class Calc:
    @classmethod
    def add(cls,a,b):
        print(a+b)


Calc.add(10,20)
Calc.add(30,40)