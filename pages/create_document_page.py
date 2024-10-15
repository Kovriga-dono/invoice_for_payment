from selene.api import *
import re
import time
from models import locators, data
import allure
from selene.core import command as _advanced_commands
command = _advanced_commands


def fill_inn():
    s(locators.inn).set(data.contact.inn)
    s(locators.inn_click).click()
    browser.element(locators.cr_button).perform(command.js.scroll_into_view)
    s(locators.service).set(data.contact.service)
    s(locators.quantity).set(data.contact.quantity)
    s(locators.price).set(data.contact.price)
    s(locators.comment).click()
    time.sleep(2)
    s(locators.cr_button).click()
    s(locators.close_button).click()
    time.sleep(5)
    browser.switch_to_next_tab()
    s(locators.close_invoice_button).click()
    time.sleep(5)
