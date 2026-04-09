from Models.Student import Student
from Models.Professor import Professor
from Models.Classes import Classes
from Service.StudentService import StudentService
from Service.ProfessorService import ProfessorService
from Service.ClassesService import ClassesService
from Utils.ReportGenerator import ReportGenerator

professor_service = ProfessorService()
student_service = StudentService()
classes_service = ClassesService()
utils = ReportGenerator()

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
   
    if student_service.findById(student_id) == None:
        print("Error: Id does not exist in database")
        return deleteStudent()
    if student_service.findEnrollment(student_id) == True:
        print("Student is currently in classes thus cannot be deleted")
        return deleteStudent()
    student_service.deleteById(student_id)

def viewClassesStudentEnrolled():
    try:
        print("Enter the student's id to view all classes enrolled in")
        raw = input().strip()
        student_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return viewClassesStudentEnrolled()
    if student_service.findById(student_id) == None:
        print("Error: Id does not exist in database")
        return viewClassesStudentEnrolled()
    print(student_service.findAllClasses(student_id))

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
    if student_service.findById(student_id) == None or classes_service.findById(class_id) == None:
        print("Error: Id does not exist in database")
        return enrollStudentInClass()
    student_service.enroll(student_id,class_id)

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
        return dropStudentInClass()
    if student_service.findById(student_id) == None or classes_service.findById(class_id) == None:
        print("Error: Id does not exist in database")
        return dropStudentInClass()
    student_service.drop(student_id,class_id)

def generateStudentEnrollmentReport():
    try:
        print("Enter the student's id to generate a report of all classes enrolled in")
        raw = input().strip()
        student_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return generateStudentEnrollmentReport()
    if student_service.findById(student_id) == None:
        print("Error: Id does not exist in database")
        return generateStudentEnrollmentReport()
    utils.generateStudentReport(student_id)

# ── Professor methods────────────────────────────────────────────────────────────
def viewAllProfessors():
    professor_service.findAll()

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
    professor_service.save(new_professor)
    

def updateProfessor():
    try:
        print("Enter the professor's id to update")
        raw = input().strip()
        professor_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return updateProfessor()
   
    if professor_service.findById(professor_id) == None:
        print("Error: Id does not exist in database")
        return updateProfessor()
    else:
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
            return updateProfessor()
        new_professor = Professor(first_name,last_name,department,email)
        professor_service.updateById(professor_id,new_professor)

def deleteProfessor():
    try:
        print("Enter the professor's id to delete")
        raw = input().strip()
        professor_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return deleteProfessor()
    if professor_service.findTeaching(professor_id) == True:
        print("Professor is still teaching thus cannot be deleted")
        return deleteProfessor()
    professor_service.deleteById(professor_id)
    
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
    classes_service.findAll()

def viewAllStudentsEnrolled():
    try:
        print("Id of class to view students: ")
        raw = input().strip()
        class_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return viewAllStudentsEnrolled()
    if classes_service.findById(class_id) == None:
        print("Error: Class id does not exist in database")
        return viewAllStudentsEnrolled()
    classes_service.findAllEnrolled(class_id)

def addClass():
    print("Class name: ")
    class_name: str = input().strip()
    if len(class_name)==0:
        print("Error: Class name can not be left blank")
        return addClass()
    try:
        print("Id of professor to assign class: ")
        raw = input().strip()
        professor_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return addClass()
    if professor_service.findById(professor_id) == None:
        print("Error: Id does not exist in database")
        return addClass()
    
    new_class = Classes(class_name,professor_id)
    classes_service.save(new_class)
    
def updateClass():
    try:
        print("Enter the id of the class to update: ")
        raw = input().strip()
        class_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return updateClass()
    print("Class name: ")
    class_name: str = input().strip()
    if len(class_name)==0:
        print("Error: Class name can not be left blank")
        return updateClass()
    try:
        print("Id of professor to assign class: ")
        raw = input().strip()
        professor_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return updateClass()
    if classes_service.findById(class_id)== None or professor_service.findById(professor_id) == None:
        print("Error: Id does not exist in database")
        return updateClass()
    new_class = Classes(class_name,professor_id)
    classes_service.updateById(class_id,new_class)
    
def deleteClass():
    try:
        print("Enter the id of the class to delete: ")
        raw = input().strip()
        class_id = int(raw)
    except ValueError:
        print("  ⚠  Invalid input — enter a number.")
        return deleteClass()
    if classes_service.findById(class_id)== None:
        print("Error that class id is registered")
        return deleteClass
    classes_service.deleteById(class_id)