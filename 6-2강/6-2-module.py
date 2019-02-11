# 모듈(module) : 프로그램(기능)의 모음.
# 형식: from ** import ***
#       import ***
def add_all(*args):
    return sum(args)

# 파이썬에서는 모든 것이 다 객체이다.
# dir(): 객체의 어떤 기능, 값이 있는지 알 수 있음.
dir(int)
dir(str)
dir(list)