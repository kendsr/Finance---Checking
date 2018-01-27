import sqlite3

DB = sqlite3.connect("../Data/Finance.sqlite")
C = DB.cursor()

C.execute('''
    select round(available,2) from available_funds
    ''')

print("Available Funds")
print("---------------")

for row in C:
    print(row[0])


C.close()
DB.close()