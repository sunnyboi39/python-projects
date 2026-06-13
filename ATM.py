

def deposit(balance,amount):
    return balance+amount
def withdraw(balance,amount):
    return balance-amount

starting_balance = 1000
def atm(balance):
    action= input("Hello! what would you like to do today?\nC for Check Balance    D for Deposit    W for Withdraw\n~").upper()
    print("-"*32)
    if action=="D":
        amount=float(input("Enter Amount:"))
        balance=deposit(balance, amount)
        print("-" * 32)
        print(f"{'New balance':<16}|{balance:<16.2f}") #formatting
        print("-" * 32)
    elif action=="W":
        amount = float(input("Enter Amount:"))
        balance = withdraw(balance, amount)
        print("-" * 32)
        print(f"{'New balance':<16}|{balance:<16.2f}")
        print("-" * 32)
    else: # does check balance for c and in case wrong key is pressed
        print(f"{'Balance':<16}|{balance:<16.2f}")
        print("-" * 32)

    anything_else=input("Is there anything else you would like to do? (Y/N)\n~").upper()
    if anything_else=="Y":
        atm(balance) #calls itself so that the balance doesn't go back to 1000 if they want to do another action


atm(starting_balance)
