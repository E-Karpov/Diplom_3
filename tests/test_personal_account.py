import allure
from data.urls import URLS, MainUrl
from pages.main_page import HeaderPage
from pages.login_page import LoginPage
from pages.profile_area_page import ProfileAreaPage


@allure.feature('Тесты личного кабинета')
class TestProfileAreaPage:
    """Тесты для страницы личного кабинета"""

    @allure.title('Проверка перехода в личный кабинет')
    @allure.description('Проверяет переход в личный кабинет авторизованного пользователя')
    def test_navigate_to_user_profile(self, driver, create_new_user, login):
        """Тест перехода в личный кабинет"""
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        header.click_profile_area_btn()
        assert profile_area.check_profile_area_form() and profile_area.get_current_url() == (
                    MainUrl.MAIN_URL + URLS.URL_PROFILE_AREA)

    @allure.title('Проверка перехода в историю заказов')
    @allure.description('Проверяет переход в раздел истории заказов из личного кабинета')
    def test_view_order_history(self, driver, create_new_user, login):
        """Тест перехода в историю заказов"""
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        header.click_profile_area_btn()
        profile_area.click_history_orders_btn()
        assert profile_area.check_profile_area_form() and profile_area.get_current_url() == (
                    MainUrl.MAIN_URL + URLS.URL_HISTORY_ORDER)

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверяет выход пользователя из аккаунта')
    def test_exit_profile(self, driver, create_new_user, login):
        """Тест выхода из аккаунта"""
        header = HeaderPage(driver)
        profile_area = ProfileAreaPage(driver)
        login_page = LoginPage(driver)
        header.click_profile_area_btn()
        profile_area.click_exit_btn()
        assert login_page.check_authorization_form_verification() and login_page.get_current_url() == (
                    MainUrl.MAIN_URL + URLS.URL_LOGIN)