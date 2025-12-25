from routes.route_order import OrderApi
from data_for_test import colour_for_test, Bodies
import pytest
import allure

class TestCreateOrder:
    @pytest.mark.parametrize("colour", colour_for_test)
    @allure.title('Проверка создания ордера с разными цветами на ответ 201')
    def test_create_order_with_different_colours_201(self, colour):
        order_api = OrderApi()
        body = Bodies()
        order_body = body.order_body(colour)
        response = order_api.create_order(payload=order_body)
        assert 201 == response.status_code

    @pytest.mark.parametrize("colour", colour_for_test)
    @allure.title('Проверка что при создании ордера с разными цветами в ответе приходит Track')
    def test_create_order_with_different_colours_body(self, colour):
        order_api = OrderApi()
        body = Bodies()
        order_body = body.order_body(colour)
        response = order_api.create_order(payload=order_body)
        assert "track" in response.json()
