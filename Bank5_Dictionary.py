accountsList=[]

def newAccount(aName,aBalance,aPassword):
    global accountsList
    newAccountsDict = {'name':aName,'balance':aBalance,'password':aPassword}
    accountsList.append(newAccountsDict)

def show(accountNumber):
    global accountsList
    print('Account',accountNumber)
    thisAccountDict=accountsList[accountNumber]
    print('name',thisAccountDict['name'])
    print('balance',thisAccountDict['balance'])
    print('password',thisAccountDict['password'])
    print()

def getBalance(accountNumber,password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect Password')
        return None
    return thisAccountDict['balance']

print('Joes account number is' ,len(accountsList))
newAccount('Joe',100,'soup')

print('Marys account number is ', len(accountsList))
newAccount('Mary',12345,'nuts')

while True:
    print()
    print('press b to get the balance')
    print('press d to make a deposit')
    print('press n to create a new account')
    print ('press w to make a withdrawl')
    print('press s to show all accounts')
    print('press q to quit')
    print()

    action = input('what do you want to do')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance')
        userAccountNumber = input ('Please enter your account number')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('Please enter your password')
        theBalance =getBalance(userAccountNumber,userPassword)
        if theBalance is not None:
            print('Your balance is',theBalance)
    elif action =='d':
        print('Deposit')
        userAccountNumber = input ('Please enter your account number')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter the amount to deposit')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter your password')

        newBalance = deposit(userAccountNumber,userDepositAmount,userPassword)
        if newBalance is not None:
            print('Your new balance is',newBalance)

    elif action == 'n':
        print('New account')
        userName = input('what is your name')
        userStartingAmount = input ('what is the amount of your initial deposit')
        userStartingAmount = int(userStartingAmount)
        userPassword = input ('what password would you like to use for this account')
        
        userAccountNumber = len(accountsList)
        newAccount(userName,userStartingAmount,userPassword)
        print('your new account number is : ',userAccountNumber )
