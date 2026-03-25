import pytest
import allure
from general_action import *
from api_client import *

@pytest.fixture
def created_courier():
    payload = generate_courier_data() 
    response = ApiClient.create_courier(payload)

    return   {
        'payload': payload,
        'response': response,
        'login': payload['login'],
        'password': payload['password'],
        'first_name': payload['first_name']
    }

def attach_response_to_allure(response):
    with allure.step("Ответ сервера"):
        allure.attach(
            body=response.text,
            name="Тело ответа",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            body=str(response.status_code),
            name="Статус-код",
            attachment_type=allure.attachment_type.TEXT
        )