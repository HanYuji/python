# csv (comma-separated values)
# 콤마로 구별되어있는 값들
csv_values = """
이름, 연락처, 나이, 이메일
철수, 010-1234-1234, 23, cheolsu@gmail.com
영희, 010-4321-4321, 27, 0hee@gmail.com
"""

# split(구분자) : 구분자를 기준으로 값을 잘라서 리스트로 만듦.
# phone = "010-1234-5678"
# print(phone)

# phone_split = phone.split('-')
# print(phone_split)

# strip(구분자) : 양쪽 끝에 있는 구분자를 없앰.
# string = "----py--thon!!!----"
# print(string.strip('-').strip('!'))

# print(csv_values)

csv_values = csv_values.strip('\n')
# print(csv_values)
csv_list = csv_values.split('\n')
print(csv_list)
print('---------------------------------------')

# info = {}

# for el in csv_list:
#     print(el)

# print('---------------------------------------')

# for el in csv_list:
#     print(el.split(','))
# print('---------------------------------------')

# dictionary로 만들기
keys = []

# for el in csv_list:
#     print(el)

# for el in csv_list[0]:
#     print(el)

# print(csv_list[0].split(','))

# for el in csv_list[0].split(','):
#     print(el)

for el in csv_list[0].split(','):
    keys.append(el.strip(' '))

print(keys)

# values만 가져오기
for val in csv_list[1:]:
    print(val)

results = []
for val in csv_list[1:]:
    result_dict = {}
    i = 0
    for el in val.split(','):
        result_dict[keys[i]] = el.strip(' ')
        i += 1
    results.append(result_dict)
print(results)

# 직접 해보기
# csv를 dictionary로 바꾸기
# 1) 이름, 나이, 전화번호, 이메일을 항목으로 가지고 4명의 정보를 담고있는 csv를 만드세요.
# 2) 위의 정보를 dictionary로 바꾸세요.

# csv_values = """
# 이름, 나이, 전화번호, 이메일
# 둘리, 20, 010-1234-5678, dulri@gmail.com
# 길동, 40, 010-9876-5432, gildong@naver.com
# 또치, 22, 010-1234-9876, ddochi@gmail.com
# """

# set : {} 형식이며, 값만 들어감, 중복제거.
set1 = {1,1,2,3,4,4,4,4,5,5,5}
print(set1)

set2 = {}
print(type(set2))

# dict(), set() 있음. list(), list[]는 없음. list(a)와 같은 것은 있음.
set3 = set()
print(type(set3))

set3.add(3)
set3.add(4)
set3.add(5)
set3.add(6)
print(set3)

set1.union(set3) #합집합
set1.difference(set3) #차집합
set3.difference(set1)

# 직접해보기 set 연산
# 1) set1 변수에 1~100까지 숫자 중 3의 배수
# 2) set2 변수에 1~100까지 숫자 중 5의 배수
# 3) set3 변수에 1~100까지 숫자 중 15의 배수
# 4) 두 set1, set2에서 겹치는 숫자를 출력하세요.
# 5) set3에서 set1에 포함되지 않는 숫자를 출력하세요.

set1 = set()
set2 = set()
set3 = set()

# for i in range(1,101):
#     if (i % 3) == 0:
#         set1.add(i)

# for i in range(1,101):
#     if (i % 5) == 0:
#         set2.add(i)

# for i in range(1,101):
#     if (i % 15) == 0:
#         set3.add(i)

# 위의 식을 하나에서 처리하기
# for i in range(1, 101):
#     if i % 3 == 0:
#         set1.add(i)
#     if i % 5 == 0:
#         set2.add(i)
#     if i % 15 == 0:
#         set3.add(i)

# 다른 방법2
for i in range(1, 101):
    if i % 3 == 0:
        set1.add(i)
    if i % 5 == 0:
        set2.add(i)

set3 = set1.intersection(set2)

print(set1)
print(set2)
print(set3)
set1.intersection(set2) #교집합
set3.difference(set1) #차집합
set3 - set1 #차집합

########################################################
# Comprehension : 각각의 값들을 생성하고 초기화 할 수 있음.
# List Comprehension
a = []
for i in range(1, 11):
    a.append(i**2)
print(a)

# list 안에서 for문 돌리기
b = [ j**2 for j in range(1, 11) ]
print(b)

c = []
for i in range(1, 101):
    if i % 3 == 0:
        c.append(i)
print(c)

d = [i for i in range(1, 101) if i % 2 == 0]
print(d)

# [[1,2], [1,2]]
e = []
for i in range(1,3):
    el = []
    for j in range(1,3):
        el.append(j)
    e.append(el)

print(e)

# _ : 인덱스는 사용하지 않고, 횟수만 사용했다는 의미.
result = [ [x for x in range(1,3)] for _ in range(2)]
print(result)

# 직접 해보기 : List Comprehension
# 1) 1~100까지 숫자 중 3의 배수인 숫자만 가진 리스트 만들기
# 2) [[1,2,3], [1,2,3], [1,2,3]]

result1 = [i for i in range(1, 100) if i % 3 == 0]
print(result1)

result2 = [ [i for i in range(1,4)] for _ in range(3)]
print(result2)