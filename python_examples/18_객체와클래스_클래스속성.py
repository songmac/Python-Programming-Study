# 클래스 속성 (class attribute) : 모든 객체(인스턴스)가 공유하는 속성. 객체없이 클래스명으로 접근 가능


class Dog:
    dog_count = 0  # 클래스 속성

    def __init__(self, name, color):  
        self.name = name  # 인스턴스 속성
        self.color = color
        Dog.dog_count += 1  # 클래스 속성 접근

    def dog_Count(self):  # Python에서는 같은 이름을 클래스 속성과 메서드에 동시에 사용할 수 없음
        print("총 강아지는 : ", Dog.dog_count)

# 인스턴스 생성
hello = Dog("hello", "black")
hello.dog_Count() 
happy = Dog("happy", "white")
happy.dog_Count() 

    