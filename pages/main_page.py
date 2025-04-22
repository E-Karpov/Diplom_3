import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators
from locators.locators import HeaderPageLocators


class HeaderPage(BasePage):
    """Класс для работы с хедером сайта"""

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_btn(self):
        """Кликает по кнопке конструктора"""
        self.move_to_element_and_click(HeaderPageLocators.CONSTRUCTOR_BTN)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_feed_btn(self):
        """Кликает по кнопке ленты заказов"""
        self.move_to_element_and_click(HeaderPageLocators.ORDER_FEED_BTN)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_profile_area_btn(self):
        """Кликает по кнопке личного кабинета"""
        self.move_to_element_and_click(HeaderPageLocators.PERSONAL_ACCOUNT_BTN)


class MainPage(BasePage):
    """Класс для работы с главной страницей"""

    @allure.step('Переход к кнопке "Личный Кабинет" и клик на нее')
    def move_to_personal_account_btn_and_click(self):
        """Переходит к кнопке личного кабинета и кликает по ней"""
        self.move_to_element_and_click(MainPageLocators.PERSONAL_ACCOUNT_BTN)

    @allure.step('Проверка отображения формы конструктора')
    def check_constructor_form(self):
        """Проверяет видимость формы конструктора"""
        return self.check_element(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Проверка отображения формы ленты заказов')
    def check_orders_feed_form(self):
        """Проверяет видимость формы ленты заказов"""
        return self.check_element(MainPageLocators.ORDER_FEED_FORM)

    @allure.step('Клик по Флюоресцентной булке R2-D3')
    def click_fluorescent_bun_btn(self):
        """Кликает по элементу флюоресцентной булки"""
        self.click_button(MainPageLocators.FLUORESCENT_BUN_BTN)

    @allure.step('Проверка отображения формы "Информации о булке"')
    def check_fluorescent_bun_form(self):
        """Проверяет видимость формы с деталями ингредиента"""
        return self.check_element(MainPageLocators.POPUP_FORM_INGREDIENTS)

    @allure.step('Проверка закрытия формы "Информация о булке"')
    def check_close_fluorescent_bun_form(self):
        """Проверяет закрытие формы с деталями ингредиента"""
        return self.check_element_is_not_visible(MainPageLocators.POPUP_FORM_INGREDIENTS)

    @allure.step('Закрытие формы информации об ингредиенте')
    def close_popup_form(self):
        """Закрывает модальное окно"""
        self.move_to_element_and_click(MainPageLocators.CLOSE_POPUP_FORM)

    @allure.step('Добавить булку в корзину')
    def add_bun(self):
        """Добавляет булку в корзину"""
        self.drag_and_drop(MainPageLocators.FLUORESCENT_BUN_BTN, MainPageLocators.ORDER_BASKET)
        self.wait_for_load_element(MainPageLocators.COUNTER_INGREDIENT)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_place_order_button(self):
        """Кликает по кнопке оформления заказа"""
        self.click_button(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Создание заказа')
    def create_order(self):
        """Создает новый заказ"""
        self.add_bun()
        self.click_place_order_button()

    @allure.step('Получение значения счетчика ингредиента')
    def check_counter_ingredient(self):
        """Проверяет значение счетчика ингредиента"""
        return self.get_text_locator(MainPageLocators.COUNTER_INGREDIENT)

    @allure.step('Проверка отображения формы оформления заказа')
    def check_order_form(self):
        """Проверяет видимость формы заказа"""
        return self.check_element(MainPageLocators.ORDER_FORM)

    @allure.step('Получение номера оформленного заказа')
    def get_order_number(self):
        """Получает номер заказа"""
        return self.get_text_locator(MainPageLocators.ORDER_NUM)

    @allure.step('Ожидание загрузки кнопки Оформить заказ')
    def wait_load_main_page(self):
        """Ожидает загрузки главной страницы"""
        self.wait_for_load_element(MainPageLocators.PLACE_ORDER_BUTTON)