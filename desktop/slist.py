# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentlist.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_studentList(object):

    def __init__(self,message):
        print("username su: " + message)
        self.adminID = message

    def setupUi(self, studentList):
        studentList.setObjectName("studentList")
        studentList.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(studentList)
        self.centralwidget.setObjectName("centralwidget")
        self.departmentID = QtWidgets.QLineEdit(self.centralwidget)
        self.departmentID.setGeometry(QtCore.QRect(130, 130, 113, 21))
        self.departmentID.setObjectName("departmentID")
        self.nameSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.nameSurname.setGeometry(QtCore.QRect(130, 90, 113, 21))
        self.nameSurname.setObjectName("nameSurname")
        studentList.setCentralWidget(self.centralwidget)

        self.retranslateUi(studentList)
        QtCore.QMetaObject.connectSlotsByName(studentList)

    def retranslateUi(self, studentList):
        _translate = QtCore.QCoreApplication.translate
        studentList.setWindowTitle(_translate("studentList", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studentList = QtWidgets.QMainWindow()
    ui = Ui_studentList()
    ui.setupUi(studentList)
    studentList.show()
    sys.exit(app.exec_())
