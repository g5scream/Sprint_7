import pytest
import allure
from data import ApiData
from urls import create_order
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
        response = create_order(payload)
        
        print(f"Тело ответа : {response.text}")

        assert ApiData.RESPONSE_FIELD_TRACK in response.json()