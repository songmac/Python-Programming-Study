# 설명
"""
Python은 try 첫 줄부터 순차적으로 코드를 실행. 
실행 과정에서 예외가 발생하면, Python은 즉시 해당 예외를 찾아 try 블록의 나머지 부분을 건너뛰고, 
적절한 except 블록으로 이동하여 예외 처리를 시도.
그 후 해당 예외가 처리될 때까지 try 블록의 나머지 코드는 실행되지 않음.
"""

x = [1, 2, 3]

try:
    print(10/0)
    x[5]

except ZeroDivisionError as e: # 발생한 예외를 e변수에 할당
    print("숫자를 0으로 나눌 수 없음", e)

except IndexError as e:
    print("잘못된 인덱스", e)


# 'as e' 구문 : e 변수를 통해 예외 메시지(e.args 또는 str(e))에 접근하여 사용자에게 보다 구체적인 오류 메시지를 제공