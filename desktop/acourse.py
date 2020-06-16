# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addcourse.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QSize
from database import *

class Ui_addingCourse(object):

	def __init__(self,message):
		print("username su: " + str(message[0]))
		self.information = message[0]
		self.remainingCredit = self.information[3]

	def ListSectionsOfCourse(self):
		if(self.combolist.currentText()!="Select a course"):
			db_connection = DatabaseConnection()
			selectedClass = self.combolist.currentText().split(" - ")[0].strip()
			print("selected class is",selectedClass)
			# sectionsOfClass = db_connection.listOfSections(selectedClass)
			sectionsOfClass = []
			for classInfo in self.classList:
				if(str(classInfo[1]) == selectedClass):
					sectionsOfClass.append(classInfo[8:10])
			# sectionsOfClass = [classInfo[8:10] for classInfo in self.classList if str(classInfo[0]) == selectedClass]
			print("sections are", sectionsOfClass)
			combo_idx = 1
			for section in sectionsOfClass:
				self.combosec.addItem("")
				itemtext = "Section Number #" + str(section[0]) + ", Total Quota:" + str(section[1])
				self.combosec.setItemText(combo_idx, itemtext)
				combo_idx = combo_idx + 1
			if(combo_idx==1):
				msg = QMessageBox()
				msg.setWindowTitle("Error")
				msg.setText("There is no other available section")
				msg.exec_()
		else:
			msg = QMessageBox()
			msg.setWindowTitle("Error")
			msg.setText("Please select a class")
			msg.exec_()

	def Enroll(self):
		if self.combolist.currentText()!="Select a course" and self.combosec.currentText()!="Select the section":
			db_connection = DatabaseConnection()
			classCode, className = self.combolist.currentText().split(" - ")[0], self.combolist.currentText().split(" - ")[1]
			classCredit = int((self.combolist.currentText().split(" - ")[2]).split(" ")[0][1:])
			sectionID = (self.combosec.currentText().split(", ")[0]).split("#")[1]
			classID = [classInfo[5] for classInfo in self.classList if classInfo[1] == classCode][0]
			takenCourses = [classCode[0] for classCode in db_connection.getTakenCourses(str(self.information[0]))]
			print("taken courses are:", takenCourses)
			if(classID in takenCourses):
				msg = QMessageBox()
				msg.setWindowTitle("Error")
				msg.setText("You have already enrolled to this class!")
				msg.exec_()
			elif(self.remainingCredit - classCredit < 0):
				msg = QMessageBox()
				msg.setWindowTitle("Error")
				msg.setText("You don't have enough credit left to enroll this class!")
				msg.exec_()
			else:
				print("classCode is", classCode)
				print("classID is", classID)
				print("sectionID is", sectionID)
				print("quota is")
				db_connection.enrollClass(self.information[0], classID, sectionID)
				self.creditLimit.setText("Remaining Credit: " + str(self.remainingCredit - classCredit))
				msg = QMessageBox()
				msg.setWindowTitle("Success")
				msg.setText("You have successfully enrolled to this class.")
				msg.exec_()

	def setupUi(self, addingCourse):
		db_connection = DatabaseConnection()
		addingCourse.setObjectName("addingCourse")
		addingCourse.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(addingCourse)
		self.centralwidget.setObjectName("centralwidget")
		self.departmentName = QtWidgets.QLineEdit(self.centralwidget)
		self.departmentName.setGeometry(QtCore.QRect(20, 130, 180, 21))
		self.departmentName.setObjectName("departmentName")
		self.departmentName.setText(db_connection.getDepartmentName(self.information[7]))
		self.departmentName.setReadOnly(True)
		self.studentNumber = QtWidgets.QLineEdit(self.centralwidget)
		self.studentNumber.setGeometry(QtCore.QRect(20, 90, 180, 21))
		self.studentNumber.setObjectName("studentNumber")
		self.studentNumber.setText(str(self.information[0]))
		self.studentNumber.setReadOnly(True)
		self.nameSurname = QtWidgets.QLineEdit(self.centralwidget)
		self.nameSurname.setGeometry(QtCore.QRect(20, 50, 180, 21))
		self.nameSurname.setObjectName("nameSurname")
		self.nameSurname.setText(self.information[1] + " " + self.information[2])
		self.nameSurname.setReadOnly(True)
		
		self.creditLimit = QtWidgets.QLineEdit(self.centralwidget)
		self.creditLimit.setGeometry(QtCore.QRect(20, 170, 180, 21))
		self.creditLimit.setObjectName("remainingCredit")
		self.creditLimit.setText("Remaining Credit: " + str(self.information[3]))
		self.creditLimit.setReadOnly(True)
		addingCourse.setCentralWidget(self.centralwidget)
		self.retranslateUi(addingCourse)
		QtCore.QMetaObject.connectSlotsByName(addingCourse)
		self.combolist = QtWidgets.QComboBox(self.centralwidget)
		self.combolist.setGeometry(QtCore.QRect(100,250,230,120))
		font = QtGui.QFont()
		font.setPointSize(13)
		self.combolist.setFont(font)
		self.combolist.setObjectName("combolist")
		self.combolist.addItem("")
		self.combolist.setItemText(0,"Select a course")
		self.combolist.setCurrentIndex(0)

		self.combosec = QtWidgets.QComboBox(self.centralwidget)
		self.combosec.setGeometry(QtCore.QRect(400,250,230,120))
		self.combosec.setFont(font)
		self.combosec.setObjectName("combosec")
		self.combosec.addItem("")
		self.combosec.setItemText(0,"Select the section")
		self.combosec.setCurrentIndex(0)

		self.classList = db_connection.getTheDepartmentsOpenCourses(2019, "Fall", int(self.information[7]))
		comboIndex = 1
		self.classHeaders = sorted(list(set([classInfo[1] + " - " + classInfo[2] + " - (" + str(classInfo[3]) + " Credit)"  for classInfo in self.classList])))
		try:
			for classHeader in self.classHeaders:
				self.combolist.addItem("")
				self.combolist.setItemText(comboIndex, classHeader)
				comboIndex = comboIndex + 1
		except Exception as e:
			print(e)
			self.combolist.addItem("")
			self.combolist.setItemText(1,"No class")

		self.listSection = QtWidgets.QPushButton(self.centralwidget)
		self.listSection.setGeometry(QtCore.QRect(200, 390, 130, 32))
		self.listSection.setObjectName("selectClass")
		self.listSection.setText("List Sections")
		self.listSection.clicked.connect(self.ListSectionsOfCourse)
		
		self.enrollClass = QtWidgets.QPushButton(self.centralwidget)
		self.enrollClass.setGeometry(QtCore.QRect(400, 390, 130, 32))
		self.enrollClass.setObjectName("Enroll")
		self.enrollClass.setText("Enroll")
		self.enrollClass.clicked.connect(self.Enroll)

	def retranslateUi(self, addingCourse):
		_translate = QtCore.QCoreApplication.translate
		addingCourse.setWindowTitle(_translate("addingCourse", "MainWindow"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	addingCourse = QtWidgets.QMainWindow()
	ui = Ui_addingCourse()
	ui.setupUi(addingCourse)
	addingCourse.show()
	sys.exit(app.exec_())
