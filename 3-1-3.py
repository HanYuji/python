import random

""" 
num = 1

while num <= 100:
    print(num)
    num += 1 
"""

num = random.randint(1,100)

while True:
    guess = int(input("1~100사이의 추측값을 입력하세요. "))
    if num == guess :
        print("정답!")
        break
    elif abs(num - guess) <= 10:
        print("아깝네요ㅠㅠ")
    else:
        print("틀렸습니다.")