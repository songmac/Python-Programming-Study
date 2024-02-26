# 일급함수(일급객체, first-class Function)
"""
설명
1. 함수를 변수에 담을 수 있어야 한다
2. 함수를 매개변수로 전달할 수 있어야 한다
3. 함수를 리턴값으로 사용될 수 있어야 한다

파이썬에서는 함수가 일급객체 조건을 만족한다
즉, 함수를 데이터처럼 자유롭게 사용할 수 있다는 것을 의미한다

"""


# 클로저(Closure)
"""
설명
1. 내부 함수를 결과로 반환할 때, 그 내부 함수를 클로저라고 한다
2. 내부함수는 외부함수의 변수(프리변수)에 참조가능하고 함수가 종료된 후에도 접근 및 값이 유지된다

사용 용도
1. 함수프로그래밍
2. 동시성제어
3. 데코레이터
"""

def closure():
    # Free Variable
    save_text = ""

    def save(text):
        nonlocal save_text
        save_text += text
        return save_text
    
    return save