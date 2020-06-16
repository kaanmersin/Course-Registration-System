# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginscreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from student import Ui_StudentView
from admin import Ui_AdminView
from database import *

class Ui_LoginScreen(object):

    def OpenWindow(self):
        username= self.username.text()
        password= self.password.text()
        if(len(username)>0):
            if(len(password)>0):
                db_connection = DatabaseConnection()
                #print(db_connection.loginCheck(username,password))
                panel = db_connection.loginCheck(username,password)
                print(panel)
                if(panel!="noone"):
                    self.message = username
                    
                    if(panel=="student"):
                        self.ui = Ui_StudentView(self.message)
                    else:
                        self.ui = Ui_AdminView(self.message)
                    self.window = QtWidgets.QMainWindow()
                    self.ui.setupUi(self.window)
                    LoginScreen.hide()
                    self.window.show()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Wrong username or password")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Please enter password")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please enter username")
            msg.exec_()
            
            
        
    def setupUi(self, LoginScreen):
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LoginScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(290, 310, 113, 32))
        self.loginButton.setObjectName("loginButton")
        
        self.loginButton.clicked.connect(self.OpenWindow)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 200, 81, 16))
        self.label.setObjectName("label")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(340, 240, 113, 21))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 240, 81, 16))
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(340, 200, 113, 21))
        self.username.setObjectName("username")
        LoginScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginScreen)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)

    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "MainWindow"))
        self.loginButton.setText(_translate("LoginScreen", "Login"))
        self.label.setText(_translate("LoginScreen", "Username:"))
        self.label_2.setText(_translate("LoginScreen", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginScreen = QtWidgets.QMainWindow()
    ui = Ui_LoginScreen()
    ui.setupUi(LoginScreen)
    LoginScreen.show()
    sys.exit(app.exec_())
