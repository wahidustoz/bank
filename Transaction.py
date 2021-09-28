import datetime
import uuid

class Transaction:
    def __init__(self, accoundId:str, amount:float, date:datetime, note:str):
        
        self.id = uuid.uuid4()
        self.accountId = accoundId
        self.amount = amount
        self.date = date
        self.note = note
    
    # to-do: -> overload __str__

    def __str__(self):
        return f'{self.accountId}\t{self.amount}\t{self.date}\t{self.note}\n'