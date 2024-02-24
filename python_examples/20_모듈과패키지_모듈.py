# 모듈 : 변수, 함수, 클래스 등을 모아놓은 스크립트 파일
# import 하려는 스크립트와 같은 디렉토리에 위치해야 함

## 사용방법 1
import calc

print(calc.add(5,6))
print(calc.sub(5,6))


## 사용방법 2
from calc import add, sub

print(calc.add(5,6))
print(calc.sub(5,6))



# 시작점 확인 __name__







