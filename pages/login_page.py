import allure
from pages.base_page import BasePage
from locators.locators import AuthPageLocators


class LoginPage(BasePage):
    """Класс для работы со страницей авторизации"""

    @allure.step('Проверка отображения формы логина')
    def check_authorization_form_verification(self):
        """Проверяет видимость формы авторизации"""
        return self.check_element(AuthPageLocators.AUTH_FORM)

    @allure.step('Заполнение поля "Email"')
    def send_email_to_email_field(self, email):
        """Вводит email в поле ввода"""
        self.send_keys_to_field(AuthPageLocators.EMAIL_INPUT, email)

    @allure.step('Заполнение поля "Password"')
    def send_password_to_password_field(self, password):
        """Вводит пароль в поле ввода"""
        self.send_keys_to_field(AuthPageLocators.PASSWORD_INPUT, password)

    @allure.step('Клик на кнопку "Войти"')
    def click_login_btn(self):
        """Кликает по кнопке входа"""
        self.move_to_element_and_click(AuthPageLocators.LOGIN_ACCOUNT_BTN)

    @allure.step('Авторизация на сайте')
    def login(self, email, password):
        """Выполняет авторизацию пользователя"""
        self.send_email_to_email_field(email)
        self.send_password_to_password_field(password)
        self.click_login_btn()

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_recovery_btn(self):
        """Кликает по кнопке восстановления пароля"""
        self.move_to_element_and_click(AuthPageLocators.RECOVER_BTN)

    @allure.step('Клик на кнопку "Зарегистрироваться"')
    def click_register_btn(self):
        """Кликает по кнопке регистрации"""
        self.move_to_element_and_click(AuthPageLocators.REGISTRATION_BTN)