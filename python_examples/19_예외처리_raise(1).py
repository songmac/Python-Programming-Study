# raise : 예외 발생시키기
# 설명 : 특정 조건에서 프로그램의 흐름을 의도적으로 중단하고, 문제를 식별하기 위한 메시지를 제공 할 때 유용하게 쓰임

try:
    raise Exception("예외강제발생") # raise 키워드는 Exception이라는 예외를 발생
except Exception as e:
    print("예외발생", e)
