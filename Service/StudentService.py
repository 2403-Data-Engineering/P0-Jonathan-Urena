from Models.Student import Student
from Data import StudentDAO

class StudentService:
    
        
    def save(self,student: Student) -> Student:
        StudentDAO.create_student(student)
        #return student
    
    #Create findById
    #Use findById to create delete/update By Id