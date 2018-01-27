#!/usr/bin/env python
import sys
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
from list_all_ui import Ui_Form

try:
    QString = unicode
except NameError:
    # Python 3
    QString = str

class Database:
    def __init__(self, parent = None):
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("../Data/Finance.sqlite")
        self.data.open()
        if not self.data.open():
            QMessageBox.warning(None, "Finance",
                QString("Database Error: %1").arg(self.db.lastError().text()))
            sys.exit(1)

def get_available_funds():
    import sqlite3
    db = sqlite3.connect("C:\\Users\\kendsr\\Desktop\\Production\\Finance\\Data\\Finance.sqlite")    
    cursor = db.cursor()
    cursor.execute("select round(available,2) from available_funds")  
    return str(cursor.fetchone()[0])
    cursor.close()    
    db.close()

class Model(QtSql.QSqlTableModel):
    def __init__(self, parent = None):
        super(Model, self).__init__(parent)
        self.setEditStrategy(QtSql.QSqlTableModel.OnRowChange)
        self.setTable("checking")
        if not self.select():
            print(self.lastError().text()) 
            print("Select not OK")

class Main(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.db = Database()
        self.model = Model(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.showColumn(1)
        self.ui.tableView.resizeColumnsToContents()
        self.available_funds = get_available_funds()
        self.ui.label_2.setText("Available Funds: " + self.available_funds)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.resize(1150, 800)
    window.setWindowTitle('Maygrove Finance System')
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
