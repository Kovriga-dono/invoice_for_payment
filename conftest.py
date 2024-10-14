from selene.api import *
import pytest



# def pytest_addoption(parser):
#     parser.addoption("--remote", action="store_true", default=False, help="Запустить браузер удаленно")
#     parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера для запуска тестов")


@pytest.fixture()
def browser_c():
    config.driver_name = 'chrome'
    config.window_width = 1920
    config.window_height = 1080

