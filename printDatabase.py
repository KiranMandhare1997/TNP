import sqlite3
class DatabaseConnection:	
   
   def __init__(self):
   	  self.conn=sqlite3.connect('student.db')
    
   def displayTable(self):
          Q="select * from studentInfo ";
          cursor=self.conn.execute(Q)
	  for attribute in cursor:
		print attribute[0],"    ",attribute[1],"\n"
	
   def create(self):
           Q="create table if not exists studentInfo(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,EMAIL VARCHAR(100) NOT NULL,PHONE NUMERIC);"
           self.conn.execute(Q)
    
   def insert(self,student):
         Q="insert into studentInfo values (?, ?, ?, ?);"
	 cursor=self.conn.execute(Q,(student.rollNo,student.name,student.email,student.phone))
	 self.conn.commit()
   def closeConnection(self):
	 self.conn.close()      

class Student:
   studentCount=0;
   def  _init_(self,rollNo,name,email,phone):
 	self.rollNo=rollNo   
 	self.name=name
        self.email=email
        self.phone=phone
        Student.studentCount+=1;
   def readData(self):
      	self.name=raw_input('Enter your name: ')
        self.rollNo=input('Enter your rollNo: ')
        self.email=raw_input('Enter your email: ')
        self.phone=input('Enter your phone: ')
   def displayStudentNumber(self):
        print "Total Employee %d" %Student.studentCount
   def displayStudent(self):
        print rollNo,"      	",name,"     	 ",email,"    	",phone

db=DatabaseConnection()
stud=Student()
while 1:
     print("""
                   Enter the operation to perform :\n
	           1.Create Table
	   	   2.Insert New Record
 	           3.Display Table
	           4.Exit
                """)
     choice=input("Select the input : ")
     if choice==1:
	  db.create()
     elif choice==2:
               stud.readData()     
     	       db.insert(stud)	
     elif choice==3:
	  db.displayTable()
     elif choice==4:
          db.closeConnection()
	  break
     
