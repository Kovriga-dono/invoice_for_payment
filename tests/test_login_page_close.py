from pages import main_page, create_document_page
from conftest import browser
import allure


# вход в ДБО
@allure.feature("autotest example")
@allure.testcase("SKB_LAB-28056")
@allure.title("SKB_LAB-28056 : Кнопка 'Крестик' в модальном окне 'Сохранить контрагента?'")
# Открываем браузер, переходим на страницу создания документа
def test_close_popup(browser):
    main_page.open_browser()
    main_page.login()
    create_document_page.create_document()
    create_document_page.close_popup()
    create_document_page.switch_tabs()
    create_document_page.check_inn()
