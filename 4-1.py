list1 = [1,2,3,4,5]
print(type(list1))

# 직접 해보기1
a = tuple(range(1, 101))
b = list(a)
print(a)
print(b)

# dictionary
my_info = {
    'name' : 'gildong',
    'phone' : '010-1234-5678',
    'age' : 27
}

my_info['email'] = 'gildong@gmail.com'

for i in my_info:
    print(i) #key 출력

print("-------------------------------------------")

for j in my_info:
    print(my_info[j]) #value 출력

print("-------------------------------------------")

for k in my_info.values():
    print(k) #value 출력

print("-------------------------------------------")

for l in my_info:
    print(my_info.get(l)) #value 출력

print("-------------------------------------------")

for m in my_info:
    print(m, end = " : ")
    print(my_info[m])

print("-------------------------------------------")

for n in my_info.items():
    print(n) #key와 value가 튜플로 출력됨.

print("-------------------------------------------")

for key, value in my_info.items():
    print(key, end = " : ")
    print(value)