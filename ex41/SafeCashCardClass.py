from CashCardClass import SimpleCashCard as CashCard

class SafeCashCard(CashCard):

    def withdraw(self,amount_won):

        print("SafeCashCard withdraw()")

        if self.check_balance() >= amount_won:
            CashCard.withdraw(self,amount_won)

        else:

            print("**Error")
            print("No money")
            print("No withdraw")


if "__main__" == __name__:
    from CashCard_user import chk_bal

    myCard = CashCard()
    mySafeCard = SafeCashCard

    mySistersSafdCard = SafeCashCard()

    myCard.deposit(10000)

    mySafeCard.deposit(10000)
    mySistersSafdCard.deposit(200000)

    chk_bal("myCard zango hanin after input", myCard)
    chk_bal("mySafeCard zango hanin after input", mySafeCard)
    chk_bal("mySistersSafeCard zango hanin after input", mySistersSafdCard)

    myCard.withdraw(100000)
    mySafeCard.withdraw(100000)
    mySistersSafdCard.withdraw(100000)

    chk_bal("myCard zango hanin after output",myCard)
    chk_bal("mySafeCard zango hanin after output",mySafeCard)
    chk_bal("mySistersSafeCard zango hanin after output",mySistersSafdCard)