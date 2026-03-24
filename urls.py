import requests

SERVICE_BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'


def create_courier(payload):
    return requests.post(f'{SERVICE_BASE_URL}/courier', data = payload)

def login_courier(payload):
    return requests.post(f'{SERVICE_BASE_URL}/courier/login', data = payload)

def create_order(payload):
    return requests.post(f'{SERVICE_BASE_URL}/orders', json = payload)

def get_orders():
    return requests.get(f'{SERVICE_BASE_URL}/orders')
