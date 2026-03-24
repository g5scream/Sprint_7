import pytest
from general_action import *
from urls import create_courier


@pytest.fixture
def created_courier():
    payload = generate_courier_data()
    response = create_courier(payload)

    return {
        'payload': payload,
        'response': response,
        'login': payload['login'],
        'password': payload['password'],
        'first_name': payload['first_name']
    }