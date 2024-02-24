# 패키지 : 여러가지 모듈을 모아놓은 것

## 모듈 pkcalc/calc.py 임포트
## 같은 디렉토리에 위치

## 방법 1
import pkcalc.calc as calc

print(calc.name)
print(calc.add(5,6))


## 방법 2
from pkcalc.calc import name, add

print(name)
print(add(5,6))