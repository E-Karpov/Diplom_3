from data.ingredients import Ingredients
from data.urls import MainUrl, Endpoints
import requests
import allure


class Order:
    """Методы для работы с заказами через API"""

    @allure.step('Создание нового заказа пользователя через API')
    def create_order(self, create_new_user):
        """Создает новый заказ для пользователя"""
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        requests.post(
            MainUrl.MAIN_URL + Endpoints.CREATE_ORDER,
            headers=headers,
            data=Ingredients.CORRECT_INGREDIENTS_DATA
        )

    @allure.step('Получение заказов пользователя через API')
    def get_user_orders(self, create_new_user):
        """Получает список заказов пользователя"""
        token = create_new_user[1].json()["accessToken"]
        headers = {'Authorization': token}
        response = requests.get(MainUrl.MAIN_URL + Endpoints.GET_ORDERS, headers=headers)
        return response.json()["orders"][0]["number"]