import sys

from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
from list_ui import Ui_Form

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

class Model(QtSql.QSqlTableModel):
    def __init__(self, parent = None):
        super(Model, self).__init__(parent)
        self.setEditStrategy(QtSql.QSqlTableModel.OnRowChange)
        self.setTable("checking")
        self.setFilter("status != 'X' and status != 'x' and category != 'Escrow'") ## Transactions which have not cleared the bank
        self.select()        

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

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.resize(1150, 800)
    window.setWindowTitle('Maygrove Finance System')
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
