my_money = [0]

def spend(m):
    if my_money[0] > m:
        my_money[0] -= m
        print("{}을/를 사용했습니다. 남은 잔액은 {} 입니다.".format(m, my_money[0]))
    else:
        print("가지고 있는 돈이 부족합니다.")

def income(m):
    my_money[0] += m
    print("{}을 벌었습니다. 남은 잔액은 {} 입니다.".format(m, my_money))

wallet = {
    'money': my_money
    , 'spend': spend
    , 'income': income
}
