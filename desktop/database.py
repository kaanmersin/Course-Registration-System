import mysql.connector  
import hashlib

class DatabaseConnection():

	def __init__(self):    
		self.cnx = mysql.connector.connect(user='kole', password='Scrool12*',
								  host='167.71.66.201',
								  database='471DB')
		self.cursor = self.cnx.cursor()
		
	def query(self, query_str):
	   cursor = self.cursor
	   cursor.execute(query_str)
	   result = cursor.fetchall()
	   #print(result)
	   return result

	def queryinsertdelete(self,query_str):
		cursor = self.cursor
		cursor.execute(query_str)
		self.cnx.commit()

	def show_columns(self, table_name):
		query = "SHOW COLUMNS FROM " + table_name
		self.query(query)

	def close_conn(self):
		self.cnx.close()
			
	def loginCheck(self, username, password):
		m = hashlib.sha1()
		m.update(password.encode('utf-8'))
		encyrpted = m.hexdigest()
		result = "noone"
		query = "SELECT * FROM UsersStudent WHERE userid= '" + username + "' AND password= '" + encyrpted +"'"
		queryfinal = self.query(query)
		if(len(queryfinal)==0):
			query = query = "SELECT * FROM UsersInstructor WHERE userid= '" + username + "' AND password= '" + encyrpted +"'"
			queryfinal = self.query(query)
			if(len(queryfinal)!=0):
				result =  "instructor"
		else:
			result = "student"
		return result

	def getStudentInformation(self,username):
		output=[]
		query = "SELECT * FROM StudentTakenCourse WHERE studentID= '" + username + "'"
		queryfinal = self.query(query)
		if(len(queryfinal)>0):
			for result in queryfinal:
				query2 = "SELECT * FROM Class WHERE classID= '" + str(result[1]) + "'"
				information = self.query(query2)
				section = str(result[2])
				timeinfo = str(information[0][3]) + " " + str(information[0][2])
				courseID = str(information[0][1])
				query3 = "SELECT * FROM Course WHERE courseID= '" + str(courseID) + "'"
				linformation = self.query(query3)
				name = linformation[0][1]
				credit = linformation[0][3]
				output.append(name + "   " + section+ "       " +timeinfo + "   " + str(credit))
			return output

	def getTakenCourses(self, studentID):
		query = "SELECT classID FROM StudentTakenCourse WHERE studentID= '" + str(studentID) + "'"
		return self.query(query)

	def getStudentInformation2(self,username):
		output=[]
		query = "SELECT * FROM StudentTakenCourse WHERE studentID= '" + username + "'"
		queryfinal = self.query(query)
		if(len(queryfinal)>0):
			for result in queryfinal:
				query2 = "SELECT * FROM Class WHERE classID= '" + str(result[1]) + "'"
				information = self.query(query2)
				courseID = str(information[0][1])
				query3 = "SELECT * FROM Course WHERE courseID= '" + str(courseID) + "'"
				linformation = self.query(query3)
				name = linformation[0][1]
				output.append(name + " " + str(result[1]) + " " + str(result[2]))
			return output

	def getStudentPersonal(self,username):
		query = "SELECT * FROM Student WHERE studentID= '" + username + "'"
		queryfinal = self.query(query)
		return queryfinal

	def getDepartmentName(self,departmentID):

		print(departmentID)
		query = "SELECT * FROM Department WHERE departmentID= '" + str(departmentID) + "'"
		queryfinal = self.query(query)
		return queryfinal[0][1]

	def deleteCourse(self,username,classID):
		query = "DELETE FROM StudentTakenCourse WHERE studentID='" + username + "' AND classID='"+ classID + "'"
		self.queryinsertdelete(query)

	def listOfSections(self,classID):
		query = "SELECT * FROM Section WHERE classID= '" + str(classID) + "'"
		queryfinal = self.query(query)
		return queryfinal

	def listOfSectionsByView(self,courseCode):
		query = "SELECT sectionID, quota FROM joincourseclasssection WHERE CourseCode= '" + str(CourseCode) + "'"
		queryfinal = self.query(query)
		return queryfinal	

	def updateSection(self,username,classID,newSection):
		query = "UPDATE StudentTakenCourse SET sectionID ='" + str(newSection) + "' WHERE studentID='" + username + "'AND classID='" + classID + "'"
		self.queryinsertdelete(query)

	def enrollClass(self, studentID, classID, sectionID):
		query = "INSERT INTO `StudentTakenCourse`(studentID, classID, sectionID) VALUES (" + str(studentID) + "," + str(classID) + "," + str(sectionID) + ");"
		print(query)
		self.queryinsertdelete(query)

	def updateSection(self, studentID, classID, newSectionID):
		inputs = [studentID, classID, newSectionID]
		result = self.cursor.callproc("updateMySection", inputs)
		print(result)
		print("section updated")

	def getTheDepartmentsOpenCourses(self, year, term, depid):
		inputs = [year, term, depid]
		result = self.cursor.callproc("myDepartmentOpenCourse", inputs)
		fetched = [result.fetchall() for result in self.cursor.stored_results()]
		return fetched[0]

	def getAllInformation(self,name):
		query = "SELECT * FROM " + str(name) 
		queryfinal = self.query(query)
		return queryfinal

	def getColumnNames(self,name):
		query = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" + str(name) + "'"
		queryfinal = self.query(query)
		return queryfinal

if __name__ == "__main__":
	# This is for testing

	get_student_user = "SELECT * FROM UsersStudent LIMIT 5"
	get_instructor_user = "SELECT * FROM UsersInstructor LIMIT 5"
	db_conn = DatabaseConnection()
	db_conn.getTheDepartmentsOpenCourses(2019, "Fall",1)
	print(db_conn.show_columns("StudentTakenCourse"))
