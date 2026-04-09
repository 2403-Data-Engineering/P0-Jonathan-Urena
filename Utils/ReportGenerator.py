from mdutils.mdutils import MdUtils
from Service.StudentService import StudentService
student_service = StudentService()
class ReportGenerator:
    
    def generateStudentReport(self,id:int):
        
        classes_result = student_service.findAllClasses(id)
        student_result = student_service.getStudentById(id)
        # import os
        # print(os.getcwd())  # prints the directory mdutils will write to
        md = MdUtils(file_name='P0-Jonathan-Urena/Utils/student_report', title='Student Enrollment Report')
        md.new_header(level=1, title='Student Info')
        md.new_paragraph(f"Student ID:{student_result["id"]} + First Name: {student_result["first_name"]}")

        