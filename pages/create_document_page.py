import selene
from selene.api import *
import re
from models import locators, data
import allure
from selene.core import command as _advanced_commands
command = _advanced_commands


def set_inn():
    s(locators.inn).set(data.contact.inn)
    s(locators.inn_click).click()


def filling_fields():
    selene.browser.element(locators.bot).perform(command.js.scroll_into_view)
    s(locators.service).set(data.contact.service)
    s(locators.quantity).set(data.contact.quantity)
    s(locators.price).set(data.contact.price)
    s(locators.comment).click()
    s(locators.cr_button).click()


def close_popup():
    s(locators.close_button).click()


def reject_popup():
    s(locators.cancel_button).click()


def accept_popup():
    s(locators.save_button).click()


def switch_tabs():
    selene.browser.switch_to_next_tab()
    selene.browser.switch_to_previous_tab()


def check_inn():
    s(locators.comment).click()
    selene.browser.element(locators.headder).perform(command.js.scroll_into_view)
    selene.browser.driver.refresh()
    s(locators.inn).click()
    b = re.search(r'\d+$', s(locators.inn_in_list).get(query.text)).group()
    a = data.contact.inn
    assert int(b) != int(a)


def chose_inn():
    s(locators.inn).click()
    s(locators.inn_in_list).click()


def set_addres():
    s(locators.addres).set(data.contact.addres)


def check_modal_window():
    browser.should(have.no.text('Сохранить контрагента?'))


def counterparty_click():
    s(locators.counterparty_button).click()

