import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1d11812210e97ca354a2aaeb0604e977'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '33824'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}) 
    assert response.json()["data"][0]["trainer_name"] == 'KillerTomatos'