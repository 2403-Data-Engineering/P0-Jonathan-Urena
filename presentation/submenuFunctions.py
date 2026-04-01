from Models.Student import Student

def addStudent():
        print("First name: ")
        first_name: str = input()
        print("Last name: ")
        last_name: str = input()
        print("Major: ")
        major: str = input()
        print("Email: ")
        email: str = input()
        print("Year: ")
        year: str = input()
        new_student = Student(first_name,last_name,major,email,year)
        
        return 
        # Implement validation steps between prompts?
        # new_student: Student = Student(first_name, last_name, major, email, year)
        # self.terminal.student_service.save(new_student)