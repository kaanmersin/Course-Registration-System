# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableViewAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

class Ui_MainWindow(object):

    def __init__(self,result,result2):
        self.result = result
        self.column_name = result2
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Sql Table")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.sqlTable = QTableWidget(self.centralwidget)
        self.sqlTable.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.sqlTable.setMaximumSize(QtCore.QSize(800, 600))
        self.sqlTable.setObjectName("sqlTable")
        self.sqlTable.setRowCount(0)
        self.sqlTable.setColumnCount(len(self.column_name))
        
        for row_number,row_data in enumerate(self.result):
            self.sqlTable.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.sqlTable.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        new_column = []
        for i in self.column_name:
            new_column.append(i[3])
        self.sqlTable.setHorizontalHeaderLabels(new_column)
#        index = 0
#        for i in column_name:
#            #self.sqlTable.setHeaderData(index, str(i[3]))
#            self.sqlTable.tableWidgetTextureLibrary.horizontalHeaderItem(index).setText(str(i[3]));
#            index = index + 1
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Sql Table", "Sql Table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
