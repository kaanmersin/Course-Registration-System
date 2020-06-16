# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentView.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from main import Ui_LoginScreen
from acourse import Ui_addingCourse
from dcourse import Ui_deleteCourse
from csection import Ui_changeSection
from database import *

class Ui_StudentView(object):
    def __init__(self,message):
        print("username su: " + message)
        self.studentID = message
        
    def openAddCourse(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_addingCourse(self.personalInfo)
        self.ui.setupUi(self.window)
        #AdminView.hide()
        self.window.show()
        
    def openDeleteCourse(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_deleteCourse(self.personalInfo)
        self.ui.setupUi(self.window)
        #AdminView.hide()
        self.window.show()
        
    def openChangeSection(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_changeSection(self.personalInfo)
        self.ui.setupUi(self.window)
        #AdminView.hide()
        self.window.show()
    def refreshPage(self):
        db_connection = DatabaseConnection()
        writing = "Name      Section     Term          Credit\n"
        try:
            for i in db_connection.getStudentInformation(self.studentID):
                writing= writing + i + "\n"
        except:
            writing = "Basket empty"
        self.textEdit.setText(writing)
        self.personalInfo = db_connection.getStudentPersonal(self.studentID)
        self.creditLimit.setText("Remaining Credit: " + str(self.personalInfo[0][3]))
    def setupUi(self, StudentView):
        db_connection = DatabaseConnection()
        self.personalInfo = db_connection.getStudentPersonal(self.studentID)
        StudentView.setObjectName("StudentView")
        StudentView.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(StudentView)
        self.centralwidget.setObjectName("centralwidget")
        self.nameSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.nameSurname.setGeometry(QtCore.QRect(20, 75, 180, 21))
        self.nameSurname.setObjectName("nameSurname")
        self.nameSurname.setText(self.personalInfo[0][1] + " " + self.personalInfo[0][2])
        self.nameSurname.setReadOnly(True)
        self.studentNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.studentNumber.setGeometry(QtCore.QRect(20, 100, 180, 21))
        self.studentNumber.setObjectName("studentNumber")
        self.studentNumber.setText(str(self.personalInfo[0][0]))
        self.studentNumber.setReadOnly(True)
        self.departmentName = QtWidgets.QLineEdit(self.centralwidget)
        self.departmentName.setGeometry(QtCore.QRect(20, 125, 180, 21))
        self.departmentName.setObjectName("departmentName")
        self.departmentName.setText(db_connection.getDepartmentName(self.personalInfo[0][7]))
        self.departmentName.setReadOnly(True)
        self.creditLimit = QtWidgets.QLineEdit(self.centralwidget)
        self.creditLimit.setGeometry(QtCore.QRect(20, 150, 180, 21))
        self.creditLimit.setObjectName("remainingCredit")
        self.creditLimit.setText("Remaining Credit: " + str(self.personalInfo[0][3]))
        self.creditLimit.setReadOnly(True)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(480, 230, 281, 281))
        self.textEdit.setObjectName("textEdit")
        writing = "Name      Section     Term          Credit\n"
        try:
            for i in db_connection.getStudentInformation(self.studentID):
                writing= writing + i + "\n"
        except:
            writing = "Basket empty"
        self.textEdit.setText(writing)
        self.textEdit.setReadOnly(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 200, 141, 16))
        self.label.setObjectName("label")
        self.enrollClass = QtWidgets.QPushButton(self.centralwidget)
        self.enrollClass.setGeometry(QtCore.QRect(130, 250, 121, 32))
        self.enrollClass.setObjectName("enrollClass")
        
        self.enrollClass.clicked.connect(self.openAddCourse)
        
        self.dropClass = QtWidgets.QPushButton(self.centralwidget)
        self.dropClass.setGeometry(QtCore.QRect(130, 290, 121, 32))
        self.dropClass.setObjectName("dropClass")
        
        self.dropClass.clicked.connect(self.openDeleteCourse)
        
        
        self.updateSection = QtWidgets.QPushButton(self.centralwidget)
        self.updateSection.setGeometry(QtCore.QRect(130, 330, 121, 32))
        self.updateSection.setObjectName("updateSection")
        
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(480, 60, 130, 32))
        self.refresh.setObjectName("updateSectionN")
        self.refresh.setText("Refresh")
        self.refresh.clicked.connect(self.refreshPage)
        
        self.updateSection.clicked.connect(self.openChangeSection)
        
        
        
        #self.logOut.clicked.connect(self.Loggingout)
        
        StudentView.setCentralWidget(self.centralwidget)

        self.retranslateUi(StudentView)
        QtCore.QMetaObject.connectSlotsByName(StudentView)

    def retranslateUi(self, StudentView):
        _translate = QtCore.QCoreApplication.translate
        StudentView.setWindowTitle(_translate("StudentView", "MainWindow"))
        self.label.setText(_translate("StudentView", "Classes"))
        self.enrollClass.setText(_translate("StudentView", "Enroll to Class"))
        self.dropClass.setText(_translate("StudentView", "Drop Class"))
        self.updateSection.setText(_translate("StudentView", "Update Section"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentView = QtWidgets.QMainWindow()
    ui = Ui_StudentView()
    ui.setupUi(StudentView)
    StudentView.show()
    sys.exit(app.exec_())
