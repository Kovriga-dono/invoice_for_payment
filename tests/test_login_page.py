from pages import main_page, create_document_page
from conftest import browser_c
import allure


#вход в ДБО
@allure.feature('autotest example')
@allure.story('filling Chrome')
def test_fill_contact(browser_c):
    main_page.open_browser()


def test_create_document():
    create_document_page.fill_inn()

