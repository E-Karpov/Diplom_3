import allure
from data.urls import URLS, MainUrl
from pages.main_page import MainPage, HeaderPage


@allure.feature('Тесты главной страницы')
class TestMainPage:
    """Тесты для главной страницы"""

    @allure.title('Проверка перехода по клику на "Конструктор"')
    @allure.description('Проверяет переход на страницу конструктора при клике на соответствующую кнопку')
    def test_follow_to_constructor_page(self, driver):
        """Тест перехода в конструктор"""
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        header.click_constructor_btn()
        assert main_page.check_constructor_form() and main_page.get_current_url() == MainUrl.MAIN_URL

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    @allure.description('Проверяет переход на страницу ленты заказов при клике на соответствующую кнопку')
    def test_follow_to_orders_feed_page(self, driver):
        """Тест перехода в ленту заказов"""
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_feed_btn()
        assert main_page.check_orders_feed_form() and main_page.get_current_url() == (MainUrl.MAIN_URL + URLS.URL_FEED)

    @allure.title('Проверка отображения деталей ингредиента')
    @allure.description('Проверяет, что при клике на ингредиент появляется всплывающее окно с деталями')
    def test_check_fluorescent_bun_form(self, driver):
        """Тест отображения деталей ингредиента"""
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_btn()
        assert main_page.check_fluorescent_bun_form()

    @allure.title('Проверка закрытия всплывающего окна')
    @allure.description('Проверяет закрытие всплывающего окна с деталями ингредиента по крестику')
    def test_close_fluorescent_bun_form(self, driver):
        """Тест закрытия окна деталей ингредиента"""
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun_btn()
        main_page.close_popup_form()
        assert main_page.check_close_fluorescent_bun_form()

    @allure.title('Проверка счетчика ингредиента')
    @allure.description('Проверяет увеличение счетчика ингредиента при добавлении его в заказ')
    def test_counter_ingredient(self, driver):
        """Тест счетчика ингредиента"""
        main_page = MainPage(driver)
        main_page.add_bun()
        assert int(main_page.check_counter_ingredient()) > 0

    @allure.title('Проверка оформления заказа')
    @allure.description('Проверяет возможность оформления заказа авторизованным пользователем')
    def test_create_order(self, driver, create_new_user, login):
        """Тест оформления заказа"""
        header = HeaderPage(driver)
        main_page = MainPage(driver)
        header.click_constructor_btn()
        main_page.create_order()
        assert main_page.check_order_form()