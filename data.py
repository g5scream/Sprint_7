from general_action import*

class ApiData:

    # HTTP-статусы
    HTTP_STATUS_CREATED = 201
    HTTP_STATUS_CONFLICT = 409
    HTTP_STATUS_OK = 200
    HTTP_STATUS_NOT_FOUND = 404
    HTTP_STATUS_BAD_REQUEST = 400

    # Ожидаемые тела ответов
    RESPONSE_OK = {'ok': True}
    RESPONSE_FIELD_TRACK = 'track'

    # Сообщения об ошибках
    ERROR_LOGIN_ALREADY_USED = 'Этот логин уже используется'
    ERROR_ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
    ERROR_MISSING_DATA = 'Недостаточно данных для входа'
    ERROR_INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"
    
    # Цвета для заказов
    ORDER_COLORS_BLACK = ['BLACK']
    ORDER_COLORS_GREY = ['GREY']
    ORDER_COLORS_MIXED = ['BLACK', 'GREY']
    ORDER_COLORS_EMPTY = []

    # Наборы тестовых данных для ошибок создания курьера
    COURIER_CREATION_ERROR_CASES = [
        # Случай 1: отсутствует логин
        (
            {'password': generate_password(), 'first_name': generate_first_name()}
        ),
        # Случай 2: отсутствует пароль
        (
            {'login': generate_login(), 'first_name': generate_first_name()}
        )
    ]