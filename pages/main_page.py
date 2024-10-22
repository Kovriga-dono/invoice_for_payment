from selene.api import *
from models import data
from pages import locators
import allure


def open_browser():
    with allure.step('open page'):
        browser.open('https://delo-prod.skblab.ru/documents/create?documents=invoice')


def login():
    s(locators.login).set(data.contact.log)
    s(locators.password).set(data.contact.pas)
    s(locators.log_button).click()
    s(locators.accept).set(data.contact.pas)


def quit_browser():
    browser.quit()


