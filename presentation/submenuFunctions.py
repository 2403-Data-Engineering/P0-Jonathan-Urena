from Models.Student import Student
from Models.Professor import Professor
from Models.Class import Class
from Service.StudentService import StudentService
student_service = StudentService()

# ── Student methods────────────────────────────────────────────────────────────
def viewAllStudents():
    student_service.findAll()

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

def updateStudent():
    try:
        print("Enter the student's id to update")
        raw = input().strip()
        student_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return updateStudent()
   
    if student_service.findById(student_id) == None:
        print("Error: Id does not exist in database")
        return updateStudent()
    else:
        print("Enter Updated Information")
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
        updated_student = Student(first_name,last_name,major,email,year)
        student_service.updateById(student_id,updated_student)
    
def deleteStudent():
    try:
        print("Enter the student's id to delete")
        raw = input().strip()
        student_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return deleteStudent()
    #call service

def viewClassesStudentEnrolled():
    try:
        print("Enter the student's id to view all classes enrolled in")
        raw = input().strip()
        student_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return viewClassesStudentEnrolled()
    #call service

def enrollStudentInClass():
    try:
        print("Enter the student's id to enroll")
        raw = input().strip()
        student_id = int(raw)
        print("Enter the id of the class to enroll: ")
        raw = input().strip()
        class_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return enrollStudentInClass()
    print("Success")

def dropStudentInClass():
    try:
        print("Enter the student's id to drop")
        raw = input().strip()
        student_id = int(raw)
        print("Enter the id of the class to drop: ")
        raw = input().strip()
        class_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return enrollStudentInClass()
    print("Success")

def generateStudentEnrollmentReport():
    try:
        print("Enter the student's id to generate a report of all classes enrolled in")
        raw = input().strip()
        student_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return generateStudentEnrollmentReport()
    #call service

# ── Professor methods────────────────────────────────────────────────────────────
def viewAllProfessors():
    professorsList = []
    print("All Professors List")

    #student_service.findAll()

def addProfessor():
    print("First name: ")
    first_name: str = input().strip()
    print("Last name: ")
    last_name: str = input().strip()
    print("Department: ")
    department: str = input().strip()
    print("Email: ")
    email: str = input().strip()
    if len(first_name)==0 or len(last_name)==0 or len(department)==0 or len(email)==0:
        print("Error: No field can be left blank")
        return addProfessor()
    new_professor = Professor(first_name,last_name,department,email)

    print(new_professor)
    # Implement validation steps between prompts?
    # new_student: Student = Student(first_name, last_name, major, email, year)
    # self.terminal.student_service.save(new_student)

def updateProfessor():
    try:
        print("Enter the professor's id to update")
        raw = input().strip()
        professor_id = int(raw)
        print(professor_id)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return updateProfessor()

def deleteProfessor():
    try:
        print("Enter the professor's id to delete")
        raw = input().strip()
        professor_id = int(raw)
        print(professor_id)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return deleteProfessor()
    
def generateProfessorReport():
    try:
        print("Enter the professor's id to generate a report of all classes teaching and students enrolled")
        raw = input().strip()
        professor_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return generateProfessorReport()
    #call service
# ── Class methods────────────────────────────────────────────────────────────
def viewAllClasses():
    classList = []
    print("All Class List")

    #class_service.findAll()

def addClass():
    print("Class name: ")
    class_name: str = input().strip()
    try:
        print("Id of professor to assign class: ")
        raw = input().strip()
        professor_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return addClass()
    if len(class_name)==0:
        print("Error: Class name can not be left blank")
        return addClass()
    new_class = Class(class_name)
    print(new_class)
    
def updateClass():
    try:
        print("Enter the id of the class to update: ")
        raw = input().strip()
        class_id = int(raw)
        print("Id of professor to assign to class: ")
        raw = input().strip()
        professor_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return updateClass()
    
def deleteClass():
    try:
        print("Enter the id of the class to delete: ")
        raw = input().strip()
        class_id = int(raw)
        
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return deleteClass()