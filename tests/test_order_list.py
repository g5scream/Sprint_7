import allure
from urls import get_orders

@allure.suite('Тесты работы со списком заказов')
class TestOrdersList:
    @allure.title('Возвращение списка заказов')
    def test_get_orders_list(self):
        response = get_orders()
        data = response.json()

        print(f"Список заказов: {data['orders']}")
        
        assert isinstance(data['orders'], list)