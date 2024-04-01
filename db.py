import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('disney_characters.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Characters(
                       id INTEGER PRIMARY KEY,
                       user TEXT NOT NULL
            )
        ''')

        conn.commit()
        conn.close()
        print("Database Initiated Successfully")

    except Exception as e:
        print("Error Occurred: ", e)
