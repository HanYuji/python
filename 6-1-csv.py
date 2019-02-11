import pprint
# 직접 해보기 : csv파일 변환
# 1) key 값이 최소 3개 이상인 dictionary를 최소 3개 포함한 리스트를 csv파일로 만들어서 저장하는 함수를 만드세요.
# 2) 저장한 csv 파일을 불러와서 다시 dictionary로 변환하는 함수로 만드세요.
values = [{
    "name" : "sol"
    , "phone" : "010-1234-5678"
    , "city" : "seoul"
    , "email" : "test@gmail.com"
    , "cat" : "야옹이"
} for _ in range(3)]

pprint.pprint(values)

def to_csv(value):
    keys = []
    for el in value[0]:
        keys.append(el)
    # keys = ['name', 'phone', 'city']
    results = []
    for d in value:
        result = []
        for el in d.values():
            result.append(el)
        results.append(result)

# join(): 괄호가 아닌 함수 앞에 구분자를 넣으면 구분자를 기준으로 괄호안의 값을 연결해줌.
    content = ', '.join(keys) + '\n'
    for result in results:
        content += ', '.join(result) + '\n'
    f = open("./csv_file.txt", "w")
    f.write(content)
    f.close()

to_csv(values)

# 2번
# 힌트: strip(), split()
f = open("./csv_file.txt,", "r")
content = f.read()
# 하다 말음. 지난 강의 참고해서 해결할 것.

f.close()
