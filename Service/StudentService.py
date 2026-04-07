from Models.Student import Student
from Data import StudentDAO

class StudentService:
    
        
    def save(self,student: Student) -> Student:
        StudentDAO.create_student(student)
        return student
    
    def findAll(self):
        StudentDAO.get_all_students()

#Returns true if found in table or false otherwise
    def findById(self,id:int) -> Student:
        result = StudentDAO.get_student_by_id(id)
        
        if not result:
            return None
        #found_student = Student(result["first_name"],result["last_name"],result["email"],result["major"],result["year"],result["id"])
        return result["id"]
    
    def updateById(self,id:int,updated_student):
        get_id = self.findById(id)
        if not get_id:
            return None
        updated_student.setId(get_id)
        
        StudentDAO.update_student(updated_student)
        
        
    #Create findById
    #Use findById to create delete/update By Id
    