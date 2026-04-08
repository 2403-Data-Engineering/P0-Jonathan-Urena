from Data import db_connection_manager
from Models.Classes import Classes

def get_all_classes():
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        sql = "SELECT * FROM classes"

        cursor.execute(sql)

        for row in cursor:
            print(row)

def get_classes_by_id(id: int) -> str:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM classes WHERE id = %s", [id])
        return cursor.fetchone()
    #returns dict

def create_classes(classes:Classes) -> Classes:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO classes (class_name,assigned_professor) VALUES (%(class_name)s, %(professor_id)s)",classes.__dict__)
        conn.commit()
    

def update_classes(classes: Classes) -> Classes:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """UPDATE classess 
               SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, major=%(major)s, year=%(year)s 
               WHERE id=%(id)s""",
            classes.__dict__
        )
        conn.commit()

def delete_classes(id: int) -> None:
    with db_connection_manager.get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM classess WHERE id=%(id)s", {"id": id})
        conn.commit()