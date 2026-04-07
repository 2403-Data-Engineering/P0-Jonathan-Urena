from dataclasses import dataclass
@dataclass
class Student:
    id:str
    first_name: str
    last_name: str
    major: str
    email: str
    year: str
    #Need to get id from database
    def __init__(self,first_name: str,last_name: str,major: str,email: str,year: str,id=None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.email = email
        self.year = year
        self.id = id
    
    def getFirstName(self):
        return self.first_name
    
    def getLastName(self):
        return self.last_name
    
    def getMajor(self):
        return self.major
    
    def getEmail(self):
        return self.email
    
    def getYear(self):
        return self.year
    
    def setFirstName(self,first_name):
        self.first_name = first_name
    
    def setLastName(self):
        return self.last_name
    
    def getMajor(self):
        return self.major
    
    def getEmail(self):
        return self.email
    
    def getYear(self):
        return self.year
    
    def setId(self,id):
        self.id = id
    