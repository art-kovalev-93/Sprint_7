from urls import API_URL
import requests
import allure

class OrderApi:
    @allure.step('Запрос. Тип Post. /api/v1/orders. Создание заказа.')
    def create_order(self, payload):
        response = requests.post(f'{API_URL}/api/v1/orders', data=payload)
        return response

    @allure.step('Запрос. Тип get. /api/v1/orders. Получение списка заказов.')
    def get_orders(self, params):
        response = requests.get(f'{API_URL}/api/v1/orders', params=params)
        return response