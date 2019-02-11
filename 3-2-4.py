# 소수판별
# 내가 한 거 -> 완벽하지 않음.
# for i in range(1, 101):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         else:
#             print(i)

#정답
for i in range(1, 101):
    key = True
    for j in range(2, i):
        if i % j == 0:
            key = False
            break
    if key:
        print(i)
                        