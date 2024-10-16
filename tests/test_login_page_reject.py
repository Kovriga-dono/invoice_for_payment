from pages import main_page, create_document_page
from conftest import browser
import allure


@allure.feature("autotest example")
@allure.testcase("SKB_LAB-28054")
@allure.title("SKB_LAB-28054 : Кнопка 'Отменить' в модальном окне 'Сохранить контрагента?'")
def test_reject_popup(browser):
    main_page.open_browser()
    main_page.login()
    create_document_page.create_document()
    create_document_page.reject_popup()
    create_document_page.switch_tabs()
    create_document_page.check_inn()
