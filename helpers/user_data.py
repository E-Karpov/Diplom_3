from faker import Faker
import allure


class Person:
    """Генерация тестовых данных пользователя"""

    @staticmethod
    @allure.step('Генерация email, password, name пользователя')
    def create_data_correct_user():
        """Генерирует корректные данные для регистрации пользователя"""
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data