from data_for_test import StatusMessages, login_data, wrong_login_data, non_existent_profile
import pytest
from routes.route_user import UserApi
import allure


class TestLogin:
    @allure.title('Проверка успешного логина, код ответа 200.')
    def test_login_success_200(self):
        api = UserApi()
        response = api.login_user(payload=login_data)
        assert 200 == response.status_code

    @allure.title('Проверка успешного логина, Тело ответа содержит id.')
    def test_login_success_body(self):
        api = UserApi()
        message = StatusMessages()
        response = api.login_user(payload=login_data)
        assert  response.json() == message.success_login_user

    @allure.title('Проверка логина c неверными данными, код ответа 400')
    @pytest.mark.parametrize("payload", wrong_login_data)
    def test_login_without_one_parametre_400(self, payload):
        api = UserApi()
        response = api.login_user(payload=payload)
        assert 400 == response.status_code

    @allure.title('Проверка логина c неверными данными, bad_request_err')
    @pytest.mark.parametrize("payload", wrong_login_data)
    def test_login_without_one_parametre_body(self, payload):
        api = UserApi()
        message = StatusMessages()
        response = api.login_user(payload=payload)
        assert response.json() == message.bad_request_error

    @allure.title('Проверка логина c не созданным пользователем, 404')
    def test_login_profile_not_found_404(self):
        api = UserApi()
        response = api.login_user(payload=non_existent_profile)
        assert 404 == response.status_code

    @allure.title('Проверка логина c не созданным пользователем, Not found')
    def test_login_profile_not_found_body(self):
        api = UserApi()
        message = StatusMessages()
        response = api.login_user(payload=non_existent_profile)
        assert response.json() == message.not_found_error