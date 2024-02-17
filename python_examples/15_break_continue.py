# for, while에서 제어흐름을 벗어나기 위해 사용
# break : for, while을 완전히 중단
# continue : 이번 반복만 중단하고 처음으로 돌아가 다음반복 수행



# for문
for i in range(5):
    if(i==3):
        break
    print(i, end="")
print()

for i in range(5):
    if(i==3):
        continue
    print(i, end="")
print()


# while문
i = 0
while i < 30:
    if i == 20:
        break
    print(i, end=' ')
    i += 1
print()

i = 0
while i < 30:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=' ')
    i += 1
print()

