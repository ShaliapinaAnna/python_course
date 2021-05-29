class BankAccount:
    def __init__(self, owner_name, number, balance, password):
        self.owner_name = owner_name
        self.number = number
        self.__balance = balance
        self.__password = password

    def change_balance(self, inp_balance, inp_password):
        if inp_password == self.__password:
            self.__balance = inp_balance
            return self.__balance
        else:
            return 'Wrong password'


bank_account = BankAccount('Alex', '170123456', 10000, '123321')
print(bank_account.change_balance(0, '123'))
print(bank_account.change_balance(0, '123321'))
