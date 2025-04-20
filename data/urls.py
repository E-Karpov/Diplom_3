class MainUrl:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'


class URLS:
    """URLs сервиса"""
    URL_FEED = 'feed'  # Лента заказов
    URL_LOGIN = 'login'  # Авторизация
    URL_RECOVERY = 'forgot-password'  # Восстановление пароля
    URL_REGISTER = 'register'  # Регистрация пользователя
    URL_PROFILE_AREA = 'account/profile'  # Личный кабинет
    URL_HISTORY_ORDER = 'account/order-history'  # История заказов
    URL_RESET_PASSWORD = 'reset-password'  # Сброс пароля


class Endpoints:
    """Эндпоинты API"""

    CREATE_USER = 'api/auth/register'
    LOGIN = 'api/auth/login'
    DELETE_USER = 'api/auth/user'
    CREATE_ORDER = 'api/orders'
    GET_ORDERS = 'api/orders'
