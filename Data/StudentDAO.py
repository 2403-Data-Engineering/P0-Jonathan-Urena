from db_connection_manager import get_connection
# from Models.Student import Student

def get_all_students():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT * FROM students"

        cursor.execute(sql)

        for row in cursor:
            print(row)

def get_student_by_id(id: int) -> str:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id = %s", [id])
        return cursor.fetchone()
    #returns dict

def create_student() -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO students (first_name,last_name,email,major,year) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(major)s, %(year)s)",
        {
        "first_name": "John",
        "last_name":  "Smith",
        "email":      "johns@gmail.com",
        "major":       "Business",
        "year":       "Sophmore",
        })
        conn.commit()

#new_student = Student("John","Smith","Business","johns@gmail.com","Sophmore")
create_student()