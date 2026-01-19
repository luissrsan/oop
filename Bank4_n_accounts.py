accountNamesList = []
accountBalancesList=[]
accountPasswordsList=[]

def newAccount(name,balance,password):
    global accountNamesList,accountBalancesList,accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)

def show(accountNumber):
     global accountNamesList,accountBalancesList,accountPasswordsList
     print('Account',accountNumber)
     print('Name',accountNamesList[accountNumber])
     print('Balance:',accountBalancesList[accountNumber])
     print('Password',accountPasswordsList[accountNumber])
    
def getBalance(accountNumber,password):
     global accountNamesList,accountBalancesList,accountPasswordsList
     if password!= accountPasswordsList[accountNumber]:
        print('INCORRECT PASSWORD')
        return None
    return accountBalanceList[accountNumber]

print('Joes Account is account number:',len(accountNamesList))
newAccount('Joe',100,'soup')

print('Marys Account is account number:', len(accountNamesList))
newAccount('Mary',12345,'nuts')

while True:
    print()
    print('press b to get the balance')
    print('press d to make a deposit')
    print('press n to create a new account')
    print('press w to make a withdrawl')
    print('press s to show all accounts')
    print('press q to quit')
    print()

    action=input('What do you want to do')
    action = action.lower()
    action = action[0]
    print()
    if action == 'b'
        print('Get Balance')
        userAccountNumber = input ('Please enter your account number:')
        userAccountNumber = int(userAccountNumber)
        userPassword = input ('Please enter your password')
        theBalance = getBalance(userAccountNumber,userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

print('Done')