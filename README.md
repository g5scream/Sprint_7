# Sprint_7

### Тестирование API сервиса [ЯндексСамокат](https://qa-scooter.praktikum-services.ru/) | [API ЯндексСамокат](https://qa-scooter.praktikum-services.ru/docs)

### Стек технологий
* **Язык:** Python 3.14
* **Фреймворк:** PyTest
* **Генерация тестовых данных:** Faker
* **HTTP‑клиент:** Requests 
* **Отчётность:** Allure
* **API‑тестирование:** Прямой вызов REST API

### Запуск тестов
* **Запуск тестов в один поток:** `pytest -v`
* **Allure отчеты, сохраняет результаты выполнения:** `pytest tests/ --alluredir=allure_results`
* **Сформировать интерактивный отчёт Allure:** `allure serve allure_results` 

### Структура проекта
    Sprint_6/
    ├── conftest.py
    ├── urls.py
    ├── general_action.py
    ├── data 
    ├── pytest.ini
    ├── README.md
    ├── requirements.txt                
    └── tests/
        ├── test_create_courier.py
        ├── test_login_courier.py
        ├── test_order_create.py     
        └── test_order_list.py

### Реализованны сценарии

* **Работа с курьерами**
    - Успешная регистрация курьера с обязательными полями.
    - Запрет дублирования курьеров (уникальный логин).
    - Обработка ошибок при отсутствии обязательных полей.
    - Авторизация существующего курьера с возвратом id.
    - Обработка неверных данных при входе.

* **Работа с заказами**
    - Создание заказа с разными комбинациями цветов: BLACK, GREY, оба или ни одного.
    - Успешный ответ содержит уникальный track.
    - Получение списка всех заказов.