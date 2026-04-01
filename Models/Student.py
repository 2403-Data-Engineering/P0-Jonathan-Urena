from dataclasses import dataclass

@dataclass
class Student:
    first_name: str
    last_name: str
    major: str
    email: str
    year: str

    def __init__(self,first_name: str,last_name: str,major: str,email: str,year: str):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.email = email
        self.year = year
    
    
    