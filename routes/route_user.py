from urls import API_URL
import requests
import allure

class UserApi:

    @allure.step('Запрос. Тип Delete. /api/v1/courier/{id}. Удаление курьера.')
    def delete_user(self, id):
        response = requests.delete(f'{API_URL}/api/v1/courier/{id}', data={"id": f"{id}"})
        return response

    @allure.step('Запрос. Тип Post. /api/v1/courier/login Логин Курьера')
    def login_user(self, payload):
        response = requests.post(f'{API_URL}/api/v1/courier/login', data=payload)
        return response

    @allure.step('Запрос. Тип Post. /api/v1/courier Регистрация Курьера')
    def create_user(self, payload):
        response = requests.post(f'{API_URL}/api/v1/courier', data=payload)
        return response