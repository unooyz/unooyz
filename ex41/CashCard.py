balance_won = 0

def deposit(amount_won):

    global  balance_won

    balance_won += amount_won

def withdraw(amount_woon):

    global  balance_won
    balance_won += (-amount_woon)

def check_balance():

    return balance_won