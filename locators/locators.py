from selenium.webdriver.common.by import By


class HeaderPageLocators:
    """Локаторы для хедера сайта"""

    CONSTRUCTOR_BTN = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")  # Кнопка конструктора
    ORDER_FEED_BTN = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")  # Кнопка ленты заказов
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")  # Кнопка личного кабинета


class MainPageLocators:
    """Локаторы для главной страницы"""

    ORDER_FEED_FORM = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")  # Форма ленты заказов
    CONSTRUCTOR_FORM = (
    By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")  # Форма конструктора
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка оформления заказа
    FLUORESCENT_BUN_BTN = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")  # Кнопка флюоресцентной булки
    CLOSE_POPUP_FORM = (By.XPATH, '//button[contains(@class,"close")]')  # Кнопка закрытия модального окна
    COUNTER_INGREDIENT = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")  # Счетчик ингредиента
    ORDER_FORM = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")  # Форма оформленного заказа
    ORDER_BASKET = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")  # Корзина заказа
    ORDER_NUM = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")  # Номер заказа
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка личного кабинета
    POPUP_FORM_INGREDIENTS = (By.XPATH, "//h2[text()= 'Детали ингредиента']")  # Форма деталей ингредиента


class AuthPageLocators:
    """Локаторы для страницы авторизации"""

    AUTH_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Форма авторизации
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    LOGIN_ACCOUNT_BTN = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка входа
    REGISTRATION_BTN = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # Кнопка регистрации
    RECOVER_BTN = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Кнопка восстановления пароля


class RecoveryPageLocators:
    """Локаторы для страницы восстановления пароля"""

    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    RECOVER_BTN = (By.XPATH, ".//button[text() = 'Восстановить']")  # Кнопка восстановления
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка входа
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Введите новый пароль']")  # Поле ввода пароля
    CODE_FROM_MAIL = (By.XPATH, ".//label[text() = 'Введите код из письма']")  # Поле ввода кода
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка сохранения
    RECOVERY_TEXT_FORM = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")  # Форма восстановления
    SHOW_BTN = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")  # Кнопка показа пароля
    INPUT_FIELD_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")  # Подсвеченное поле


class PersonalAreaLocators:
    """Локаторы для личного кабинета"""

    PROFILE_FORM = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # Форма профиля
    PROFILE_BTN = (By.XPATH, ".//a[text() = 'Профиль']")  # Кнопка профиля
    ORDER_HISTORY_BTN = (By.XPATH, ".//a[text() = 'История заказов']")  # Кнопка истории заказов
    HISTORY_ORDER_FORM = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")  # Форма истории заказов
    NUMBER_ORDER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")  # Номер заказа
    CANCEL_BTN = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка отмены
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка сохранения
    EXIT_BTN = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка выхода


class OrderFeedLocators:
    """Локаторы для ленты заказов"""

    TITLE_ORDERS_LIST = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок страницы
    ORDERS_INFO = (By.XPATH, '//p[text()="Cостав"]')  # Окно деталей заказа
    TOTAL_ORDERS_COUNTER = (
    By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # Счетчик всех заказов
    DAILY_ORDERS_COUNTER = (
    By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # Счетчик заказов за день
    NUMBER_ORDER_IN_JOB = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")  # Заказы в работе
    ORDER_INFO_WINDOW = (
    By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")  # Первый заказ в истории
    ORDER_HISTORY = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')  # Все заказы в истории