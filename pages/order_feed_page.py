import allure
from pages.base_page import BasePage
from locators.locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    """Класс для работы со страницей ленты заказов"""

    @allure.step('Получение кол-ва заказов')
    def check_counter_orders(self, locators):
        """Проверяет счетчик заказов"""
        return self.get_text_locator(locators)

    @allure.step('Клик на 1 заказ в "Ленте заказов"')
    def click_order_info(self):
        """Кликает по первому заказу в ленте"""
        self.click_button(OrderFeedLocators.ORDER_INFO_WINDOW)

    @allure.step('Проверка видимости формы заказа')
    def check_order_info_window(self):
        """Проверяет видимость формы с деталями заказа"""
        return self.check_element(OrderFeedLocators.ORDERS_INFO)

    @allure.step('Получение заказов "В работе"')
    def get_orders_in_jobs(self):
        """Получает список заказов в работе"""
        elements = self.get_text_locators(OrderFeedLocators.NUMBER_ORDER_IN_JOB)
        orders_list = []
        for element in elements:
            order_number = element.text[1:]
            orders_list.append(order_number)
        return orders_list

    @allure.step('Получение списка всех заказов в "Ленте заказов"')
    def get_text_all_orders(self):
        """Получает список всех заказов"""
        elements = self.get_orders_history()
        text_list = []
        for element in elements:
            text_list.append(element)
        return text_list

    @allure.step('Получение номеров заказов')
    def get_orders_history(self):
        """Получает историю заказов"""
        elements = self.get_text_locators(OrderFeedLocators.ORDER_HISTORY)
        orders_list = []
        for element in elements:
            order_number = element.text[2:]
            orders_list.append(order_number)
        return orders_list