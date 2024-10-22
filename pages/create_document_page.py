from selene import browser, have
import selene
from selene.api import *
import re
from models import data
from pages import locators
from selene.core import command as _advanced_commands

command = _advanced_commands


# заполняем ИНН организации
def set_inn():
    s(locators.inn).set(data.contact.inn)
    s(locators.inn_click).click()


# заполняем обязательные поля
def filling_fields():
    browser.wait_until(lambda: browser.execute_script("return document.readyState") == 'complete')
    selene.browser.element(locators.bot).perform(command.js.scroll_into_view)
    s(locators.service).set(data.contact.service)
    s(locators.quantity).click()
    s(locators.quantity).set(data.contact.quantity)
    s(locators.price).set(data.contact.price)
    selene.browser.element(locators.cr_button).perform(command.js.scroll_into_view)
    s(locators.comment).click()
    s(locators.cr_button).click()


# закрытие модального окна на "крестик"
def close_popup():
    s(locators.close_button).click()


# закрытие модального окна кнопкой "отмена"
def reject_popup():
    s(locators.cancel_button).click()


# кнопка поддверждения модального окна
def accept_popup():
    selene.browser.element(locators.save_button).perform(command.js.scroll_into_view)
    s(locators.save_button).click()


# переключение между активными вкладками
def switch_tabs():
    browser.wait_until(lambda: browser.execute_script("return document.readyState") == 'complete')
    selene.browser.switch_to_next_tab()
    selene.browser.switch_to_previous_tab()


# сравнение инн последнего созданного контрагента
def check_inn():
    s(locators.comment).click()
    selene.browser.element(locators.headder).perform(command.js.scroll_into_view)
    selene.browser.driver.refresh()
    s(locators.inn).click()
    b = re.search(r'\d+$', s(locators.inn_in_list).get(query.text)).group()
    a = data.contact.inn
    assert int(b) != int(a)


# выбор инн
def chose_inn():
    s(locators.inn).click().should(be.visible)
    s(locators.inn_in_list).click()


# установка адреса
def set_addres():
    s(locators.addres).set(data.contact.addres)


# проверка открытия модального окна
def check_modal_window():
    browser.should(have.no.text('Сохранить контрагента?'))


# переход на страницу контрагентов
def counterparty_click():
    s(locators.counterparty_button).click()
