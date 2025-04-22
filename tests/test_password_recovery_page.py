import allure
from data.urls import URLS, MainUrl
from helpers.user_data import Person
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage
from pages.login_page import LoginPage


@allure.feature('Тесты восстановления пароля')
class TestRecoveryPage:
    """Тесты для страницы восстановления пароля"""

    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Проверяет переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_follow_to_the_password_recovery_page(self, driver):
        """Тест перехода на страницу восстановления пароля"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        assert recovery_page.check_recovery_form() and recovery_page.get_current_url() == (
                    MainUrl.MAIN_URL + URLS.URL_RECOVERY)

    @allure.title('Проверка восстановления пароля')
    @allure.description('Проверяет ввод почты и клик по кнопке "Восстановить" на странице восстановления пароля')
    def test_password_recovery_flow(self, driver):
        """Тест процесса восстановления пароля"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.send_email_to_email_field(Person.create_data_correct_user()["email"])
        recovery_page.click_recovery_btn()
        assert recovery_page.check_save_btn() and recovery_page.get_current_url() == (
                    MainUrl.MAIN_URL + URLS.URL_RESET_PASSWORD)

    @allure.title('Проверка подсветки поля пароля')
    @allure.description('Проверяет, что клик по кнопке показать/скрыть пароль подсвечивает поле')
    def test_password_field_highlight(self, driver):
        """Тест подсветки поля пароля"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        person_data = Person().create_data_correct_user()
        main_page.move_to_personal_account_btn_and_click()
        login_page.click_recovery_btn()
        recovery_page.send_email_to_email_field(person_data.get("email"))
        recovery_page.click_recovery_btn()
        assert recovery_page.check_active_password_field(person_data.get("password"))