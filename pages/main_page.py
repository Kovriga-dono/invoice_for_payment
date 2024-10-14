from selene.api import *
import re
import time
from models import locators, data
import allure


def open_browser():
    with allure.step('open page'):
        browser.open('https://delo-prod.skblab.ru/documents/create?documents=invoice')


def fill_login():
    s(locators.login).set(data.contact.log)


def fill_pass():
    s(locators.password).set(data.contact.pas)


def log_click():
    s(locators.log_button).click()
    time.sleep(5)


def fill_accept():
    s(locators.accept).set(data.contact.pas)
    time.sleep(3)


# def doc_click():
#     s(locators.doc_button).click()
#
#
# def create_doc_click():
#     s(locators.create_doc_button).click()


def fill_inn():
    s(locators.inn).set(data.contact.inn)
    s(locators.inn_click).click()
