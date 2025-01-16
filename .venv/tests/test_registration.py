import random
import string
from venv import create
import requests
from helpers import Helpers
from data_for_test import StatusMessages
import pytest


class TestCourierLogin:
    def test_create_courier_status_201(self):
        helper = Helpers()
        payload = helper.generate_data()
        response = helper.create_user(payload=payload)
        assert 201 == response.status_code

    def test_create_courier_body_is_right(self):
        helper = Helpers()
        message = StatusMessages()
        payload = helper.generate_data()
        response = helper.create_user(payload=payload)
        assert  response.json() == message.success_create_user

    def test_create_courier_with_simmilar_login_error_409(self):
        helper = Helpers()
        payload = helper.generate_data()
        helper.create_user(payload=payload)
        response = helper.create_user(payload=payload)
        assert 409 == response.status_code

    def test_create_courier_with_simmilar_login_error_body(self):
        helper = Helpers()
        message = StatusMessages()
        payload = helper.generate_data()
        helper.create_user(payload=payload)
        response = helper.create_user(payload=payload)
        assert message.simmilar_login_error == response.json()

    wrong_registration_data = [{"login": "megauser", "password": "password"},
                        {"login": "login", "firstName": "password"},
                        {"password": "password", "firstName": "firstName"}]

    @pytest.mark.parametrize("payload", wrong_registration_data)
    def test_create_with_incomplete_body_400(self, payload):
        helper = Helpers()
        helper.create_user(payload=payload)
        response = helper.create_user(payload=payload)
        assert 400 == response.status_code

    @pytest.mark.parametrize("payload", wrong_registration_data)
    def test_create_with_incomplete_body_body(self, payload):
        helper = Helpers()
        message = StatusMessages()
        helper.create_user(payload=payload)
        response = helper.create_user(payload=payload)
        assert message.incomplete_data_error == response.json()





