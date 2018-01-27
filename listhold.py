import sqlite3

DB = sqlite3.connect("../Data/Finance.sqlite")
C = DB.cursor()
C.execute('''
    select * from checking 
        where desc = "HOLD"
        and withdrawal > 0
    ''')

print("Id\tDate\t\tAmount\tCategory")
print("--\t----\t\t------\t-------")

for row in C:
    out = '{}\t{}\t{}\t{}'.format(row[0], row[1], row[3], row[6])
    print(out)

C.close()
DB.close()

