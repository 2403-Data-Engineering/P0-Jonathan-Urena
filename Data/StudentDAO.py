from Data import db_connection_manager
from Models.Student import Student

def get_all_students():
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT * FROM students"

        cursor.execute(sql)

        for row in cursor:
            print(row)

def get_student_by_id(id: int) -> str:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id = %s", [id])
        return cursor.fetchone()
    #returns dict

def create_student(student:Student) -> Student:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO students (first_name,last_name,email,major,year) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(major)s, %(year)s)",student.__dict__)
        conn.commit()
    

