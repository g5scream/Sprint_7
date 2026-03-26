import allure
import pytest
from conftest import attach_response_to_allure
from data import ApiData
from api_client import ApiClient

@allure.suite('Тесты удаления курьера')
class TestCourierDeletion:

    @allure.title('Успешное удаление курьера')
    def test_delete_courier_success(self, created_courier):
        courier_id = created_courier['id']

#        assert courier_id is not None, "Не удалось получить ID кура"

        response = ApiClient.delete_courier(courier_id)
        attach_response_to_allure(response)

        response_json = response.json()

        assert response.status_code == ApiData.HTTP_STATUS_OK
        assert response_json == ApiData.RESPONSE_OK
        