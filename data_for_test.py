class StatusMessages:
    similar_login_error={'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    success_create_user={'ok': True}
    incomplete_data_error={"code": 400,"message": "Недостаточно данных для создания учетной записи"}
    success_login_user = {"id": 449683}
    bad_request_error = {"code": 400, "message": "Недостаточно данных для входа"}
    not_found_error = {"code": 404, "message": "Учетная запись не найдена"}
    empty_order_list = {
    "orders": [],
    "pageInfo": {
        "page": 0,
        "total": 0,
        "limit": 30
    },
    "availableStations": []
}

login_data={"login": "test_user_007", "password": "password"}
non_existent_profile = {"login": "non_existent_profile", "password": "password"}
wrong_login_data = [{"login": "test_user_009", "password": ""}, {"login": "", "password": "password"}]
colour_for_test = [["BLACK", "GREY"], [], ["BLACK"], ["GREY"]]

class Bodies:
    def order_body(self,colour):
        order_body = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colour
        }
        return order_body

