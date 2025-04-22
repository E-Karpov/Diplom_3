import allure
from locators.locators import PersonalAreaLocators
from pages.base_page import BasePage


class ProfileAreaPage(BasePage):
    """Класс для работы со страницей личного кабинета"""

    @allure.step('Проверка отображения формы "Личного кабинета"')
    def check_profile_area_form(self):
        """Проверяет видимость формы личного кабинета"""
        return self.check_element(PersonalAreaLocators.PROFILE_FORM)

    @allure.step('Клик по кнопке "Профиль"')
    def click_profile_btn(self):
        """Кликает по кнопке профиля"""
        self.click_button(PersonalAreaLocators.PROFILE_BTN)

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_orders_btn(self):
        """Кликает по кнопке истории заказов"""
        self.click_button(PersonalAreaLocators.ORDER_HISTORY_BTN)

    @allure.step('Проверка отображения формы "История заказов"')
    def check_history_form(self):
        """Проверяет видимость формы истории заказов"""
        return self.check_element(PersonalAreaLocators.HISTORY_ORDER_FORM)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_btn(self):
        """Кликает по кнопке выхода"""
        self.click_button(PersonalAreaLocators.EXIT_BTN)

    @allure.step('Клик по кнопке "Отмена"')
    def click_cancel_btn(self):
        """Кликает по кнопке отмены"""
        self.click_button(PersonalAreaLocators.CANCEL_BTN)

    @allure.step('Клик по кнопке "Сохранить"')
    def click_save_btn(self):
        """Кликает по кнопке сохранения"""
        self.click_button(PersonalAreaLocators.SAVE_BTN)

    @allure.step('Получение номера заказа в истории')
    def get_orders_number(self):
        """Получает номер заказа из истории"""
        return self.get_text_locator(PersonalAreaLocators.NUMBER_ORDER)