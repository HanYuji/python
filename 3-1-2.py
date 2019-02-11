import random
""" 
n = random.randint(1,10)
print(n)

print(abs(10-15))
 """
""" """ """  """ """ """
num1 = random.randint(1,100)
num2 = int(input("추측값을 입력하세요. "))

if abs(num1 - num2) == 0:
    print("정답!!!")
elif abs(num1 - num2) <= 10:
    print("아깝네요ㅠㅠ")
else:
    print("꽝!")


