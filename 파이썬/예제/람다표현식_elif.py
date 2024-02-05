# 람다표현식에서는 elif를 사용할 수 없음
# 람다 매개변수들의 구조 이해하기(실제구조와 다름) : 결과1 if 조건식1, else{결과2 if 조건식2, else 결과3}
# 실제 구조 : 결과1 if 조건식1 else 결과2 if 조건식2 else 결과3

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda x:0 if x%2 == 0 else 1 if x % 3 == 0 else 2, a))
print(result)