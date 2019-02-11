# 추상화 : 별도의 공간에 존재하여, 변수간 간섭되는 방해를 일으키지 않는 방법.
# 분리 : 코드를 다른 곳에 작성하여, 필요한 경우에 호출만 하여 사용할 수 있는 방법.

# 함수 만드는 방법
# def func_name(arg):
#     #코드 작성
#     print("Hello, Func")
#     return arg
#     # return 생략 시 None 값을 리턴함.

def print_hello_world():
    print("Hello, world!")

print_hello_world()

def add_4(a):
    return a + 4

result1 = add_4(5)
print(result1)

def add(a, b):
    return a + b

result2 = add(5,6)
print(result2)

# 직접 해보기 : 함수 만들기
# 1) 숫자를 받아서 +1 해주는 함수를 만드세요.
# 2) 어떤 문자열 값을 받아서 뒤에 느낌표를 붙이는 함수를 만드세요.
def add_1(num):
    return num + 1

def add_mark(string):
    if type(string) == str:
        return string + "!"

print(add_1(3))
print(add_mark(1))
print(add_mark("python"))

# 직접 해보기: 다음 연산을 담당하는 함수를 만들어서 순서대로 실행해보세요.
# 1) 1~9까지 숫자를 하나 선택하세요.
# 2) 선택한 숫자에 2를 곱하세요.
# 3) 5를 더하세요.
# 4) 결과에 50을 곱하세요.
# 5) 1769를 더한 다음
# 6) 그리고 자신이 태어난 년도를 빼세요.
# 다시 하기!
def multi(num):
    result = ((num * 2) + 5 ) * 50 + 1769
    return result

def sub(num):
    result = result - num
    return result

result = 0
# print("1~9까지 숫자 중 하나를 선택하세요.")
input1 = input('1~9까지 숫자 중 하나를 선택하세요.')
multi(input1)

# print("자신이 태어난 년도를 입력하세요.")
input2 = input('자신이 태어난 년도를 입력하세요.')
sub(input2)

print(result)

# default value
# def func_name(위치인자, 키워드인자):
def add(a, b):
    return a + b

print(add(1)) # error 발생

def add(a, b=1):
    return a + b

print(add(1))
print(add(1,10))

def range_list(start=0, end):
    return list(range(start, end))

print(range_list(1, 10))
print(range_list(10)) # default 값은 마지막에 와야한다.

# default 값은 default 값을 주지 않은 파라미터 뒤에 와야한다.
def range_list(start, end=None):
    # None을 boolean값으로 하면 false임.
    if not end:
        return list(range(start))
    return list(range(start, end))

print(range_list(1, 10))
print(range_list(10)) 

# 직접 해보기: range_list 업그레이드
# 1) range 함수의 step 파라미터까지 받는 함수를 완성시켜보세요.
def range_list_upgrade(start, end=None, step=None):
    if not step:
        if not end:
            return list(range(start))
        return list(range(start, end))
    return list(range(start, end, step))

print(range_list_upgrade(1,10,2))
print(range_list_upgrade(3,6))
print(range_list_upgrade(5))