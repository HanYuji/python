class Wallet:
    money = 0

    def __init__(self, name):
        self.owner = name

    def print_owner_name(self):
        print("{}님의 잔액은 {}원 입니다.".format(self.owner, self.money))
    
    def now_money(self):
        print("현재 잔액은 {}원 입니다.".format(self.money))

    def spend(self, m):
        if self.money < m:
            print("돈이 부족합니다.")
            self.print_owner_name()
        else:
            self.money -= m
            print("{}을 지출했습니다.".format(m))
            self.now_money()

    def income(self, m):
        self.money += m
        self.print_owner_name()
    
# sol_wallet = Wallet('sol')
# suzy_wallet = Wallet('suzy')