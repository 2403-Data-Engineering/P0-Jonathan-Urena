from Models.Professor import Professor
from Data import ProfessorDAO

class ProfessorService:
    
        
    def save(self,professor: Professor) -> Professor:
        ProfessorDAO.create_professor(professor)
        return professor
    
    def findAll(self):
        ProfessorDAO.get_all_professors()

    #returns id and class_name of all courses teaching
    def findTeaching(self,id:int) -> list[dict]:
        result = ProfessorDAO.get_teaching(id)
        if not result:
            return None
        return result


#Returns true if found in table or false otherwise
    def findById(self,id:int) -> Professor:
        result = ProfessorDAO.get_professor_by_id(id)
        if not result:
            return None
        #found_professor = Professor(result["first_name"],result["last_name"],result["email"],result["major"],result["year"],result["id"])
        return result["id"]
    
    def updateById(self,id:int,updated_professor):
        get_id = self.findById(id)
        if not get_id:
            return None
        updated_professor.setId(get_id)
        
        ProfessorDAO.update_professor(updated_professor)

    def deleteById(self,id:int):
        get_id = self.findById(id)
        if not get_id:
            return None
        ProfessorDAO.delete_professor(id)
        
    #returns professor info
    def getProfessorById(self,id:int) -> int:
        result = ProfessorDAO.get_professor_by_id(id)
        if not result:
            return None
        return result
    