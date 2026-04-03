import allure
from api_client import *
from data import ApiData
from conftest import attach_response_to_allure

@allure.suite('Тесты работы со списком заказов')
class TestOrdersList:
    @allure.title('Возвращение списка заказов')
    def test_get_orders_list(self):
        response = ApiClient.get_orders()
        data = response.json()

        attach_response_to_allure(response)
        
        response_json = response.json()

        assert response.status_code == ApiData.HTTP_STATUS_OK
        assert isinstance(response_json['orders'], list)