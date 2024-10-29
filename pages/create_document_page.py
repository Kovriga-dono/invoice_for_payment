import selene
from selene.api import *
import re
from models import data
from pages import locators
from selene.core import command as _advanced_commands
import allure

command = _advanced_commands


@allure.step("заполняем ИНН")
def set_inn():
    s(locators.inn).set(data.contact.inn)
    s(locators.inn_click).click()


@allure.step("заполняем обязательные поля")
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


@allure.step("закрываем модальное окно нажатием крестика")
def close_popup():
    s(locators.close_button).click()


@allure.step("в модальном окне нажимаем 'отмена'")
def reject_popup():
    s(locators.cancel_button).click()


@allure.step("в модальном окне нажимаем 'создать'")
def accept_popup():
    selene.browser.element(locators.save_button).perform(command.js.scroll_into_view)
    s(locators.save_button).click()


@allure.step("возвращаемся на вкладку после формирования документа")
def switch_tabs():
    browser.wait_until(lambda: browser.execute_script("return document.readyState") == 'complete')
    selene.browser.switch_to_next_tab()
    selene.browser.switch_to_previous_tab()


@allure.step("проверяем ИНН последнего созданного клиента")
def check_inn():
    s(locators.comment).click()
    selene.browser.element(locators.headder).perform(command.js.scroll_into_view)
    selene.browser.driver.refresh()
    s(locators.inn).click()
    b = re.search(r'\d+$', s(locators.inn_in_list).get(query.text)).group()
    a = data.contact.inn
    assert int(b) != int(a), "ошибка, клиент был сохранён"


@allure.step("выбираем ИНН из списка")
def chose_inn():
    s(locators.inn).click().should(be.visible)
    s(locators.inn_in_list).click()


@allure.step("заполняем адрес")
def set_addres():
    s(locators.addres).set(data.contact.addres)


@allure.step("проверяем открытие модального окна")
def check_modal_window():
    browser.should(have.no.text('Сохранить контрагента?'))


@allure.step("переходим на страницу контрагентов")
def counterparty_click():
    s(locators.counterparty_button).click()
