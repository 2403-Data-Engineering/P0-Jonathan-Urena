from dataclasses import dataclass

@dataclass
class Class:
    id : int
    class_name: str

    def __init__(self,class_name: str):
        self.id = 0
        self.class_name = class_name
   