# 예외처리
# try:
#     Error 발생할 우려가 있는 코드
# except:
#     Error 발생 시 작동하는 코드

try:
    num = input('숫자를 입력하세요.')
    num = int(num)
    print(num + 5)
except:
    print('숫자만 입력하세요. 한글과 영어 등 다른 언어는 안 돼요.')

# 대표적인 Error
# TypeError
# NameError
# ZeroDivisionError
# ...
# 에러를 명시해주면 에러 발생 시 디버깅이 용이해짐.
try:
    num = input('숫자를 입력하세요.')
    num = int(num)
    print(10 / num)
except (ValueError, ZeroDivisionError):
    print('숫자만 입력하세요. 한글과 영어 등 다른 언어는 안 돼요. 0도 안 돼요.')

