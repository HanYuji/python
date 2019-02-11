for i in range(1, 101):
    print(i)


n = 1

while n <= 100:
    print(n)
    n += 1

##############################
for i in range(100):
    print(i)
    if i > 20:
        break


for i in range(1, 101):
    if i % 2 == 0:
        print( i, "는 짝수입니다.")
    else:
        pass

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

#sum()함수 이용해서 1~100까지 다 더하기
val = list(range(1, 101))
val
sum(val)