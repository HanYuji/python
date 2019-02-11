# File 입/출력, 모듈
# 파일 입출력
# 파일 경로: 상대경로, 절대경로
# 모드: w, r, a
# w: write 모드, 파일 전체에 새로 쓰기
# r: read 모드, 파일을 읽는 모드
# a: append 모드, 파일에 내용을 추가하는 모드
# f = open('파일 경로', '모드')
# f.close()

# 파일 생성
# f = open("./hello.txt", "w") # .은 현재 위치 의미.
# f.write("Hello World!")
# f.close()

# 파일에 내용 추가하기
# f = open("./hello.txt", "a")
# for i in range(2, 11):
#     content = "\n" + str(i) + "번째 줄 입니다."
#     f.write(content)
# f.close()

# 파일 읽어오기
# f = open("./hello.txt", "r")
# content = f.read()
# print(content)
# print(f.read()) # 안 나옴.
# #이유: 위에서 한번 읽었는데 읽고 나면 커서가 마지막 줄에 있음.
# #다시 읽길 원한다면 커서 위치를 바꿔주면 다시 읽을 수 있음.
# f.close()

# 커서 위치를 옮겨서 다시 읽기
# f = open("./hello.txt", "r")
# content = f.read()
# print(content)
# f.seek(0) # 커서를 파일의 0번째 위치로 옮김.
# print(f.read())
# f.close()

# 절대경로를 이용해보기
# f = open("C:\\Users\\UZ\\Desktop\\Python\\hello.txt", "r")
# content = f.read()
# print(content)
# f.seek(0) # 커서를 파일의 0번째 위치로 옮김.
# print(f.read())
# f.close()

# readline(): 한 줄씩 읽어오기
# f = open("./hello.txt", "r")
# content = f.readline()
# print(content)
# print(f.readline())
# print(f.readline())
# f.close()

# 직접 해보기 : 파일 만들고 읽어오기
# 1) 파일을 만들어서 "hello world!"를 10줄 써 넣으세요.
# 2) 파일을 append 모드로 열어서 "hello python!"을 10줄 추가하세요.
# 3) 파일을 읽어온 뒤에 파일 내용에 hello world를 20번 hello python을 10번 출력해보세요.
f = open("./test.txt", "w")
for _ in range(10):
    f.write("hello world!\n")
f.close()

f = open("./test.txt", "a")
for _ in range(10):
    f.write("hello python!\n")
f.close()

f = open("./test.txt", "r")
for _ in range(10):
    print(f.readline())
f.seek(0)
print(f.read())
f.close()

