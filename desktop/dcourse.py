# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deletecourse.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from database import *
import sys
import os

class Ui_deleteCourse(object):

    def __init__(self,message):
        print("username su: " + str(message[0]))
        self.information = message[0]
        
    def deleteSecCourse(self):
        db_connection = DatabaseConnection()
        for i in self.classList:
            if(i.split(" ")[0] == self.combolist.currentText()):
                print(i)
                db_connection.deleteCourse(str(self.information[0]),str(i.split(" ")[1]))
                print("silindi")
        self.combolist.clear()

        self.combolist.addItem("")
        self.combolist.setItemText(0,"Select a course")
        self.combolist.setCurrentIndex(0)
        index=1
        self.classList =db_connection.getStudentInformation2(str(self.information[0]))
        try:
            for i in self.classList:
                self.combolist.addItem("")
                self.combolist.setItemText(index,i.split(" ")[0])
                index = index + 1
        except:
            self.combolist.addItem("")
            self.combolist.setItemText(1,"No class")
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Class dropped")
        msg.exec_()
        
        #self.classList
        #print(self.combolist.currentText())
        
    def setupUi(self, deleteCourse):
        deleteCourse.setObjectName("deleteCourse")
        db_connection = DatabaseConnection()
        deleteCourse.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(deleteCourse)
        self.centralwidget.setObjectName("centralwidget")
        self.studentNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.studentNumber.setGeometry(QtCore.QRect(20, 90, 180, 21))
        self.studentNumber.setObjectName("studentNumber")
        self.studentNumber.setText(str(self.information[0]))
        self.studentNumber.setReadOnly(True)
        self.departmentName = QtWidgets.QLineEdit(self.centralwidget)
        self.departmentName.setGeometry(QtCore.QRect(20, 130, 180, 21))
        self.departmentName.setObjectName("departmentName")
        self.departmentName.setText(db_connection.getDepartmentName(self.information[7]))
        self.departmentName.setReadOnly(True)
        self.nameSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.nameSurname.setGeometry(QtCore.QRect(20, 50, 180, 21))
        self.nameSurname.setObjectName("nameSurname")
        self.nameSurname.setText(self.information[1] + " " + self.information[2])
        self.nameSurname.setReadOnly(True)
        deleteCourse.setCentralWidget(self.centralwidget)

        self.retranslateUi(deleteCourse)
        QtCore.QMetaObject.connectSlotsByName(deleteCourse)

        self.combolist = QtWidgets.QComboBox(self.centralwidget)
        self.combolist.setGeometry(QtCore.QRect(100,250,231,121))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.combolist.setFont(font)
        self.combolist.setObjectName("combolist")
        self.combolist.addItem("")
        self.combolist.setItemText(0,"Select a course")
        self.combolist.setCurrentIndex(0)
        index=1
        self.classList =db_connection.getStudentInformation2(str(self.information[0]))
        try:
            for i in self.classList:
                self.combolist.addItem("")
                self.combolist.setItemText(index,i.split(" ")[0])
                index = index + 1
        except:
            self.combolist.addItem("")
            self.combolist.setItemText(1,"No class")
        self.selectClass = QtWidgets.QPushButton(self.centralwidget)
        self.selectClass.setGeometry(QtCore.QRect(320, 390, 113, 32))
        self.selectClass.setObjectName("selectClass")
        self.selectClass.setText("Drop Class")
        self.selectClass.clicked.connect(self.deleteSecCourse)
        
    def retranslateUi(self, deleteCourse):
        _translate = QtCore.QCoreApplication.translate
        deleteCourse.setWindowTitle(_translate("deleteCourse", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteCourse = QtWidgets.QMainWindow()
    ui = Ui_deleteCourse()
    ui.setupUi(deleteCourse)
    deleteCourse.show()
    sys.exit(app.exec_())
