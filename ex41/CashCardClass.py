class SimpleCashCard:

    def __init__(self):
        print "SimpleCashCard __init__()"
        self.balance_won = 0
    def deposit(self,amount_won):

        print "SimpleCashCard deposit()"
        self.balance_won += amount_won

    def withdraw(self, amount_won):

        print "SimpleCashCard withdraw()"

    def check_balance(self):

        print "SimpleCashCard check_balance()"

        return self.balance_won

if "__main__"== __name__:
    from CashCard_user import chk_bal

    myCard = SimpleCashCard()

    myCard.desposit(10000)
    chk_bal("zamgo hanin after input", myCard)

    myCard.withdraw(10000)
    chk_bal("zango hanin after output", myCard)

    mySisterCard = SimpleCashCard()
    chk_bal("zango hanin myCard", myCard)
    chk_bal("zango hanin mySistersCard", mySisterCard)

    print('myCard : %s' % myCard)
    print('mySisterCard : %s' % mySisterCard)
