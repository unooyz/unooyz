import CashCard as CashCard_module

def chk_bal(message, account):
    print ("%s : %d" % (message, account.check_balance()))


if '__main__' == __name__:
    chk_bal("CashCard_module Zan ack hanin", CashCard_module)

    print ("10000won imgeam")

    CashCard_module.deposit(10000)

    chk_bal("hanin",CashCard_module)

    print("1000won chulgeam")
    CashCard_module.withdraw(1000)

    chk_bal("hanin", CashCard_module)

    import  CashCard as mySistersCard_module

    chk_bal("CashCard_moudule hanin", CashCard_module)
    chk_bal("mySistersCard_moudule hanin", mySistersCard_module)

    print("CashCard_module: %s" % CashCard_module)
    print("mySistersCard_moudle : %s" % mySistersCard_module)

