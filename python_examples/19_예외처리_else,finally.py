# else : 오류가 발생하지 않을때만 동작
# finally : 오류발생여부 상관없이 무조건 동작

try:
    print(10/0)
except:
    print("예외오류발생")
else:
    print("오류발생하지 않음")
finally:
    print("무조건 실행")