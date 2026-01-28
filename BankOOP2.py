from Account import *

accountsList=[]
oAccount=Account('Joe',100,'JoesPassword')
accountsList.append(oAccount)
print('Joes Account number is 0')

oAccount =Account('Mary',12345,'MarysPassword')
accountsList.append(oAccount)
print('Marys Account number is 1')

accountsList[0].show()
accountsList[1].show()
print()

print('calling methods of the two accounts')
accountsList[0].deposit(50,'JoesPassword')
accountsList[1].withdraw(345,'MarysPassword')

accountsList[1].deposit(100,'MarysPassword')
accountsList[0].show()
accountsList[1].show()

print()
userName = input ('what is the name for the user account?')
userBalance = input('what is the starting balance for this account ')
userBalance = int(userBalance)
userPassword =input ('what is the password you want to use for this account')
oAccount = Account(userName,userBalance,userPassword)
accountsList.append(oAccount)


print('created new account ,account number is 2 ')
accountsList[2].show()
accountsList[2].deposit(100,userPassword)
userBalance = accountsList[2].getBalance(userPassword)
print()
print('after depositing 100 , the user balance is ,',userBalance)
accountsList[2].show()