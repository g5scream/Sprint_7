import allure
import pytest
from conftest import attach_response_to_allure
from data import ApiData
from api_client import *
from general_action import *

@allure.suite('Тесты создания курьера')
class TestCourierCreation:
    @allure.title('создание курьера')    
    def test_create_courier_succ(self):
        payload = generate_courier_data()
        response = ApiClient.create_courier(payload)

        attach_response_to_allure(response)

        response_json = response.json()

        assert response.status_code == ApiData.HTTP_STATUS_CREATED
        assert response_json == ApiData.RESPONSE_OK   

    @allure.title('нельзя создать двух одинаковых курьеров')
    def test_create_courier_dubl_fail(self, created_courier):
        payload = created_courier['payload']
        response = ApiClient.create_courier(payload)

        attach_response_to_allure(response)

        response_json = response.json()

        assert response.status_code == ApiData.HTTP_STATUS_CONFLICT
        assert ApiData.ERROR_LOGIN_ALREADY_USED in str(response_json)

    @allure.title('нельзя создать курьера без логина или без пароля')
    @pytest.mark.parametrize('payload', ApiData.COURIER_CREATION_ERROR_CASES)
    def test_create_courier_incomplete_data(self, payload):
        response = ApiClient.create_courier(payload)

        attach_response_to_allure(response)

        response_json = response.json()

        assert response.status_code == ApiData.HTTP_STATUS_BAD_REQUEST
        assert ApiData.ERROR_INSUFFICIENT_DATA in str(response_json)
