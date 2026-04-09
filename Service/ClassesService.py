from Models.Classes import Classes
from Data import ClassesDAO

class ClassesService:
    
        
    def save(self,classes: Classes) -> Classes:
        ClassesDAO.create_classes(classes)
        return classes
    
    def findAll(self):
        ClassesDAO.get_all_classes()

    def findAllEnrolled(self,id:int):
        result = ClassesDAO.get_student_enrolled(id)
        return result

#Returns true if found in table or false otherwise
    def findById(self,id:int) -> Classes:
        result = ClassesDAO.get_classes_by_id(id)
        
        if not result:
            return None
        #found_classes = Classes(result["first_name"],result["last_name"],result["email"],result["major"],result["year"],result["id"])
        return result["id"]
    
    def updateById(self,id:int,updated_classes):
        get_id = self.findById(id)
        if not get_id:
            return None
        updated_classes.setId(get_id)
        
        ClassesDAO.update_classes(updated_classes)

    def deleteById(self,id:int):
        get_id = self.findById(id)
        if not get_id:
            return None
        ClassesDAO.delete_classes(id)
        
        
    #Create findById
    #Use findById to create delete/update By Id
    