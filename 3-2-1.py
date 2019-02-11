for i in [1,2,3,4]:
    print(i)

for c in "python":
    print(c)

# range: 범위 지정
# range(100) : 0부터 99까지
# range(1, 100) : 1부터 99까지
for i in range(100):
    print(i)

# 0~99까지 들어있는 리스트 만들기
# 방법1
var = []
for i in range(100):
    var.append(i)

#방법2
list(range(100))


