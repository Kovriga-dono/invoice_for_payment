import selene
from selene.api import *
import re
from models import data
from pages import locators, urls
from selene.core import command as _advanced_commands
import allure

command = _advanced_commands


@allure.step("сравниваем заполненные данные с данными в карточке клиента")
def output_data():
    browser.wait_until(lambda: browser.execute_script("return document.readyState") == 'complete')
    assert browser.driver.current_url == urls.contragents_page, "открыта не корректная страница"
    output_comp_name = s(locators.contragent_name).get(query.text)
    assert output_comp_name == data.contact.company_name, "имя компании не совпадает"
    output_inn = s(locators.contragent_inn).get(query.text)
    assert output_inn == data.contact.inn, "ИНН не совпадает"
    output_kpp = re.search(r'\d+', s(locators.contragent_kpp).get(query.text)).group()
    assert output_kpp == data.contact.kpp, "КПП не совпадает"
    s(locators.contragent_name).click()
    s(locators.show_addres).click()
    output_addres = s(locators.contragent_addres).get(query.text)
    assert output_addres == data.contact.addres, "Адрес не совпадает"


@allure.step("возвращаемся на вкладку после формирования документа")
def switch_tabs():
    browser.wait_until(lambda: browser.execute_script("return document.readyState") == 'complete')
    window_handles = browser.driver.window_handles
    browser.driver.switch_to.window(window_handles[1])
    selene.browser.close()
    browser.driver.switch_to.window(window_handles[0])


@allure.step("удаляем созданного клиента")
def delete_contragency():
    s(locators.menu_button).click()
    s(locators.delete_button).click()
    s(locators.save_button).click()
    output_comp_name = s(locators.contragent_name).get(query.text)
    assert output_comp_name != data.contact.company_name, "последний созданный клиент не был удалён!"
