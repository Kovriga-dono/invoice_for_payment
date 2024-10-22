from pages import main_page, create_document_page
from conftest import browser
import allure


@allure.feature("autotest example")
@allure.testcase("SKB_LAB-28054")
@allure.title("SKB_LAB-28054 : Кнопка 'Отменить' в модальном окне 'Сохранить контрагента?'")
def test_reject_popup(browser):
    # Открываем браузер, переходим на страницу входа в ДБО
    main_page.open_browser()
    # выполняется вход в ДБО
    main_page.login()
    # заполняется ИНН
    create_document_page.set_inn()
    # заполняются обязательные поля
    create_document_page.filling_fields()
    # закрытие модального окна
    create_document_page.reject_popup()
    # переключение между активными вкладками
    create_document_page.switch_tabs()
    # проверяем ИНН последнего созданного клиента
    create_document_page.check_inn()
    main_page.quit_browser()
