import allure
import pytest
from data import ApiData
from urls import create_courier
from general_action import *

@allure.suite('Тесты создания курьера')
class TestCourierCreation:
    @allure.title('создание курьера')    
    def test_create_courier_succ(self):
        payload = generate_courier_data()
        response = create_courier(payload)

        print(f"Статус-код: {response.status_code}")
        print(f"Тело ответа: {response.text}")

        assert response.status_code == ApiData.HTTP_STATUS_CREATED
        assert response.json() == ApiData.RESPONSE_OK   

    @allure.title('нельзя создать двух одинаковых курьеров')
    def test_create_courier_dubl_fail(self, created_courier):
        payload = created_courier['payload']
        response = create_courier(payload)
        
        print(f"Статус-код: {response.status_code}")
        print(f"Тело ответа : {response.text}")

        assert response.status_code == ApiData.HTTP_STATUS_CONFLICT
        assert ApiData.ERROR_LOGIN_ALREADY_USED in response.text

    @allure.title('нельзя создать курьера без логина или без пароля')
    @pytest.mark.parametrize('payload', ApiData.COURIER_CREATION_ERROR_CASES)
    def test_create_courier_incomplete_data(self, payload):

        response = create_courier(payload)

        assert response.status_code == ApiData.HTTP_STATUS_BAD_REQUEST
        assert ApiData.ERROR_INSUFFICIENT_DATA in response.text

        print(f"Статус-код: {response.status_code}")
        print(f"Тело ответа: {response.text}")