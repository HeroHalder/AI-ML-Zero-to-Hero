class Bank:
    def __init__(self):
        self.__balance = 1000   # private

    def show_balance(self):
        print(self.__balance)

b = Bank()
b.show_balance()
#print(b.__balance)   # AttributeError: 'Bank' object has no attribute '__balance'
