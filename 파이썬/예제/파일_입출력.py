# 파일쓰기
file = open("file.txt", "w") # 파일 쓰기모드(w)
file.write("First File") #문자열 저장
file.close() #파일 객체 닫기

# 파일읽기
file = open("file.txt", "r")
text = file.read()
print(text)
file.close()