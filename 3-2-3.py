# sum()함수 이용해서 1~100까지 다 더하기
val = list(range(1, 101))
val
sum(val)

# sum(range(1,101))

# # 1~100 까지 숫자 중 2와 3의 약수만 더하기
# n = 0
# for i in range(1, 101):
#     if i % 2 == 0 or i % 3 == 0:
#         n += i
#     else:
#         pass
# print(n)

# # fizz buzz
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)