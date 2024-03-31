import requests

def get_info():
    base_url = 'https://api.disneyapi.dev/character'
    next_page = base_url
    while next_page:
        res = requests.get(next_page)
        if res.status_code == 200:
            data = res.json()
            for character in data['data']:
                char_id = character['_id']
                print("Character ID:", char_id)
            next_page = data['info']['nextPage']
        else:
            print(f"Error Status Code: {res.status_code}")
            return None

get_info()
