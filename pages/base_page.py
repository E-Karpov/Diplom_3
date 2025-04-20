from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    """Базовый класс для работы со страницами"""

    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver

    def get_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url

    def wait_element_clickable(self, locator, timeout=5):
        """Ожидание кликабельности элемента"""
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_load_element(self, locator, timeout=20):
        """Ожидание загрузки элемента"""
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_button(self, locator):
        """Клик по кнопке"""
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).click()

    def send_keys_to_field(self, locator, text):
        """Ввод текста в поле"""
        self.wait_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    def get_text_locator(self, locator, timeout=5):
        """Получение текста элемента"""
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def get_text_locators(self, locator, timeout=5):
        """Получение текста нескольких элементов"""
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def check_element(self, locator):
        """Проверка видимости элемента"""
        self.wait_for_load_element(locator)
        return self.driver.find_element(*locator)

    def check_element_is_not_visible(self, locator, timeout=10):
        """Проверка невидимости элемента"""
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def drag_and_drop(self, element_one, element_two):
        """Перетаскивание элемента"""
        element = self.driver.find_element(*element_one)
        target = self.driver.find_element(*element_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    def move_to_element_and_click(self, locator):
        """Наведение на элемент и клик"""
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()