from pages import main_page, create_document_page
from conftest import browser
import allure


@allure.feature("autotest example")
@allure.testcase("SKB_LAB-28327")
@allure.title("SKB_LAB-28327 : Отсутствие модального окна при добавлении контрагента")
def test_absence_window(browser):
    # Открываем браузер, переходим на страницу входа в ДБО
    main_page.open_browser()
    # выполняется вход в ДБО
    main_page.login()
    # выбираем существующего контрагента
    create_document_page.chose_inn()
    # устанавливаем адрес
    create_document_page.set_addres()
    # заполняем обязательные поля
    create_document_page.filling_fields()
    # переключаемся между активными вкладками
    create_document_page.switch_tabs()
    # проверяем отсутствие модального окна
    create_document_page.check_modal_window()
    main_page.quit_browser()


