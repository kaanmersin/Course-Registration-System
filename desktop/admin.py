# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminView.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from main import Ui_LoginScreen
from tableView import Ui_MainWindow
from database import *
from PyQt5.QtWidgets import QMessageBox

class Ui_AdminView(object):

    def __init__(self,message):
        print("username su: " + message)
        self.adminID = message
    
    def listAll1(self):
        if(self.combolist.currentText()!="Select a Table"):
            db_connection = DatabaseConnection()
            self.result = db_connection.getAllInformation(self.combolist.currentText())
            self.result2 = db_connection.getColumnNames(self.combolist.currentText())
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow(self.result,self.result2)
            self.ui.setupUi(self.window)
            #AdminView.hide()
            self.window.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please select a table")
            msg.exec_()
    def openStat1(self):
        if(self.combolist.currentText()!="Select a Table"):
            db_connection = DatabaseConnection()
            result = db_connection.getAllInformation(self.combolist.currentText())
            result2 = self.result2 = db_connection.getColumnNames(self.combolist.currentText())
            
            writing = "Number of entries = " + str(len(result))
            writing2 = ""
            for i in result2:
                writing2 = writing2 + i[3]+ "-"
            writing = writing + "\nColumn names are:" + writing2
            writing = writing[:-1]
            self.textEdit.append(writing)
            #self.textEdit.setText(writing)
            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please select a table")
            msg.exec_()
    def setupUi(self, AdminView):
        AdminView.setObjectName("AdminView")
        AdminView.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AdminView)
        self.centralwidget.setObjectName("centralwidget")
        self.combolist = QtWidgets.QComboBox(self.centralwidget)
        self.combolist.setGeometry(QtCore.QRect(100,250,231,121))
        self.openStat = QtWidgets.QPushButton(self.centralwidget)
        self.openStat.setGeometry(QtCore.QRect(220, 390, 130, 32))
        self.openStat.setObjectName("openStat")
        self.openStat.setText("Open Statics")
        self.openStat.clicked.connect(self.openStat1)
        self.listAll = QtWidgets.QPushButton(self.centralwidget)
        self.listAll.setGeometry(QtCore.QRect(360, 390, 130, 32))
        self.listAll.setObjectName("listAll")
        self.listAll.setText("Open the Table")
        self.listAll.clicked.connect(self.listAll1)
        self.combolist.addItem("")
        self.combolist.setItemText(0,"Select a Table")
        self.combolist.setCurrentIndex(0)
        self.combolist.addItem("")
        self.combolist.setItemText(1,"Class")
        self.combolist.addItem("")
        self.combolist.setItemText(2,"Course")
        self.combolist.addItem("")
        self.combolist.setItemText(3,"Department")
        self.combolist.addItem("")
        self.combolist.setItemText(4,"Faculty")
        self.combolist.addItem("")
        self.combolist.setItemText(5,"Instructor")
        self.combolist.addItem("")
        self.combolist.setItemText(6,"InstructorGivesCourse")
        self.combolist.addItem("")
        self.combolist.setItemText(7,"PrerequisiteCourses")
        self.combolist.addItem("")
        self.combolist.setItemText(8,"Section")
        self.combolist.addItem("")
        self.combolist.setItemText(9,"Student")
        self.combolist.addItem("")
        self.combolist.setItemText(10,"StudentHasGradedClass")
        self.combolist.addItem("")
        self.combolist.setItemText(11,"StudentTakenCourse")
        self.combolist.addItem("")
        self.combolist.setItemText(12,"UsersInstructor")
        self.combolist.addItem("")
        self.combolist.setItemText(13,"UsersStudent")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(500, 120, 281, 281))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        
        
#        self.logOut.clicked.connect(self.OpenWindow)
        
        AdminView.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminView)
        QtCore.QMetaObject.connectSlotsByName(AdminView)

    def retranslateUi(self, AdminView):
        _translate = QtCore.QCoreApplication.translate
        AdminView.setWindowTitle(_translate("AdminView", "MainWindow"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminView = QtWidgets.QMainWindow()
    ui = Ui_AdminView()
    ui.setupUi(AdminView)
    AdminView.show()
    sys.exit(app.exec_())
