
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QTableWidgetItem
import btn as bt
import xlsxwriter
import csv


import time

import os
from PyQt5 import QtSql
import subprocess



conn = sqlite3.connect('vanreda.db')
c = conn.cursor()

broj = 0
class Rac_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()





    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 805)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ikonaframe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 199);")
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('vanreda.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('racuni')


#sejva u text fajl  >>>POTREBNA PROMJENA "patha" ZA SVAKI PC>>>>
        def racunibutton():

            t = str(time.strftime("%Y%m%d-%H%M%S"))
            filename = t + ".txt"
            print("Račun spremljen u ", filename)

            with open(os.path.join('C:/Users/Danijel/Desktop/BP2kode/log/racuni',filename), 'a', newline="\n") as fajl:
                data_line = self.lineEdit.displayText()
                vrijeme = str(time.strftime("%Y-%m-%d-%H:%M"))
                writer = csv.writer(fajl,delimiter=',', quotechar=' ',escapechar=' ', quoting=csv.QUOTE_MINIMAL, dialect='excel')
                for row in range(self.tableWidget.rowCount()):

                    rowdata = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:

                            rowdata.append(item.text())
                        else:
                            rowdata.append("")


                    writer.writerow([rowdata,data_line,vrijeme])


####ubacuje u db
        def racunButtonDB():
            global broj

            broj +=1
            rac = broj
            radnik = self.lineEdit.text()
            vrijeme = str(time.strftime("%Y.%m.%d-%H:%M"))
            c.execute(" INSERT INTO fiskal  (datum) VALUES (:datum)",{"datum": vrijeme})


            for row in range(self.tableWidget.rowCount()):
                artikal = self.tableWidget.item(row,0).text()

                with conn:
                    c.execute("  INSERT INTO racuni (racun,artikal,radnik,vrijeme) VALUES (:racun,:artikal,:radnik,:vrijeme)",{"racun" : rac,"artikal" : artikal,"radnik" : radnik,"vrijeme" : vrijeme})








        def openPregled():

            subprocess.call("python" + " pregled.py", shell=True)
#BRISE TABLICU

        def close():
            sys.exit()
        def ponisti():
                while (self.tableWidget.rowCount() > 0):
                        self.tableWidget.removeRow(0)
#BRISE REDAK
        def oduzmi():
                self.tableWidget.removeRow(self.tableWidget.currentRow())

        def addp1():
                 c.execute("select artikal from artikli where sifra=1")
                 a = c.fetchall()
                 c.execute("select cijena from artikli where sifra=1")
                 b = c.fetchall()
                 for row_number, row_data in enumerate(a):
                    self.tableWidget.insertRow(row_number)
                    for colum_number, data in enumerate(row_data):
                       self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                       self.tableWidget.setItem(row_number, 0,QtWidgets.QTableWidgetItem(str(data)))

                 for row_number, row_data in enumerate(b):

                     for colum_number, data in enumerate(row_data):

                         self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(data)))




        def addp2():
                c.execute("select artikal,cijena from artikli where sifra=2")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                    self.tableWidget.insertRow(row_number)
                    for colum_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                        self.tableWidget.setItem(row_number, colum_number,QtWidgets.QTableWidgetItem(str(data)))
        def addp3():
                c.execute("select artikal,cijena from artikli where sifra=3")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                    self.tableWidget.insertRow(row_number)
                    for colum_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                        self.tableWidget.setItem(row_number, colum_number,QtWidgets.QTableWidgetItem(str(data)))
        def addp4():
                c.execute("select artikal,cijena from artikli where sifra=4")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                    self.tableWidget.insertRow(row_number)
                    for colum_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                        self.tableWidget.setItem(row_number, colum_number,QtWidgets.QTableWidgetItem(str(data)))
        def addp5():
                c.execute("select artikal,cijena from artikli where sifra=5")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                    self.tableWidget.insertRow(row_number)
                    for colum_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                        self.tableWidget.setItem(row_number, colum_number,QtWidgets.QTableWidgetItem(str(data)))

        def addp6():
                c.execute("select artikal,cijena from artikli where sifra=6")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp7():
                c.execute("select artikal,cijena from artikli where sifra=7")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp8():
                c.execute("select artikal,cijena from artikli where sifra=8")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp9():
                c.execute("select artikal,cijena from artikli where sifra=9")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp10():
                c.execute("select artikal,cijena from artikli where sifra=10")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp11():
                c.execute("select artikal,cijena from artikli where sifra=11")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp12():
                c.execute("select artikal,cijena from artikli where sifra=12")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp13():
                c.execute("select artikal,cijena from artikli where sifra=13")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp14():
                c.execute("select artikal,cijena from artikli where sifra=14")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp15():
                c.execute("select artikal,cijena from artikli where sifra=15")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addp16():
                c.execute("select artikal,cijena from artikli where sifra=16")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi1():
                c.execute("select artikal,cijena from artikli where sifra=33")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi2():
                c.execute("select artikal,cijena from artikli where sifra=34")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi3():
                c.execute("select artikal,cijena from artikli where sifra=35")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi4():
                c.execute("select artikal,cijena from artikli where sifra=36")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi5():
                c.execute("select artikal,cijena from artikli where sifra=37")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi6():
                c.execute("select artikal,cijena from artikli where sifra=38")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi7():
                c.execute("select artikal,cijena from artikli where sifra=39")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi8():
                c.execute("select artikal,cijena from artikli where sifra=40")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi9():
                c.execute("select artikal,cijena from artikli where sifra=41")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi10():
                c.execute("select artikal,cijena from artikli where sifra=42")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi11():
                c.execute("select artikal,cijena from artikli where sifra=43")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi12():
                c.execute("select artikal,cijena from artikli where sifra=44")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi13():
                c.execute("select artikal,cijena from artikli where sifra=45")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi14():
                c.execute("select artikal,cijena from artikli where sifra=46")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi15():
                c.execute("select artikal,cijena from artikli where sifra=47")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addpi16():
                c.execute("select artikal,cijena from artikli where sifra=48")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm1():
                c.execute("select artikal,cijena from artikli where sifra=17")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm2():
                c.execute("select artikal,cijena from artikli where sifra=18")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm3():
                c.execute("select artikal,cijena from artikli where sifra=19")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm4():
                c.execute("select artikal,cijena from artikli where sifra=20")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm5():
                c.execute("select artikal,cijena from artikli where sifra=21")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm6():
                c.execute("select artikal,cijena from artikli where sifra=22")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm7():
                c.execute("select artikal,cijena from artikli where sifra=23")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm8():
                c.execute("select artikal,cijena from artikli where sifra=24")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm9():
                c.execute("select artikal,cijena from artikli where sifra=25")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm10():
                c.execute("select artikal,cijena from artikli where sifra=26")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm11():
                c.execute("select artikal,cijena from artikli where sifra=27")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm12():
                c.execute("select artikal,cijena from artikli where sifra=28")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm13():
                c.execute("select artikal,cijena from artikli where sifra=29")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm14():
                c.execute("select artikal,cijena from artikli where sifra=30")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm15():
                c.execute("select artikal,cijena from artikli where sifra=31")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

        def addm16():
                c.execute("select artikal,cijena from artikli where sifra=32")
                a = c.fetchall()
                for row_number, row_data in enumerate(a):
                        self.tableWidget.insertRow(row_number)
                        for colum_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, 2, QTableWidgetItem('1'))
                                self.tableWidget.setItem(row_number, colum_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.racunFrame = QtWidgets.QFrame(self.centralwidget)
        self.racunFrame.setGeometry(QtCore.QRect(710, 60, 361, 501))
        self.racunFrame.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.racunFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.racunFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.racunFrame.setObjectName("racunFrame")
        self.tableWidget = QtWidgets.QTableWidget(self.racunFrame)
        self.tableWidget.setGeometry(QtCore.QRect(15, 10, 331, 481))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["ARTIKAL","CIJENA","KOLIČINA"])
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 173)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 70)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 681, 511))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 253, 171);\n"
"\n"
"border-top-color: rgb(0, 0, 0);\n"
"font: 40pt \"Franklin Gothic Medium\";")
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.pushPice_1 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_1.setGeometry(QtCore.QRect(20, 40, 141, 61))
        self.pushPice_1.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_1.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_1.setObjectName("pushPice_1")
        self.pushPice_1.setText(bt.p1)

        self.pushPice_1.clicked.connect(addp1)
        self.pushPice_2 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_2.setGeometry(QtCore.QRect(180, 40, 141, 61))
        self.pushPice_2.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_2.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_2.setObjectName("pushPice_2")
        self.pushPice_2.setText(bt.p2)
        self.pushPice_2.clicked.connect(addp2)
        self.pushPice_3 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_3.setGeometry(QtCore.QRect(340, 40, 141, 61))
        self.pushPice_3.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_3.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_3.setObjectName("pushPice_3")
        self.pushPice_3.setText(bt.p3)
        self.pushPice_3.clicked.connect(addp3)
        self.pushPice_4 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_4.setGeometry(QtCore.QRect(500, 40, 141, 61))
        self.pushPice_4.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_4.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_4.setObjectName("pushPice_4")
        self.pushPice_4.setText(bt.p4)
        self.pushPice_4.clicked.connect(addp4)
        self.pushPice_7 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_7.setGeometry(QtCore.QRect(340, 130, 141, 61))
        self.pushPice_7.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_7.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_7.setObjectName("pushPice_7")
        self.pushPice_7.setText(bt.p7)
        self.pushPice_7.clicked.connect(addp7)
        self.pushPice_6 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_6.setGeometry(QtCore.QRect(180, 130, 141, 61))
        self.pushPice_6.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_6.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_6.setObjectName("pushPice_6")
        self.pushPice_6.setText(bt.p6)
        self.pushPice_6.clicked.connect(addp6)
        self.pushPice_5 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_5.setGeometry(QtCore.QRect(20, 130, 141, 61))
        self.pushPice_5.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_5.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_5.setObjectName("pushPice_5")
        self.pushPice_5.setText(bt.p5)
        self.pushPice_5.clicked.connect(addp5)
        self.pushPice_8 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_8.setGeometry(QtCore.QRect(500, 130, 141, 61))
        self.pushPice_8.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_8.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_8.setObjectName("pushPice_8")
        self.pushPice_8.setText(bt.p8)
        self.pushPice_8.clicked.connect(addp8)
        self.pushPice_9 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_9.setGeometry(QtCore.QRect(20, 220, 141, 61))
        self.pushPice_9.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_9.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_9.setObjectName("pushPice_9")
        self.pushPice_9.setText(bt.p9)
        self.pushPice_9.clicked.connect(addp9)
        self.pushPice_10 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_10.setGeometry(QtCore.QRect(180, 220, 141, 61))
        self.pushPice_10.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_10.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_10.setObjectName("pushPice_10")
        self.pushPice_10.setText(bt.p10)
        self.pushPice_10.clicked.connect(addp10)
        self.pushPice_11 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_11.setGeometry(QtCore.QRect(340, 220, 141, 61))
        self.pushPice_11.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_11.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_11.setObjectName("pushPice_11")
        self.pushPice_11.setText(bt.p11)
        self.pushPice_11.clicked.connect(addp11)
        self.pushPice_12 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_12.setGeometry(QtCore.QRect(500, 220, 141, 61))
        self.pushPice_12.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_12.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_12.setObjectName("pushPice_12")
        self.pushPice_12.setText(bt.p12)
        self.pushPice_12.clicked.connect(addp12)
        self.pushPice_13 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_13.setGeometry(QtCore.QRect(20, 310, 141, 61))
        self.pushPice_13.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_13.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_13.setObjectName("pushPice_13")
        self.pushPice_13.setText(bt.p13)
        self.pushPice_13.clicked.connect(addp13)
        self.pushPice_14 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_14.setGeometry(QtCore.QRect(180, 310, 141, 61))
        self.pushPice_14.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_14.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_14.setObjectName("pushPice_14")
        self.pushPice_14.setText(bt.p14)
        self.pushPice_14.clicked.connect(addp14)
        self.pushPice_15 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_15.setGeometry(QtCore.QRect(340, 310, 141, 61))
        self.pushPice_15.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_15.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_15.setObjectName("pushPice_15")
        self.pushPice_15.setText(bt.p15)
        self.pushPice_15.clicked.connect(addp15)
        self.pushPice_16 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushPice_16.setGeometry(QtCore.QRect(500, 310, 141, 61))
        self.pushPice_16.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPice_16.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55ffff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPice_16.setObjectName("pushPice_16")
        self.pushPice_16.setText(bt.p16)
        self.pushPice_16.clicked.connect(addp16)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.pushMeso_1 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_1.setGeometry(QtCore.QRect(20, 40, 141, 61))
        self.pushMeso_1.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_1.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_1.setObjectName("pushMeso_1")
        self.pushMeso_1.setText(bt.m1)
        self.pushMeso_1.clicked.connect(addm1)
        self.pushMeso_2 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_2.setGeometry(QtCore.QRect(180, 40, 141, 61))
        self.pushMeso_2.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_2.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_2.setObjectName("pushMeso_2")
        self.pushMeso_2.setText(bt.m2)
        self.pushMeso_2.clicked.connect(addm2)
        self.pushMeso_4 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_4.setGeometry(QtCore.QRect(500, 40, 141, 61))
        self.pushMeso_4.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_4.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_4.setObjectName("pushMeso_4")
        self.pushMeso_4.setText(bt.m4)
        self.pushMeso_4.clicked.connect(addm4)
        self.pushMeso_3 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_3.setGeometry(QtCore.QRect(340, 40, 141, 61))
        self.pushMeso_3.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_3.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_3.setObjectName("pushMeso_3")
        self.pushMeso_3.setText(bt.m3)
        self.pushMeso_3.clicked.connect(addm3)
        self.pushMeso_5 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_5.setGeometry(QtCore.QRect(20, 130, 141, 61))
        self.pushMeso_5.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_5.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_5.setObjectName("pushMeso_5")
        self.pushMeso_5.setText(bt.m5)
        self.pushMeso_5.clicked.connect(addm5)
        self.pushMeso_7 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_7.setGeometry(QtCore.QRect(340, 130, 141, 61))
        self.pushMeso_7.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_7.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_7.setObjectName("pushMeso_7")
        self.pushMeso_7.setText(bt.m7)
        self.pushMeso_7.clicked.connect(addm7)
        self.pushMeso_6 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_6.setGeometry(QtCore.QRect(180, 130, 141, 61))
        self.pushMeso_6.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_6.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_6.setObjectName("pushMeso_6")
        self.pushMeso_6.setText(bt.m6)
        self.pushMeso_6.clicked.connect(addm6)
        self.pushMeso_8 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_8.setGeometry(QtCore.QRect(500, 130, 141, 61))
        self.pushMeso_8.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_8.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_8.setObjectName("pushMeso_8")
        self.pushMeso_8.setText(bt.m8)
        self.pushMeso_8.clicked.connect(addm8)
        self.pushMeso_9 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_9.setGeometry(QtCore.QRect(20, 220, 141, 61))
        self.pushMeso_9.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_9.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_9.setObjectName("pushMeso_9")
        self.pushMeso_9.setText(bt.m9)
        self.pushMeso_9.clicked.connect(addm9)
        self.pushMeso_10 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_10.setGeometry(QtCore.QRect(180, 220, 141, 61))
        self.pushMeso_10.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_10.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_10.setObjectName("pushMeso_10")
        self.pushMeso_10.setText(bt.m10)
        self.pushMeso_10.clicked.connect(addm10)
        self.pushMeso_12 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_12.setGeometry(QtCore.QRect(500, 220, 141, 61))
        self.pushMeso_12.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_12.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_12.setObjectName("pushMeso_12")
        self.pushMeso_12.setText(bt.m12)
        self.pushMeso_12.clicked.connect(addm12)
        self.pushMeso_11 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_11.setGeometry(QtCore.QRect(340, 220, 141, 61))
        self.pushMeso_11.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_11.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_11.setObjectName("pushMeso_11")
        self.pushMeso_11.setText(bt.m11)
        self.pushMeso_11.clicked.connect(addm11)
        self.pushMeso_15 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_15.setGeometry(QtCore.QRect(340, 310, 141, 61))
        self.pushMeso_15.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_15.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_15.setObjectName("pushMeso_15")
        self.pushMeso_15.setText(bt.m15)
        self.pushMeso_15.clicked.connect(addm15)
        self.pushMeso_16 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_16.setGeometry(QtCore.QRect(500, 310, 141, 61))
        self.pushMeso_16.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_16.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_16.setObjectName("pushMeso_16")
        self.pushMeso_16.setText(bt.m16)
        self.pushMeso_16.clicked.connect(addm16)
        self.pushMeso_13 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_13.setGeometry(QtCore.QRect(20, 310, 141, 61))
        self.pushMeso_13.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_13.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_13.setObjectName("pushMeso_13")
        self.pushMeso_13.setText(bt.m13)
        self.pushMeso_13.clicked.connect(addm13)
        self.pushMeso_14 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushMeso_14.setGeometry(QtCore.QRect(180, 310, 141, 61))
        self.pushMeso_14.setMaximumSize(QtCore.QSize(141, 61))
        self.pushMeso_14.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #ff0000, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushMeso_14.setObjectName("pushMeso_14")
        self.pushMeso_14.setText(bt.m14)
        self.pushMeso_14.clicked.connect(addm14)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.pushPizza_1 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_1.setGeometry(QtCore.QRect(20, 40, 141, 61))
        self.pushPizza_1.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_1.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_1.setObjectName("pushPizza_1")
        self.pushPizza_1.setText(bt.pi1)
        self.pushPizza_1.clicked.connect(addpi1)
        self.pushPizza_2 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_2.setGeometry(QtCore.QRect(180, 40, 141, 61))
        self.pushPizza_2.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_2.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_2.setObjectName("pushPizza_2")
        self.pushPizza_2.setText(bt.pi2)
        self.pushPizza_2.clicked.connect(addpi2)
        self.pushPizza_3 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_3.setGeometry(QtCore.QRect(340, 40, 141, 61))
        self.pushPizza_3.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_3.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_3.setObjectName("pushPizza_3")
        self.pushPizza_3.setText(bt.pi3)
        self.pushPizza_3.clicked.connect(addpi3)
        self.pushPizza_7 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_7.setGeometry(QtCore.QRect(340, 130, 141, 61))
        self.pushPizza_7.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_7.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_7.setObjectName("pushPizza_7")
        self.pushPizza_7.setText(bt.pi7)
        self.pushPizza_7.clicked.connect(addpi7)
        self.pushPizza_6 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_6.setGeometry(QtCore.QRect(180, 130, 141, 61))
        self.pushPizza_6.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_6.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_6.setObjectName("pushPizza_6")
        self.pushPizza_6.setText(bt.pi6)
        self.pushPizza_6.clicked.connect(addpi6)
        self.pushPizza_5 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_5.setGeometry(QtCore.QRect(20, 130, 141, 61))
        self.pushPizza_5.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_5.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_5.setObjectName("pushPizza_5")
        self.pushPizza_5.setText(bt.pi5)
        self.pushPizza_5.clicked.connect(addpi5)
        self.pushPizza_4 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_4.setGeometry(QtCore.QRect(500, 40, 141, 61))
        self.pushPizza_4.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_4.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_4.setObjectName("pushPizza_4")
        self.pushPizza_4.setText(bt.pi4)
        self.pushPizza_4.clicked.connect(addpi4)
        self.pushPizza_8 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_8.setGeometry(QtCore.QRect(500, 130, 141, 61))
        self.pushPizza_8.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_8.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_8.setObjectName("pushPizza_8")
        self.pushPizza_8.setText(bt.pi8)
        self.pushPizza_8.clicked.connect(addpi8)
        self.pushPizza_9 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_9.setGeometry(QtCore.QRect(20, 220, 141, 61))
        self.pushPizza_9.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_9.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_9.setObjectName("pushPizza_9")
        self.pushPizza_9.setText(bt.pi9)
        self.pushPizza_9.clicked.connect(addpi9)
        self.pushPizza_10 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_10.setGeometry(QtCore.QRect(180, 220, 141, 61))
        self.pushPizza_10.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_10.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_10.setObjectName("pushPizza_10")
        self.pushPizza_10.setText(bt.pi10)
        self.pushPizza_10.clicked.connect(addpi10)
        self.pushPizza_11 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_11.setGeometry(QtCore.QRect(340, 220, 141, 61))
        self.pushPizza_11.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_11.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_11.setObjectName("pushPizza_11")
        self.pushPizza_11.setText(bt.pi11)
        self.pushPizza_11.clicked.connect(addpi11)
        self.pushPizza_12 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_12.setGeometry(QtCore.QRect(500, 220, 141, 61))
        self.pushPizza_12.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_12.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_12.setObjectName("pushPizza_12")
        self.pushPizza_12.setText(bt.pi12)
        self.pushPizza_12.clicked.connect(addpi12)
        self.pushPizza_13 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_13.setGeometry(QtCore.QRect(20, 310, 141, 61))
        self.pushPizza_13.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_13.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_13.setObjectName("pushPizza_13")
        self.pushPizza_13.setText(bt.pi13)
        self.pushPizza_13.clicked.connect(addpi13)
        self.pushPizza_14 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_14.setGeometry(QtCore.QRect(180, 310, 141, 61))
        self.pushPizza_14.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_14.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_14.setObjectName("pushPizza_14")
        self.pushPizza_14.setText(bt.pi14)
        self.pushPizza_14.clicked.connect(addpi14)
        self.pushPizza_16 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_16.setGeometry(QtCore.QRect(500, 310, 141, 61))
        self.pushPizza_16.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_16.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_16.setObjectName("pushPizza_16")
        self.pushPizza_16.setText(bt.pi16)
        self.pushPizza_16.clicked.connect(addpi16)
        self.pushPizza_15 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushPizza_15.setGeometry(QtCore.QRect(340, 310, 141, 61))
        self.pushPizza_15.setMaximumSize(QtCore.QSize(141, 61))
        self.pushPizza_15.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #55aaff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushPizza_15.setObjectName("pushPizza_15")
        self.pushPizza_15.setText(bt.pi15)
        self.pushPizza_15.clicked.connect(addpi15)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(710, 570, 361, 211))
        self.frame_4.setStyleSheet("background-color: rgb(136, 136, 136);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 341, 191))
        self.frame_2.setStyleSheet("background-color: rgb(255, 253, 171);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 10, 151, 51))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("change.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(ponisti)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 121, 51))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(oduzmi)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 150, 81))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font: 18pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("racun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(racunibutton)
        self.pushButton.clicked.connect(racunButtonDB)
        self.pushButton.clicked.connect(ponisti)







        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(10, 599, 231, 201))
        self.frame_5.setStyleSheet("background-color: rgb(136, 136, 136);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame = QtWidgets.QFrame(self.frame_5)
        self.frame.setGeometry(QtCore.QRect(10, 10, 211, 171))
        self.frame.setStyleSheet("background-color: rgb(255, 253, 171);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 20, 181, 61))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    font: 14pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(openPregled)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 100, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    font: 18pt \"Franklin Gothic Medium\";\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("slOdustani.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(close)


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 650, 301, 131))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 570, 61, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(466, 570, 71, 20))
        self.label_5.setStyleSheet("font: 10pt \"Franklin Gothic Medium\";")
        self.label_5.setObjectName("label_5")


        self.frame_5.raise_()
        self.frame_4.raise_()
        self.racunFrame.raise_()
        self.tabWidget.raise_()





        self.label_4.raise_()
        self.lineEdit.raise_()

        self.label_5.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "\"Van Reda\""))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "PIĆE"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "MESO"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "PIZZA"))
        self.pushButton_3.setText(_translate("MainWindow", "PONIŠTI"))
        self.pushButton_2.setText(_translate("MainWindow", "ODUZMI"))
        self.pushButton.setText(_translate("MainWindow", "RAČUN"))
        self.pushButton_6.setText(_translate("MainWindow", "PREGLED RAČUNA"))
        self.pushButton_5.setText(_translate("MainWindow", "IZLAZ"))


        self.label_5.setText(_translate("MainWindow", "KONOBAR:"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Rac_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
