# 기본
print("I like {0}, {1} !!".format("Winter", "Karina"))

# 변수 사용
mem1, mem2 = "Ningning", "Gissel"
print("Also, I like {}, {} too !!".format(mem1, mem2))

# 위치 변경
print("My Car Number is KE{0}{1}{2}".format(1, 3, 5))
print("My Car Number is KE{}{}{}".format(1, 3, 5))
print("My Car Number is KE{2}{1}{0}".format(1, 3, 5))
print("My Car Number is KE{2}{1}{0}".format(1, 3, 5))

# 공백 추가
print("오른쪽으로 네번 : Number {0:>4} !".format(1))
print("왼쪽으로 네번 : Number {0:<4} !".format(1))

# 공백 0으로 채우기
print("공백 0으로 채우고, 왼쪽부터 네번째자리 : Number {0:0<4} !".format(1))
print("공백 0으로 채우고, 다섯개 중에 가운데자리 : Number {0:0^5} !".format(1))