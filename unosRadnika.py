import sys
from userI import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5 import QtGui

class form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.userI = Ui_MainWindow()
        self.userI.setupUi(self)
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('vanreda.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('radnici')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal,"Radnik_ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal,"Ime")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Prezime")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "OIB")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Adresa")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Grad")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Mobitel")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Datum Zaposlenja")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Sifra")
        self.userI.tableView.setModel(self.model)
        self.userI.tableView.setColumnHidden(8, True)

        self.userI.pushButton.clicked.connect(self.dodajuDb)
        self.userI.pushButton_4.clicked.connect(self.reset)
        self.show()
        self.userI.pushButton_2.clicked.connect(self.azuriraj)
        self.userI.pushButton_3.clicked.connect(self.brisi)
        self.i = self.model.rowCount()
        self.userI.lcdNumber.display(self.i)
        print(self.userI.tableView.currentIndex().row())




    def dodajuDB(self):
        print(self.i)
        self.model.insertRows(self.i,1)
        self.model.setData(self.model.index(self.i, 0), self.userI.lineEdit_6.text())
        self.model.setData(self.model.index(self.i, 1),self.userI.lineEdit.text())
        self.model.setData(self.model.index(self.i, 2), self.userI.lineEdit_2.text())
        self.model.setData(self.model.index(self.i, 3), self.userI.lineEdit_8.text())
        self.model.setData(self.model.index(self.i, 4), self.userI.lineEdit_4.text())
        self.model.setData(self.model.index(self.i, 5), self.userI.lineEdit_5.text())
        self.model.setData(self.model.index(self.i, 6), self.userI.lineEdit_3.text())
        self.model.setData(self.model.index(self.i, 7), self.userI.dateEdit.text())
        self.model.setData(self.model.index(self.i, 8), self.userI.lineEdit_7.text())
        self.model.submitAll()
        self.i += 1
        self.userI.lcdNumber.display(self.i)

    def brisi(self):
        if self.userI.tableView.currentIndex().row() > -1:
            self.model.removeRow(self.userI.tableView.currentIndex().row())
            self.i -= 1
            self.model.select()
            self.userI.lcdNumber.display(self.i)
        else:
            QMessageBox.question(self,'Greška!', "Izaberite radnika!", QMessageBox.Ok)
            self.show()

    def azuriraj(self):
        if self.userI.tableView.currentIndex().row() > 0:
            record = self.model.record(self.userI.tableView.currentIndex().row())
            record.setValue("Radnik_ID", self.userI.lineEdit_6.text())
            record.setValue("Ime",self.userI.lineEdit.text())
            record.setValue("Prezime",self.userI.lineEdit_2.text())
            record.setValue("OIB", self.userI.lineEdit_8.text())
            record.setValue("Adresa", self.userI.lineEdit_4.text())
            record.setValue("Grad", self.userI.lineEdit_5.text())
            record.setValue("Mobitel", self.userI.lineEdit_3.text())
            record.setValue("Datum Zaposlenja", self.userI.dateEdit.text())
            record.setValue("Sifra", self.userI.lineEdit_7.text())
            self.model.setRecord(self.userI.tableView.currentIndex().row(), record)
        else:
            QMessageBox.question(self,'Greška!', "Izaberite radnika!", QMessageBox.Ok)
            self.show()

    def reset(self):
        self.userI.lineEdit.setText("")
        self.userI.lineEdit_2.setText("")
        self.userI.lineEdit_3.setText("")
        self.userI.lineEdit_4.setText("")
        self.userI.lineEdit_5.setText("")
        self.userI.lineEdit_6.setText("")
        self.userI.lineEdit_7.setText("")
        self.userI.lineEdit_8.setText("")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = form()
    sys.exit(app.exec_())
