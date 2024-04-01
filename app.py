import requests
from db import create_database,insert_data
     
def input_data():
    base_url = 'https://api.disneyapi.dev/character'
    next_page = base_url
    while next_page:
        res = requests.get(next_page)
        if res.status_code == 200:
            data = res.json()
            for character in data['data']:
                insert_data(character)
            next_page = data['info']['nextPage']
        else:
            print(f"Error Status Code: {res.status_code}")
            return None
        
if __name__ == "__main__":
    input_data()
    print('-------------------\n\nDATA INSERTED\n\n-------------------')
