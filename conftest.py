import pytest
from selenium import webdriver
import requests
from data.urls import MainUrl
from helpers.user_data import Person
from data.urls import Endpoints
from data.ingredients import Ingredients
from pages.main_page import HeaderPage, MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    """Фикстура для инициализации драйвера"""
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(MainUrl.MAIN_URL)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(MainUrl.MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_new_user():
    """Фикстура для создания тестового пользователя"""
    payload = Person.create_data_correct_user()
    response = requests.post(MainUrl.MAIN_URL + Endpoints.CREATE_USER, data=payload)
    try:
        token = response.json().get("accessToken")
        yield payload, response
        if token:
            requests.delete(MainUrl.MAIN_URL + Endpoints.DELETE_USER,
                          headers={"Authorization": token})
    except Exception as e:
        pytest.fail(f"Failed to create user: {str(e)}")




@pytest.fixture
def login(driver, create_new_user):
    """Фикстура для авторизации пользователя"""
    create_user_data = create_new_user[0]
    header_page = HeaderPage(driver)
    login_page = LoginPage(driver)
    header_page.click_profile_area_btn()
    login_page.login(create_user_data["email"], create_user_data["password"])
    main_page = MainPage(driver)
    main_page.wait_load_main_page()


@pytest.fixture
def create_order(create_new_user):
    """Фикстура для создания тестового заказа"""
    token = create_new_user[1].json()["accessToken"]
    headers = {'Authorization': token}
    response = requests.post(
        MainUrl.MAIN_URL + Endpoints.CREATE_ORDER,
        headers=headers,
        data=Ingredients.CORRECT_INGREDIENTS_DATA
    )
    return response.json()["order"]["number"]


def pytest_make_parametrize_id(val):
    """Функция для корректного отображения параметров в тестах"""
    return repr(val)