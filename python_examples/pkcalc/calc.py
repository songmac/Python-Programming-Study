name = "calc"

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# 시작점 확인 __name__
# 파이썬은 어떤 모듈에서든 실행가능
# 해당 모듈이 시작점일경우 __name__의 값은 "__main__"
# 시작점이 아닐경우 __name__는 해당 모듈의 모듈명(파일명)
if __name__=='__main__':
    print("시작점")
