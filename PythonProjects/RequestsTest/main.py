import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1d11812210e97ca354a2aaeb0604e977'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

body_put = {
    "pokemon_id": "329680",
    "name": "Бульба",
    "photo_id": 12
}

body_add = {
    "pokemon_id": "329680"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message'] 
print(message)

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put)

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add)