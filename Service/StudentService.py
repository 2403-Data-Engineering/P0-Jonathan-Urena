from Models.Student import Student
from Data import StudentDAO
from Data import db_connection_manager
class StudentService:
    
        
    def save(self,student: Student) -> Student:
        #db_connection_manager.get_connection()
        StudentDAO.create_student()
        return student
    
    #Create findById
    #Use findById to create delete/update By Id