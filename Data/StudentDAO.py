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

def get_enrollment(student_id:int):
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student_courses WHERE student_id=%s",[student_id])
        return cursor.fetchone()

def create_student(student:Student) -> Student:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO students (first_name,last_name,email,major,year) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(major)s, %(year)s)",student.__dict__)
        conn.commit()
    

def update_student(student: Student) -> Student:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """UPDATE students 
               SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, major=%(major)s, year=%(year)s 
               WHERE id=%(id)s""",
            student.__dict__
        )
        conn.commit()

def delete_student(id: int) -> None:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM students WHERE id=%(id)s", {"id": id})
        conn.commit()

def enroll_in_class(student_id:int,class_id:int):
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO student_courses (student_id,class_id) VALUES (%(student_id)s, %(class_id)s)",{
            "student_id": student_id,
            "class_id": class_id
        })
        conn.commit()

def drop_in_class(student_id:int,class_id:int):
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM student_courses WHERE student_id=%(student_id)s AND class_id=%(class_id)s",{
            "student_id": student_id,
            "class_id": class_id
        })
        conn.commit()

def get_student_classes(student_id: int):
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT classes.class_name
            FROM classes
            JOIN student_courses ON classes.id = student_courses.class_id
            WHERE student_courses.student_id = %(student_id)s
            """,
            {"student_id":student_id}
        )
        return cursor.fetchall()