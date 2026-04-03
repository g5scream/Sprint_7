import pytest
import allure
from data import ApiData
from conftest import attach_response_to_allure
from api_client import *
from general_action import generate_order_payload 

@allure.suite('Тесты создания заказов')
class TestOrderCreation:
    @allure.title('Создание заказа с разными цветами')
    @pytest.mark.parametrize('color', [
        ApiData.ORDER_COLORS_BLACK,
        ApiData.ORDER_COLORS_GREY,
        ApiData.ORDER_COLORS_MIXED,
        ApiData.ORDER_COLORS_EMPTY
    ])
    def test_create_order_with_color(self, color):
        payload = generate_order_payload(color=color)       
        response = ApiClient.create_order(payload)
        
        attach_response_to_allure(response)
        
        response_json = response.json()

        assert response.status_code == ApiData.HTTP_STATUS_CREATED
        assert ApiData.RESPONSE_FIELD_TRACK in str(response_json)