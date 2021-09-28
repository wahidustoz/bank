from storage import Storage
from Account import Account

# hamkorBank = Account('wahid', 10)
# print(hamkorBank.getBalance())
# hamkorBank.makeDeposit(100, 'Oylik oldim')
# print(hamkorBank.getBalance())
# hamkorBank.makeWithdrawal(50, 'Naushnik oldim')
# print(hamkorBank.getBalance())
# print(hamkorBank.getHistory())

db = Storage('bank.db')

print(db.accountNumberExists(123455))
