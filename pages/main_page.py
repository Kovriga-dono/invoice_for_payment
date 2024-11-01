from selene.api import *
from models import data
from pages import locators
import allure
from pages import urls


@allure.step("открываем браузер, переходим на страницу создания счета")
def open_browser():
    browser.open(urls.main_page)


@allure.step("вход в ДБО")
def login():
    s(locators.login).set(data.contact.log)
    s(locators.password).set(data.contact.pas)
    s(locators.log_button).click()
    s(locators.accept).set(data.contact.pas)
    browser.wait_until(lambda: browser.execute_script("return document.readyState") == 'complete')
    assert browser.driver.current_url == urls.main_page, "открыта не корректная страница"


@allure.step("закрываем браузер")
def quit_browser():
    browser.quit()
