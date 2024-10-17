from pages import main_page, create_document_page
from conftest import browser
import allure


@allure.feature("autotest example")
@allure.testcase("SKB_LAB-28327")
@allure.title("SKB_LAB-28327 : Отсутствие модального окна при добавлении контрагента")
def test_absence_window(browser):
    main_page.open_browser()
    main_page.login()
    create_document_page.chose_inn()
    create_document_page.set_addres()
    create_document_page.filling_fields()
    create_document_page.switch_tabs()
    create_document_page.check_modal_window()
    main_page.quit_browser()


