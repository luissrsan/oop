from Account import *

oJoesAccount = Account('Joe','100','JoesPassword')
print('created an account for joe')

oMarysAccount = Account('Mary','12345','MarysPassword')
print('Created an account for Mary')

oJoesAccount.show()
oMarysAccount.show()
print()

print('Calling methods of the two accounts')
oJoesAccount.deposit(50,'JoesPassword')
oMarysAccount.deposit(100,'MarysPassword')

oJoesAccount.show()
oMarysAccount.show()