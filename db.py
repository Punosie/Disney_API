import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('disney_characters.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Characters(
                id INTEGER PRIMARY KEY,
                films TEXT,
                shortFilms TEXT,
                tvShows TEXT,
                videoGames TEXT,
                parkAttractions TEXT,
                allies TEXT,
                enemies TEXT,
                sourceUrl TEXT,
                name TEXT,
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
            INSERT INTO Characters (id, films, shortFilms, tvShows, videoGames, parkAttractions, allies, enemies, sourceUrl, name, imageUrl, createdAt, updatedAt, url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            character['_id'],
            ','.join(character['films']) if 'films' in character else None,
            ','.join(character['shortFilms']) if 'shortFilms' in character else None,
            ','.join(character['tvShows']) if 'tvShows' in character else None,
            ','.join(character['videoGames']) if 'videoGames' in character else None,
            ','.join(character['parkAttractions']) if 'parkAttractions' in character else None,
            ','.join(character['allies']) if 'allies' in character else None,
            ','.join(character['enemies']) if 'enemies' in character else None,
            character['sourceUrl'] if 'sourceUrl' in character else None,
            character['name'] if 'name' in character else None,
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