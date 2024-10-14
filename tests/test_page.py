import pages.main_page
from conftest import browser_c
import allure


#вход в ДБО
@allure.feature('autotest example')
@allure.story('filling Chrome')
def test_fill_contact(browser_c):
    with allure.step('open Chrome'):
        pages.main_page.open_browser()
    pages.main_page.fill_login()
    pages.main_page.fill_pass()
    pages.main_page.log_click()
    pages.main_page.fill_accept()
    pages.main_page.fill_inn()

# def test_create_document():
#     pages.main_page.doc_click()
#     pages.main_page.create_doc_click()
