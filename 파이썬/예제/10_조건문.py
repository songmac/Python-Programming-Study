# 조건 생략
x = 10
if x == 10:
    pass

# 들여쓰기
    print("x가 10입니다")
    print("x가 12가 아닙니다")
        # print("x가 12가 아닙니다") # error
# print("x가 12가 아닙니다") # error
    

# 중첩 if문
if x >= 10 :
    if x <= 20:
        print("10이상 20이하")
    if x <= 30 :
        print("20초과 30이하")


# elif와 else
if x == 'A':
    print("x는 A")
elif x == 'B':
    print("x는 B")
elif x == 'C':
    print("x는 C")
else:
    print("x는 A, B, C가 아님")

    
       
