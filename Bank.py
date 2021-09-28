from storage import Storage


class Bank:

    def __init__(self):
        self.storage = Storage('bank.db')

    [classmethod]
    def deposit(cls, accountNumber:int, amount:float, note:str):
        if cls.storage.accountNumberExists(accountNumber):
            pass
        else:
            print('this account does not exist')