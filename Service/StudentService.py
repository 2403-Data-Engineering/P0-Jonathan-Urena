from Models.Student import Student
from Data import StudentDAO

class StudentService:
    
        
    def save(self,student: Student) -> Student:
        StudentDAO.create_student(student)
        return student
    
    def findAll(self):
        StudentDAO.get_all_students()
    #Create findById
    #Use findById to create delete/update By Id
    