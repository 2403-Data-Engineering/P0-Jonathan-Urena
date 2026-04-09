from mdutils.mdutils import MdUtils
from Service.StudentService import StudentService
student_service = StudentService()
class ReportGenerator:
    
    def generateStudentReport(self,id:int):
        
        classes_result = student_service.findAllClasses(id)
        student_result = student_service.getStudentById(id)
        
        
        md = MdUtils(file_name='P0-Jonathan-Urena/Utils/student_report', title='Student Enrollment Report')
        md.new_header(level=1, title='Student Info')
        md.new_paragraph(f"Student ID:{student_result["id"]} | First Name: {student_result["first_name"]} | Last Name: {student_result["last_name"]} | Major: {student_result["major"]} | Year: {student_result["year"]}\nEmail: {student_result["email"]}")
        md.new_header(level=1, title='Course Info')
        table = ["Class ID","Class Name"]
        class_rows = len(classes_result)
        
        for i in range(0,len(classes_result)):
            table.append(classes_result[i]["id"])
            table.append(classes_result[i]["class_name"])


       
        
        md.new_table(columns=2, rows=class_rows+1, text=table, text_align='center')
        
        md.create_md_file()
        
   