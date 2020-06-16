# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changesection.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from database import *

class Ui_changeSection(object):

    def __init__(self,message):
        print("username su: " + str(message[0]))
        self.information = message[0]
    
    def listSection1(self):
        if(self.combolist.currentText()!="Select a course"):
            db_connection = DatabaseConnection()
            for i in self.classList:
                if(i.split(" ")[0] == self.combolist.currentText().split("-")[0]):
                    #print(i)
                    #print(db_connection.listOfSections(i.split(" ")[1]))
                    index = 1
                    for ii in db_connection.listOfSections(i.split(" ")[1]):
                        #print(self.combolist.currentText().split("-")[1])
                        if(str(ii[0])!=self.combolist.currentText().split("-")[1]):
                            if(ii[2]>0):
                                self.combosec.addItem("")
                                self.combosec.setItemText(index, str(ii[0]))
                                index = index + 1
                    if(index==1):
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("There is no other avaiable section")
                        msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please select a class")
            msg.exec_()
            
    def updateSectionNo(self):
        db_connection = DatabaseConnection()
        for i in self.classList:
            if(i.split(" ")[0] == self.combolist.currentText().split("-")[0]):
                db_connection.updateSection(str(self.information[0]),i.split(" ")[1],self.combosec.currentText())
                msg = QMessageBox()
                msg.setWindowTitle("Success")
                msg.setText("Your Section is Updated")
                msg.exec_()
                changedone = self.combolist.currentText().split("-")[0]
                changedsec = self.combosec.currentText()
                self.combosec.clear()
                self.combolist.clear()
                self.combosec.addItem("")
                self.combosec.setItemText(0,"Select a course")
                self.combosec.setCurrentIndex(0)
                self.combolist.addItem("")
                self.combolist.setItemText(0,"Select the section")
                self.combolist.setCurrentIndex(0)
                self.classList =db_connection.getStudentInformation2(str(self.information[0]))
                index = 1
                try:
                    for i in self.classList:
                        print(i)
                        self.combolist.addItem("")
                        if(i.split(" ")[0] == changedone):
                            self.combolist.setItemText(index, changedone + "-" + changedsec)
                        else:
                            self.combolist.setItemText(index, i.split(" ")[0] + "-" + i.split(" ")[2])
                        index = index + 1
                except:
                    self.combolist.addItem("")
                    self.combolist.setItemText(1,"No class")
                
            
    def setupUi(self, changeSection):
        changeSection.setObjectName("changeSection")
        db_connection = DatabaseConnection()
        changeSection.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(changeSection)
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
        changeSection.setCentralWidget(self.centralwidget)

        self.retranslateUi(changeSection)
        QtCore.QMetaObject.connectSlotsByName(changeSection)
        
        self.combolist = QtWidgets.QComboBox(self.centralwidget)
        self.combolist.setGeometry(QtCore.QRect(100,250,231,121))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.combolist.setFont(font)
        self.combolist.setObjectName("combolist")
        self.combolist.addItem("")
        self.combolist.setItemText(0,"Select a course")
        self.combolist.setCurrentIndex(0)
        self.combosec = QtWidgets.QComboBox(self.centralwidget)
        self.combosec.setGeometry(QtCore.QRect(400,250,231,121))
        self.combosec.setFont(font)
        self.combosec.setObjectName("combosec")
        self.combosec.addItem("")
        self.combosec.setItemText(0,"Select the section")
        self.combosec.setCurrentIndex(0)
        self.classList =db_connection.getStudentInformation2(str(self.information[0]))
        index = 1
        try:
            for i in self.classList:
                print(i)
                self.combolist.addItem("")
                self.combolist.setItemText(index, i.split(" ")[0] + "-" + i.split(" ")[2])
                index = index + 1
        except:
            self.combolist.addItem("")
            self.combolist.setItemText(1,"No class")
        self.listSection = QtWidgets.QPushButton(self.centralwidget)
        self.listSection.setGeometry(QtCore.QRect(220, 390, 130, 32))
        self.listSection.setObjectName("selectClass")
        self.listSection.setText("List Sections")
        self.listSection.clicked.connect(self.listSection1)
        self.updateSectionN = QtWidgets.QPushButton(self.centralwidget)
        self.updateSectionN.setGeometry(QtCore.QRect(360, 390, 130, 32))
        self.updateSectionN.setObjectName("updateSectionN")
        self.updateSectionN.setText("Update Section")
        self.updateSectionN.clicked.connect(self.updateSectionNo)

    def retranslateUi(self, changeSection):
        _translate = QtCore.QCoreApplication.translate
        changeSection.setWindowTitle(_translate("changeSection", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changeSection = QtWidgets.QMainWindow()
    ui = Ui_changeSection()
    ui.setupUi(changeSection)
    changeSection.show()
    sys.exit(app.exec_())
