import allure
import pytest
from pages.main_page import HeaderPage
from pages.order_feed_page import OrderFeedPage
from locators.locators import OrderFeedLocators
from helpers.helpers import Order


@allure.feature('Тесты ленты заказов')
class TestOrderFeedPage:
    """Тесты для страницы ленты заказов"""

    @allure.title('Проверка деталей заказа')
    @allure.description('Проверяет отображение деталей заказа при клике на него')
    def test_view_order_details_in_feed(self, driver):
        """Тест отображения деталей заказа"""
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        feed_order.click_order_info()
        assert feed_order.check_order_info_window()

    @allure.title('Проверка отображения заказа в работе')
    @allure.description('Проверяет, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_order_in_progress_section(self, driver, create_new_user, login):
        """Тест отображения заказа в работе"""
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        order.create_order(create_new_user)
        orders_in_jobs = feed_order.get_orders_in_jobs()
        user_order = str(order.get_user_orders(create_new_user))
        assert user_order in orders_in_jobs

    @allure.title('Проверка истории заказов')
    @allure.description('Проверяет, что заказы пользователя отображаются в истории заказов')
    def test_check_user_orders_in_orders_history(self, driver, create_new_user, create_order, login):
        """Тест отображения заказов в истории"""
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        user_order = str(order.get_user_orders(create_new_user))
        orders_history_in_feed = feed_order.get_orders_history()
        assert user_order in orders_history_in_feed

    @allure.title('Проверка счетчиков заказов')
    @allure.description('Проверяет увеличение счетчиков заказов при создании нового заказа')
    @pytest.mark.parametrize('counter',
                             [OrderFeedLocators.DAILY_ORDERS_COUNTER, OrderFeedLocators.TOTAL_ORDERS_COUNTER])
    def test_update_counter_orders(self, driver, create_new_user, login, counter):
        """Тест обновления счетчиков заказов"""
        order = Order()
        header = HeaderPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_feed_btn()
        now_counter = int(feed_order.check_counter_orders(counter))
        order.create_order(create_new_user)
        new_counter = int(feed_order.check_counter_orders(counter))
        assert new_counter > now_counter