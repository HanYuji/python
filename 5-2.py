# default value
# def func_name(위치인자, 키워드인자):
# 위치인자는 키워드인자보다 앞에 나와야한다.
def test(a, b, c):
    print("a는 ", a)
    print("b는 ", b)
    print("c는 ", c)

print(test(1, 2, 3))
print(test(b=1, c=2, a=3))
print(test(3, c=2, b=1))
# print(test(b=1, c=2, 3)) # error

# packing, unpacking
# packing : 함수 정의 시 들어올 인자가 몇 개인지 모를 때 사용.
# unpacking : 함수에 어떤 값을 넣어줄 때 packing 된 값을 풀어서 넘길 때 사용.
# packing
# * : 위치인자만 들어올 때
# 함수 정의 시의 * : 인자를 packing 해서 쓰겠다는 의미.
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5, 6, 7))

#unpacking
# 함수 호출 시의 * : 리스트나 딕셔너리 따위로 packing 되어 있는 것을 unpacking 하겠다는 의미.
print(sum_all(*[1, 2, 3, 4, 5, 6, 7]))

#packing
def print_f_name(father, mother, sister, brother):
    print("아버지 이름은 ", father)
    print("어머니 이름은 ", mother)
    print("언니 이름은 ", sister)
    print("남동생 이름은 ", brother)

print_f_name(father="홍길동", mother="김영희", sister="둘리", brother="둘리")

# ** : 키워드 인자로 들어올 떄
def print_family_name(**kwargs):
    for key in kwargs:
        print(key, '의 이름은 ', kwargs[key])

print_family_name(father="홍길동", mother="김영희", sister="둘리", brother="둘리", cat = "나비", dog="멍멍이")

#unpacking
family_dict = {
    "father" : "고길동"
    , "mother" : "이영희"
    , "sister" :  "나둘리"
    , "cat" : "야옹이"
}

print_family_name(**family_dict)


likes = []
def input_like():  
    like = input("좋아하는 걸 하나 입력하세요.")
    likes.append(like)
    print(likes)

input_like()
input_like()
input_like()

# 재귀함수 (Recursion Function)
# 예) n! = n * (n-1) * (n-2) * ... * 1
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# print(factorial(5))

# 위 식을 재귀를 사용하여 나타내기
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# 직접 해보기 : 재귀 함수! 더하기
# 1) 정수 a와 n을 받아서 a에 n을 더하는 함수를 재귀함수로 만들어 보세요.
def self_add(a, n):
    if n == 0:
        return a
    return n + self_add(a, n-1)

print(self_add(10, 5))

# 강사님 방법
def add_n(a, n):
    if n == 0:
        return a
    return 1 + add_n(a, n-1)

print(add_n(10,7))
