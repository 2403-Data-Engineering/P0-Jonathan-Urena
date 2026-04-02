from Models.Student import Student
from Models.Professor import Professor
from Service.StudentService import StudentService
student_service = StudentService()

def addStudent():
    print("First name: ")
    first_name: str = input().strip()
    print("Last name: ")
    last_name: str = input().strip()
    print("Major: ")
    major: str = input().strip()
    print("Email: ")
    email: str = input().strip()
    print("Year: ")
    year: str = input().strip()
    if len(first_name)==0 or len(last_name)==0 or len(major)==0 or len(email)==0 or len(year)==0:
        print("Error: No field can be left blank")
        return addStudent()
    
    new_student = Student(first_name,last_name,major,email,year)
    student_service.save(new_student)

    return 

def addProfessor():
    print("First name: ")
    first_name: str = input()
    print("Last name: ")
    last_name: str = input()
    print("Department: ")
    department: str = input()
    print("Email: ")
    email: str = input()
    new_professor = Professor(first_name,last_name,department,email)
    print(new_professor)
    return 
    # Implement validation steps between prompts?
    # new_student: Student = Student(first_name, last_name, major, email, year)
    # self.terminal.student_service.save(new_student)
def addClass():
    print("First name: ")
    first_name: str = input()
    print("Last name: ")
    last_name: str = input()
    print("Department: ")
    department: str = input()
    print("Email: ")
    email: str = input()
    new_professor = Professor(first_name,last_name,department,email)
    print(new_professor)
    return 