# 사용자 정의 예외 클래스 만들기 : Exception 클래스를 상속받기
# 목적 : Python의 표준 예외 처리 메커니즘과 호환되는, 사용자가 직접 정의한 예외를 생성할 수 있음

class MyError(Exception): # MyError 클래스는 Exception 클래스를 상속받음
    def __init__(self):  # 오타 주의
        super().__init__("나의오류")

try:
    raise MyError
except Exception as e:
    print("예외발생", e)
