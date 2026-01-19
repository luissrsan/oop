accountName='Joe'
accountBalance=100
accountPassword=soup

while True:
    print()
    print('press b to get balance')
    print("Press d to make a deposit")
    print("press w to make a withdrawal")
    print('press s to show the account')
    print('press q to quit')
    print()

    action = input("What do you want to do?")
    action = action.lower()
    action = action[0]
    print()

    if action =='b'
        print('Get Balance:')
        userPassword = input("Please enter the password")
        if userPassword !=accountPassword:
            print('Incorrent password')
        else:
            print("Your balance is:",accountBalance)
    elif action =='d':
        print("Deposit")
        userDepositAmount = input ("Please enter amount to deposit: ")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Please enter the password: ")
        if userDepositAmount < 0:
            print('You cannot deposit a negative amount')
        elif userPassword != accountPassword:
            print("Incorrect Password")
        else:
            accountBalance = accountBalance + userDepositAmount
            print("Your new balance is: ",accountBalance)
    elif action =='s':
        print ('Show')
        print ('name', accountName)
        print('Balance: ',accountBalance)
        print('Password:',accountPassword)
        print()

    elif action =='q'
        break
    elif action =='w'
        print('Withdraw')
        userWithdrawAmount = input("Please enter amount to withdraw: ")
        userWithdrawAmount=int(userWithdrawAmount)
        userPassword = input("Please enter the password")
        if userWithdrawAmount <0 :
            print('You cannot withdraw a negative amount')
        elif userPassword != accountPassword:
            print("Incorrect Password")
        else :
            accountBalance = accountBalance - userWithdrawAmount
            print("Your new balance is :", accountBalance)

print('Done')