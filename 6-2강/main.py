from multi import multi_all
from sum import add_1

# powershell을 켜고 import sys → sys.path를 하면 리스트에 다양한 경로가 있음.
# 리스트 순서대로 모듈을 검색함.
import pprint
import random

print(__name__) # __main__

print(multi_all(1,2,3,4,5))
print(add_1(10))