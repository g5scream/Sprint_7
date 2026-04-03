import allure
import requests
from urls import *

class ApiClient:
    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(payload):
        return requests.post(COURIER_ENDPOINT, data=payload)

    @staticmethod
    @allure.step("Авторизация курьера")
    def login_courier(payload):
        return requests.post(LOGIN_ENDPOINT, data=payload)

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        return requests.post(ORDERS_ENDPOINT, json=payload)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders():
        return requests.get(ORDERS_ENDPOINT)
    
    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(f"{COURIER_ENDPOINT}/{courier_id}")