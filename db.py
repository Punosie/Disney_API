import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('disney_characters.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Characters(
                id INTEGER PRIMARY KEY,
                name TEXT,
                films TEXT,
                shortFilms TEXT,
                tvShows TEXT,
                videoGames TEXT,
                parkAttractions TEXT,
                allies TEXT,
                enemies TEXT,
                sourceUrl TEXT,
                imageUrl TEXT,
                createdAt TEXT,
                updatedAt TEXT,
                url TEXT
            )
        ''')

        conn.commit()
        conn.close()
        print("Database Initiated Successfully")

    except Exception as e:
        print("Error Occurred: ", e)


def insert_data(character):
    try:
        conn = sqlite3.connect('disney_characters.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Characters (id, name, films, shortFilms, tvShows, videoGames, parkAttractions, allies, enemies, sourceUrl, imageUrl, createdAt, updatedAt, url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            character['_id'],
            character['name'] if 'name' in character else None,
            ','.join(character['films']) if 'films' in character else None,
            ','.join(character['shortFilms']) if 'shortFilms' in character else None,
            ','.join(character['tvShows']) if 'tvShows' in character else None,
            ','.join(character['videoGames']) if 'videoGames' in character else None,
            ','.join(character['parkAttractions']) if 'parkAttractions' in character else None,
            ','.join(character['allies']) if 'allies' in character else None,
            ','.join(character['enemies']) if 'enemies' in character else None,
            character['sourceUrl'] if 'sourceUrl' in character else None,
            character['imageUrl'] if 'imageUrl' in character else None,
            character['createdAt'] if 'createdAt' in character else None,
            character['updatedAt'] if 'updatedAt' in character else None,
            character['url'] if 'url' in character else None
        ))

        conn.commit()
        conn.close()
        print(f"--->\tInserted:\t{character['name']}")

    except Exception as e:
        print("Error occurred while inserting data: ", e)


def get_char(char_name):
    try:
        conn = sqlite3.connect('disney_characters.db')
        cursor = conn.cursor()

        cursor.execute('''
                        SELECT * FROM Characters WHERE name = ?
                    ''', (char_name,))
        
        character_data = cursor.fetchone()

        conn.close()

        return character_data

    except Exception as e:
        print("Error occurred while fetching character data: ", e)