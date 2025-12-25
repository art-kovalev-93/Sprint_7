from data_for_test import StatusMessages
import allure
from routes.route_order import OrderApi

class TestOrderList:
    @allure.title('Проверка получения списка заказов, 200')
    def test_get_order_list_200(self):
        params={"courierId": "449683"}
        order_api = OrderApi()
        response = order_api.get_orders(params)
        assert 200 == response.status_code

    @allure.title('Проверка получения списка заказов, Тело ответа содержит id.')
    def test_get_order_list_check_orders(self):
        params={"courierId": "449683"}
        order_api = OrderApi()
        answer = StatusMessages()
        response = order_api.get_orders(params)
        assert response.json() == answer.empty_order_list

