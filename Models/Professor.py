from dataclasses import dataclass

@dataclass
class Professor:
    first_name: str
    last_name: str
    department: str
    email: str

    def __init__(self,first_name: str,last_name: str,department: str,email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email