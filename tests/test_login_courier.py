import allure
from data import ApiData
from conftest import attach_response_to_allure
from api_client import *
from general_action import generate_courier_data

@allure.suite('Тесты авторизации курьера')
class TestCourierLogin:
    @allure.title('Успешная авторизация курьера')
    def test_login_succ(self, created_courier):
        login = created_courier['login']
        password = created_courier['password']

        response = ApiClient.login_courier({'login' : login, 'password' : password})
        
        response_json = response.json()

        attach_response_to_allure(response)
            
        assert response.status_code == ApiData.HTTP_STATUS_OK
        assert 'id' in str(response_json)      # понятно что тест должен быть с одним assert по предыдущим спринтам

    @allure.title('Ошибка при неверном/несуществующем пароле')
    def test_login_fail_pass(self, created_courier):
        response = ApiClient.login_courier({'login' : created_courier['login'], 'password' : 'qwerty'})
    
        attach_response_to_allure(response)

        response_json = response.json()

        assert response.status_code == ApiData.HTTP_STATUS_NOT_FOUND
        assert ApiData.ERROR_ACCOUNT_NOT_FOUND in str(response_json)

    @allure.title('Ошибка при отсутствии логина')
    def test_login_missing(self):
        response = ApiClient.login_courier({'password' : '999'})

        attach_response_to_allure(response)
        
        response_json = response.json()

        assert response.status_code == ApiData.HTTP_STATUS_BAD_REQUEST
        assert ApiData.ERROR_MISSING_DATA in str(response_json)

    @allure.title('Ошибка авторизации несуществующего пользователя')
    def test_login_not_exist(self):
        response = ApiClient.login_courier({'login' : 'qwerty', 'password' : '999999'})

        attach_response_to_allure(response)
        
        response_json = response.json()

        assert response.status_code == ApiData.HTTP_STATUS_NOT_FOUND
        assert ApiData.ERROR_ACCOUNT_NOT_FOUND in str(response_json)