from pages import main_page, create_document_page, contragents_page
from conftest import browser
import allure


@allure.epic("ДБО")
@allure.feature("Создание счета на оплату")
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


@allure.testcase("SKB_LAB-28056")
@allure.title("SKB_LAB-28056 : Кнопка 'Крестик' в модальном окне 'Сохранить контрагента?'")
def test_close_popup(browser):
    main_page.open_browser()
    main_page.login()
    create_document_page.set_inn()
    create_document_page.filling_fields()
    create_document_page.switch_tabs()
    create_document_page.close_popup()
    create_document_page.check_inn()
    main_page.quit_browser()


@allure.testcase("SKB_LAB-28054")
@allure.title("SKB_LAB-28054 : Кнопка 'Отменить' в модальном окне 'Сохранить контрагента?'")
def test_reject_popup(browser):
    main_page.open_browser()
    main_page.login()
    create_document_page.set_inn()
    create_document_page.filling_fields()
    create_document_page.reject_popup()
    create_document_page.switch_tabs()
    create_document_page.check_inn()
    main_page.quit_browser()
