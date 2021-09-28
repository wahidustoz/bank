from datetime import datetime
import uuid
from Transaction import Transaction

class Account:

    __transactions = []
    name:str = 'Unknown'

    def __init__(self, name:str, accountNumber:int, openingBalance:float):

        if openingBalance < 10:
            raise Exception('Opening balance is at least $10.')

        self.id = uuid.uuid4()
        self.name = name
        self.accountNumber = accountNumber
        self.makeDeposit(openingBalance, 'Opening balance')
    
    def makeDeposit(self, amount:float, note:str):
        if amount < 1:
            raise Exception('Minimum deposit amount is $1.')
        self.__makeTransaction(amount, note)
    
    def makeWithdrawal(self, amount:float, note:str):
        if amount > self.getBalance():
            raise Exception('You have insufficient balance.')
        self.__makeTransaction(-amount, note)
    
    def getBalance(self):
        return sum(t.amount for t in self.__transactions)

    def getHistory(self):
        history = 'Amount\tDate\tNote\n'
        for t in self.__transactions:
            history += str(t)
        return history
    
    def __makeTransaction(self, amount, note):
        transaction = Transaction(self.id, amount, datetime.now(), note)
        self.__transactions.append(transaction)
