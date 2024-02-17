# 파이썬의 객체지향 프로그래밍 개념


"""
1. 클래스 속성 (Class Attribute)
클래스 속성은 클래스의 모든 인스턴스에서 공유되는 속성. 이는 모든 객체에 공통적인 값을 저장하는 데 유용.

예시: 모든 직원이 속한 회사 이름을 저장.


class Employee:
    company = "Samsung"  # 클래스 속성

    def __init__(self, name):
        self.name = name  # 인스턴스 속성

# 모든 직원 객체는 동일한 회사 이름을 공유
emp1 = Employee("Alice")
emp2 = Employee("Bob")
print(Employee.company)  # "Samsung"



2. 정적 메서드 (Static Method)
정적 메서드는 인스턴스나 클래스 상태에 접근하지 않는 메서드. 유틸리티 함수를 클래스 내부에 정의할 때 사용.

예시: 유효한 이메일 주소인지 검증하는 함수

class User:
    @staticmethod
    def is_valid_email(email):
        return "@" in email

print(User.is_valid_email("test@example.com"))  # True



3. 클래스 메서드 (Class Method)
클래스 메서드는 클래스 상태에 접근할 수 있으며, 첫 번째 매개변수로 클래스 자신(cls)을 받음. 클래스 속성을 수정하는 데 사용.

예시: 직원 수를 추적합니다.

class Employee:
    num_employees = 0  # 클래스 속성

    def __init__(self, name):
        self.name = name
        Employee.num_employees += 1

    @classmethod
    def total_employees(cls):
        return cls.num_employees

emp1 = Employee("Alice")
emp2 = Employee("Bob")
print(Employee.total_employees())  # 2



4. 비공개 속성 (Private Attribute)
비공개 속성은 클래스 외부에서 접근할 수 없는 속성. 클래스 내부의 메서드에서만 사용.

예시: 비밀번호를 안전하게 저장합니다.

class Account:
    def __init__(self, password):
        self.__password = password  # 비공개 속성

    def verify_password(self, password):
        return self.__password == password



5. 추상 클래스 (Abstract Class)
추상 클래스는 하나 이상의 추상 메서드(구현되지 않은 메서드)를 가진 클래스. 상속받는 자식 클래스에서 해당 메서드들을 구현하도록 강제.

예시: 다양한 종류의 도형을 그리는 클래스

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("원을 그립니다.")

class Rectangle(Shape):
    def draw(self):
        print("사각형을 그립니다.")



실무에서는 이러한 개념들을 통해 코드의 재사용성을 높이고, 
유지보수를 용이하게 하며, 더 안전하고 명확한 인터페이스를 제공.

"""