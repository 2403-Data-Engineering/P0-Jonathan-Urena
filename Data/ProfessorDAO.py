from Data import db_connection_manager
from Models.Professor import Professor

def get_all_professors():
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT * FROM professors"

        cursor.execute(sql)

        for row in cursor:
            print(row)

def get_professor_by_id(id: int) -> str:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM professors WHERE id = %s", [id])
        return cursor.fetchone()
    #returns dict

def create_professor(professor:Professor) -> Professor:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO professors (first_name,last_name,email,dept) VALUES (%(first_name)s, %(last_name)s, %(email)s,%(department)s)",professor.__dict__)
        conn.commit()
    

def update_professor(professor: Professor) -> Professor:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """UPDATE professors 
               SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, major=%(major)s, year=%(year)s 
               WHERE id=%(id)s""",
            professor.__dict__
        )
        conn.commit()

def delete_professor(id: int) -> None:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM professors WHERE id=%(id)s", {"id": id})
        conn.commit()