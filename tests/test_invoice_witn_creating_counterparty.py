from pages import main_page, contragents_page, create_document_page
from conftest import browser
import allure


@allure.feature("autotest example")
@allure.testcase("SKB_LAB-28040")
@allure.title("SKB_LAB-28040 : Создание счета на оплату с добавдением контрагента")
def test_creating_counterparty(browser):
    # Открываем браузер, переходим на страницу входа в ДБО
    main_page.open_browser()
    # выполняется вход в ДБО
    main_page.login()
    # заполняется ИНН
    create_document_page.set_inn()
    # заполняются обязательные поля
    create_document_page.filling_fields()
    # создаем контрагента
    create_document_page.accept_popup()
    # переключаемся между вкладками
    contragents_page.switch_tabs()
    # переходим на страницу контрагентов
    create_document_page.counterparty_click()
    # закрываем появившееся модальное окно
    create_document_page.reject_popup()
    # сравниваем заполенные данные с данными в карточке контрагента
    contragents_page.output_data()
    # удаляем созданного контрагента
    contragents_page.delete_contragency()
    main_page.quit_browser()
