# 어떠한 코드를 반복해야할 때 사용 (반복횟수가 정해져있지 않을 때)
i = 0 

while i < 10:
    print("현재값 : ", i)
    i += 1


# while 응용
count = int(input("반복횟수?"))
i = 0 

while i < count:
    print("입력한 횟수만큼 반복")
    i += 1


# 입력조건이 맞을때까지 반복하기
i = 0

while i != 5:
    i = int(input("5를 입력하면 반복이 중단됩니다. :"))
print("중단!")