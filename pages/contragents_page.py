import selene
from selene.api import *
import re
from models import locators, data
import allure
from selene.core import command as _advanced_commands


company_name = re.search(s(locators.inn).get(query.text)).group()
company_inn = re.search(s(locators.check_inn).get(query.text)).group()
company_kpp = re.search(s(locators.check_kpp).get(query.text)).group()
company_addres = re.search(s(locators.check_addres).get(query.text)).group()


def check_data():
    d = re.search(r'\d+$', s(locators.contragent_name).get(query.text)).group()
    assert str(d) == str(company_name)
    a = re.search(r'\d+$', s(locators.contragent_inn).get(query.text)).group()
    assert str(a) == str(company_inn)
    b = re.search(r'\d+$', s(locators.contragent_kpp).get(query.text)).group()
    assert str(b) == str(company_kpp)
    c = re.search(r'\d+$', s(locators.contragent_addres).get(query.text)).group()
    assert str(c) == str(company_addres)
    