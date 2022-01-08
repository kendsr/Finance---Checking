import sqlite3
from decimal import Decimal

db = sqlite3.connect("C:\\Users\\kendsr\\Google Drive\\Finance.sqlite")
cursor = db.cursor()


def get_available_funds():
    cursor.execute("select round(available,2) from available_funds")
    return cursor.fetchone()[0]


def get_uncleared_credit():
    cursor.execute('''
        select sum(withdrawal) from checking 
        where upper(status) != "X"
        ''')

    withdrawal = cursor.fetchone()[0]
    if withdrawal is None:
        return 0
    else:
        return withdrawal


def get_uncleared_debit():
    cursor.execute('''
        select sum(deposit) from checking 
        where upper(status) != "X"
        ''')
    debit = cursor.fetchone()[0]
    if debit is None:
        return 0
    else:
        return debit


def get_Hold():
    cursor.execute('''
        select sum(withdrawal) from checking 
        where desc = "HOLD"
        ''')
    return cursor.fetchone()[0]


def main():
    print("Account Balance")
    print("")
    bankStatementBalance = Decimal(input("Enter Bank Statement Balance: "))
    print("")
    print("Bank Statement Balance: " + str(bankStatementBalance))

    withdrawal = round(Decimal(get_uncleared_credit()), 2)
    debit = round(Decimal(get_uncleared_debit()), 2)
    print("Uncleared Withdrawal Transactions: " + str(withdrawal))
    print("Uncleared Deposit Transactions: " + str(debit))

    hold = round(Decimal(get_Hold()), 2)
    print("Funds on HOLD: " + str(hold))

    registryBalance = round(Decimal(get_available_funds()), 2)
    print("Available funds: " + str(registryBalance))

    total = round((registryBalance + withdrawal + hold) - debit, 2)
    print("Registry balance " + str(total))

    print("")
    # print "bankStatementBalance ", bankStatementBalance, type(bankStatementBalance)
    # if total == bankStatementBalance:
    #     print "BALANCED"
    # else:
    #     over_under = bankStatementBalance - total
    #     print "Out of balance by " + str(over_under)

    # print "O/U: ", over_under, type(over_under)
    # print "Total: ", total, type(total)
    # print "regbal: ", registryBalance, type(registryBalance)
    # print "uncleared: ", uncleared, type(uncleared)
    # print "hold: ", hold, type(hold)


if __name__ == '__main__':
    main()
    cursor.close()
    db.close()
