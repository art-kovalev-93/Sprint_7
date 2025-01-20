from helpers import Helpers
from routes.route_user import UserApi
from data_for_test import StatusMessages
import pytest


class TestCourierRegistration:
    def test_create_courier_status_201(self):
        helper = Helpers()
        payload = helper.generate_data()
        user_api = UserApi()
        response = user_api.create_user(payload=payload)
        assert 201 == response.status_code

    def test_create_courier_body_is_right(self):
        helper = Helpers()
        message = StatusMessages()
        user_api = UserApi()
        payload = helper.generate_data()
        response = user_api.create_user(payload=payload)
        assert  response.json() == message.success_create_user

    def test_create_courier_with_similar_login_error_409(self):
        helper = Helpers()
        user_api = UserApi()
        payload = helper.generate_data()
        user_api.create_user(payload=payload)
        response = user_api.create_user(payload=payload)
        assert 409 == response.status_code

    def test_create_courier_with_similar_login_error_body(self):
        helper = Helpers()
        user_api = UserApi()
        message = StatusMessages()
        payload = helper.generate_data()
        user_api.create_user(payload=payload)
        response = user_api.create_user(payload=payload)
        assert message.similar_login_error == response.json()

    incomplete_body = [{"login": "login", "password": "password"},
                        {"login": "login", "firstName": "password"},
                        {"password": "password", "firstName": "firstName"}]

    @pytest.mark.parametrize("payload", incomplete_body)
    def test_create_with_incomplete_body_400(self, payload):
        user_api = UserApi()
        user_api.create_user(payload=payload)
        response = user_api.create_user(payload=payload)
        assert 400 == response.status_code

    @pytest.mark.parametrize("payload", incomplete_body)
    def test_create_with_incomplete_body_body(self, payload):
        helper = Helpers()
        user_api = UserApi()
        message = StatusMessages()
        user_api.create_user(payload=payload)
        response = user_api.create_user(payload=payload)
        assert message.incomplete_data_error == response.json()





