import sqlite3
from Transaction import Transaction
from Account import Account

class Storage:
    def __init__(self, dbFilename:str):
        self.connection = sqlite3.connect(dbFilename)
        self.cursor = self.connection.cursor()

        self.__createTables()
    
    def __createTables(self):
        try:
            transactionTable = f"CREATE TABLE transactions(id uuid key unique, accountId uuid, amount real, date datetime, note string char(1024))"
            self.cursor.execute(transactionTable)

            accountTable = f"CREATE TABLE accounts(id uuid key unique, accountNumber integer unique, name string char(255))"
            self.cursor.execute(accountTable)
        except Exception as e:
            print(F'WARNING: {e}')

        # FOR TESTING 
        # tr = f"INSERT INTO transactions(id, accountId, amount, date, note) VALUES('4192bff0-e1e0-43ce-a4db-912808c32493', '4192bff0-e1e0-43ce-a4db-912808c32493', 1.3, datetime('now'), 'Hello world')"
        # self.cursor.execute(tr)

        # cmd = "select * from transactions;"

        # self.cursor.execute(cmd)
        # self.connection.commit()
        # print(self.cursor.fetchall())
    
    def insertTransaction(self, tr:Transaction):
        cmd = f"""INSERT INTO 
                transactions(id, accountId, amount, date, note)
                values({tr.id}, {tr.accountId}, {tr.amount}, {tr.date}, {tr.note})"""
        self.__executeCommand(cmd)

    def insertAccount(self, ac:Account):
        cmd = f"""INSERT INTO 
                accounts(id, accountNumber, name)
                values({ac.id}, {ac.accountNumber}, {ac.name})"""
        self.__executeCommand(cmd)
    
    def accountNumberExists(self, accountNumber:int) -> bool:
        
        cmd = f"select * from accounts where accountNumber = {accountNumber} limit 1;"
        self.cursor.execute(cmd)
        return len(self.cursor.fetchall()) > 0

    def __executeCommand(self, command:str, commit:bool=False):
        self.cursor.execute(command)
        if commit:
            self.connection.commit()

        
