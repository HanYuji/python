# 파일 입출력 : with
# with open('path', 'mode') as 변수명:
# 들여쓰기가 끝나면 자동으로 파일을 닫아줌.

# f = open("./test1.txt", 'w')
# f.close()
# print(f.closed) # 파일이 닫혔는지 확인하는 함수?
# if not f.closed:
#     print("파일이 꺼지지 않았어요!")

# with open("./new.txt", "w") as f:
#     f.write("안녕하세요. with입니다.")

# dir(객체명): 객체가 가지고 있는 다양한 프로퍼티나 메소드를 보여줌.
# __enter__, __exit__ 메소드를 가지고 있으면 시작하고 끝날 때 자동으로 호출해줌.

# 직접 해보기 : 파일 만들고 읽어오기
# 1) 파일을 만들어서 "hello world!"를 10줄 써 넣으세요.
# 2) 파일을 append 모드로 열어서 "hello python!"을 10줄 추가하세요.
# 3) 파일을 읽어온 뒤에 파일 내용에 hello world를 20번 hello python을 10번 출력해보세요.
with open("./test1.txt", "w") as f:
    for _ in range(10):
        f.write("hello world!\n")

with open("./test1.txt", "a") as f:
    for _ in range(10):
        f.write("hello python!\n")

with open("./test1.txt", "r") as f:
    for _ in range(10):
        print(f.readline())
    f.seek(0)
    print(f.read())

# 직접 해보기 : csv파일 변환
# 1) key 값이 최소 3개 이상인 dictionary를 최소 3개 포함한 리스트를 csv파일로 만들어서 저장하는 함수를 만드세요.
# 2) 저장한 csv 파일을 불러와서 다시 dictionary로 변환하는 함수로 만드세요.

# 안 했음. 해볼 것!