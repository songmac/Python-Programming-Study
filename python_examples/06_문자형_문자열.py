word1 = "과일"+"사과"
word2 = "과일"*3 
word3 = "I like Banana."

print(word1)
print(word2)

print(len(word1))
print(len(word2))


print(word1.upper()) # 한글이라 영향 없음
print(word2.lower()) # 한글이라 영향 없음
print(word3.upper()) # 괄호가 없으면 메서드의 내장 메모리 주소를 출력함
print(word3.lower())

print(word1.replace("사과", "딸기"))
print(word2.replace("과일", "샤인머스켓"))
print(word3.replace("Banana", "Blueberries"))