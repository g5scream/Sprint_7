import allure
from data import ApiData
from urls import create_courier, login_courier
from general_action import generate_courier_data

@allure.suite('Тесты авторизации курьера')
class TestCourierLogin:
    @allure.title('Успешная авторизация курьера')
    def test_login_succ(self, created_courier):
        login = created_courier['login']
        password = created_courier['password']

        response = login_courier({'login' : login, 'password' : password})
        print(f"Статус-код: {response.status_code}")
        print(f"Тело ответа : {response.text}")
        assert response.status_code == ApiData.HTTP_STATUS_OK
        assert 'id' in response.json()      # понятно что тест должен быть с одним assert по предыдущим спринтам

    @allure.title('Ошибка при неверном/несуществующем пароле')
    def test_login_fail_pass(self):
        courier_data = generate_courier_data()
        create_courier(courier_data)

        response = login_courier({'login' : courier_data['login'], 'password' : 'qwerty'})
        print(f"Статус-код: {response.status_code}")
        print(f"Тело ответа : {response.text}")
        assert response.status_code == ApiData.HTTP_STATUS_NOT_FOUND
        assert ApiData.ERROR_ACCOUNT_NOT_FOUND in response.text

    @allure.title('Ошибка при отсутствии логина')
    def test_login_missing(self):
        response = login_courier({'password' : '999'})
        print(f"Статус-код: {response.status_code}")
        print(f"Тело ответа : {response.text}")
        assert response.status_code == ApiData.HTTP_STATUS_BAD_REQUEST
        assert ApiData.ERROR_MISSING_DATA in response.text

    @allure.title('Ошибка авторизации несуществующего пользователя')
    def test_login_not_exist(self):
        response = login_courier({'login' : 'qwerty', 'password' : '999999'})
        print(f"Статус-код: {response.status_code}")
        print(f"Тело ответа : {response.text}")
        #print(f"Заголовки ответа: {dict(response.headers)}")
        assert response.status_code == ApiData.HTTP_STATUS_NOT_FOUND
        assert ApiData.ERROR_ACCOUNT_NOT_FOUND in response.text