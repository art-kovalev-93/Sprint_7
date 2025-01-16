import random
import string
from urls import API_URL
import requests
import urls


class Helpers:

    def generate_data(self):

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def delete_user(self, id):
        response = requests.delete(f'{urls.API_URL}/api/v1/courier/{id}', data={"id": f"{id}"})
        return  response

    def login_user(self, login, password):
        payload = {
            "login": login,
            "password": password,
        }
        response = requests.post(f'{urls.API_URL}/api/v1/courier/login', data=payload)
        return  response

    def create_user(self, payload):
        response = requests.post(f'{API_URL}/api/v1/courier', data=payload)
        return response