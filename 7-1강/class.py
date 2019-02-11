class Wallet:
    #처음 객체가 생성될 때 실행되는 메소드: __init__
    def __init__(self, name):
        # self: 객체 자신 의미.
        self.owner = name
    
    def print_owner_name(self):
        print('owner name is', self.owner)
    
my_wallet = Wallet('cat')

# print(my_wallet.owner)
my_wallet.print_owner_name()