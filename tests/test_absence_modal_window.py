from pages import main_page, create_document_page
from conftest import browser
import allure


@allure.feature("autotest example")
@allure.testcase("SKB_LAB-28327")
@allure.title("SKB_LAB-28327 : Кнопка 'Отменить' в модальном окне 'Сохранить контрагента?'")
def test_absence_window(browser):
    main_page.open_browser()
    main_page.login()
