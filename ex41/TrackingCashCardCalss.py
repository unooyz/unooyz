from SafeCashCardClass import SafeCashCard

import time

class HistoryCashCard(SafeCashCard):
    """

    cash card capable of recording histories
    """

    def __init__(self):
        print "HistoryCashCard __init__()"

        SafeCashCard.__init__(self)

        self.history = []

    def deposit(self,amount_won):
        """
        HistoryCashCard deposit method
        deposit amount & add record to history
        """
        print "HistoryCashCard deposit()"
        SafeCashCard.deposit()

        self.record_history('deposit',amount_won)

    def withdraw(self,amount_won):
        """
        historyCashCard withdraw method
        withdraw amount & sff record to history
            """

        print "HistoryCashCard withdraw()"
        SafeCashCard.withdraw(self,amount_won)
        self.record_history('withdraw',amount_won)

    def record_history(self,activity,amount_won):
        record = {
            'time':time.localtime(),
            'balance' : self.check_balance(),
            'activity':activity,
            'amount' : amount_won
        }
        self.history.append(record)

    def show_history(self):
        """
        HistoryCashCard show_history method
        show appended history
        """
        print "HistoryCashCard show_history()"

        print('%25s %10s %10s %10s' % ('time and date','activity','amount','balance'))

        for record in self.history:

            print ('%25s %10s %10d %10d' (time.asctime(record['time']), record['activity'], record['amount'], record['balance']))

if "__main__" == __name__:
    print("main 객체생성". ljust(60,'*'))
    myHistcard = HistoryCashCard()
    print("main 10000원 입금". ljust(60,'*'))
    myHistcard.deposit(10000)
    print("main 9000원 출금". ljust(60,'*'))
    myHistcard.withdraw(10000)
    print("main 9000원 출금". ljust(60,'*'))
    myHistcard.withdraw(10000)
    print("main 내역확인". ljust(60,'*'))
    myHistcard.show_history()
    print("main 끝".ljust(60,'*'))






