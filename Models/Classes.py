from dataclasses import dataclass

@dataclass
class Classes:
    id : int
    class_name: str
    professor_id:int

    def __init__(self,class_name: str,professor_id:int,id=None):
        self.id = id
        self.class_name = class_name
        self.professor_id = professor_id

    def setId(self,id: int):
        self.id = id

    
   