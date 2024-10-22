from pages import main_page, contragents_page, create_document_page
from conftest import browser
import allure


@allure.feature("autotest example")
@allure.testcase("SKB_LAB-28040")
@allure.title("SKB_LAB-28040 : Создание счета на оплату с добавдением контрагента")
def test_creating_counterparty(browser):
    main_page.open_browser()
    main_page.login()
    create_document_page.set_inn()
    create_document_page.filling_fields()
    create_document_page.accept_popup()
    contragents_page.switch_tabs()
    create_document_page.counterparty_click()
    create_document_page.reject_popup()
    contragents_page.output_data()
    contragents_page.delete_contragency()
    main_page.quit_browser()
