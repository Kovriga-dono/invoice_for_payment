from selene import browser
from selene.api import *
import re
from models import locators, data
import allure
from selene.core import command as _advanced_commands
command = _advanced_commands


def create_document():
    s(locators.inn).set(data.contact.inn)
    s(locators.inn_click).click()
    browser.element(locators.bot).perform(command.js.scroll_into_view)
    s(locators.service).set(data.contact.service)
    s(locators.quantity).set(data.contact.quantity)
    s(locators.price).set(data.contact.price)
    s(locators.comment).click()
    s(locators.cr_button).click()


def close_popup():
    s(locators.close_button).click()


def reject_popup():
    s(locators.cancel_button).click()


def switch_tabs():
    browser.switch_to_next_tab()
    browser.switch_to_previous_tab()


def check_inn():
    s(locators.comment).click()
    browser.element(locators.headder).perform(command.js.scroll_into_view)
    browser.driver.refresh()
    s(locators.inn).click()
    b = re.search(r'\d+$', s(locators.inn_in_list).get(query.text)).group()
    a = data.contact.inn
    assert int(b) != int(a)
    browser.driver.quit()
