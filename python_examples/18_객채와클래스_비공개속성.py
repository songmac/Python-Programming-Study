# 비공개 속성(private attribute) : 외부에서 속성에 접근하지 못하게 차단. 속성명앞에 __추가

class Dog:
    def __init__(self, name, color): #생성자 함수
        self.__hungry = 0 # 비공개 속성
        self.name = name
        self.color = color
    def eat(self): # 인스턴스 매서드
        if self.__hungry <= 0:
            print("배가너무 불러요!")
        else:
            self.__hungry -= 10
            print("밥먹음", self.__hungry)
    def walk(self):
        self.__hungry += 10
        print("산책", self.__hungry)
    def condition(self):
        print(f"{self.name} 배고픔 : {self.__hungry}") # f-string formatting
        # print("%s 배고픔 : %d" % (self.name, self.__hungry)) # % 연산자 사용


mery = Dog("mery", "black")
mery.walk()
mery.walk()
mery.walk()
mery.eat()
mery.eat()
mery.eat()
mery.walk()
mery.walk()
mery.condition()
# mery.__hungry += 100 # 오류
