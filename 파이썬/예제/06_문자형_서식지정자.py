name = "Tom"

print("I am", name, "!")
print("I am "+name+" !")
print("I am %s !" % name) # ,가 아닌 % # 띄어쓰기 필수

print("I am %10s !" % name)
print("I am %-10s !" % name)



name2, name3 = "Susan", "Jason"
print("I met %s and %s." % (name2, name3))



num1, num2, num3 = 3, 3.1245154, 4.56789
print("num1 = %d, num2 = %f, num3(소수점이하) = %.2f, num3(자릿수맞추기) = %07.2f" % (num1, num2, num3, num3))