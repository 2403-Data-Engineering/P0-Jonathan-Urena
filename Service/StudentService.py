from Models.Student import Student
from Data import StudentDAO


class StudentService:
    
        
    def save(self,student: Student) -> Student:
        StudentDAO.create_student(student)
        return student
    
    def findAll(self):
        StudentDAO.get_all_students()
    
    def findAllClasses(self,id:int):
        result = StudentDAO.get_student_classes(id)
        return result
    
    def findEnrollment(self,id:int) -> bool:
        result = StudentDAO.get_enrollment(id)
        if not result:
            return None
        return True

#Returns true if found in table or false otherwise
    def findById(self,id:int) -> int:
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

    def deleteById(self,id:int):
        get_id = self.findById(id)
        if not get_id:
            return None
        StudentDAO.delete_student(get_id)


    def enroll(self,student_id:int,class_id:int):
        StudentDAO.enroll_in_class(student_id,class_id)
    
    def drop(self,student_id:int,class_id:int):
        StudentDAO.drop_in_class(student_id,class_id)
        
    def getStudentById(self,id:int) -> int:
        result = StudentDAO.get_student_by_id(id)
        
        if not result:
            return None
        #found_student = Student(result["first_name"],result["last_name"],result["email"],result["major"],result["year"],result["id"])
        return result