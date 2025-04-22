import allure
from pages.base_page import BasePage
from locators.locators import RecoveryPageLocators


class RecoveryPage(BasePage):
    """Класс для работы со страницей восстановления пароля"""

    @allure.step('Проверка формы восстановления пароля')
    def check_recovery_form(self):
        """Проверяет видимость формы восстановления пароля"""
        return self.check_element(RecoveryPageLocators.RECOVERY_TEXT_FORM)

    @allure.step('Заполнение формы Email')
    def send_email_to_email_field(self, email):
        """Вводит email в поле ввода"""
        self.send_keys_to_field(RecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик по кнопке Восстановить')
    def click_recovery_btn(self):
        """Кликает по кнопке восстановления"""
        self.click_button(RecoveryPageLocators.RECOVER_BTN)

    @allure.step('Клик по кнопке Войти')
    def click_login_btn(self):
        """Кликает по кнопке входа"""
        self.click_button(RecoveryPageLocators.LOGIN_ACCOUNT_BTN)

    @allure.step('Заполнение поля Пароль')
    def send_password_to_password_field(self, password):
        """Вводит пароль в поле ввода"""
        self.send_keys_to_field(RecoveryPageLocators.PASSWORD_INPUT, password)

    @allure.step('Заполнение поля Код из письма')
    def send_code_to_code_field(self, code):
        """Вводит код из письма"""
        self.send_keys_to_field(RecoveryPageLocators.CODE_FROM_MAIL, code)

    @allure.step('Клик по кнопке Сохранить')
    def click_save_btn(self):
        """Кликает по кнопке сохранения"""
        self.click_button(RecoveryPageLocators.SAVE_BTN)

    @allure.step('Проверка подсветки поля Пароль')
    def check_active_password_field(self, password):
        """Проверяет подсветку поля пароля"""
        self.send_password_to_password_field(password)
        # Ожидание исчезновения модального окна
        self.wait_element_clickable(RecoveryPageLocators.SHOW_BTN, timeout=10)
        self.click_button(RecoveryPageLocators.SHOW_BTN)
        return self.check_element(RecoveryPageLocators.INPUT_FIELD_ACTIVE)

    @allure.step('Проверка отображения кнопки Сохранить')
    def check_save_btn(self):
        """Проверяет видимость кнопки сохранения"""
        return self.check_element(RecoveryPageLocators.SAVE_BTN)