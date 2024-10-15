from pages import main_page, create_document_page
from conftest import browser
import allure


# вход в ДБО
@allure.feature("autotest example")
@allure.testcase("SKB_LAB-28056")
@allure.title("SKB_LAB-28056 : Кнопка 'Крестик' в модальном окне 'Сохранить контрагента?'")
# Открываем браузер, переходим на страницу создания документа
def test_fill_contact(browser):
    main_page.open_browser()


# Вводим логин, пароль, код подтверждения
def test_login():
    main_page.login()

# Заполнение страницы создания документа
def test_create_document():
    create_document_page.create_document()


# Закрываем всплывающее окно
def test_close_popup():
    create_document_page.close_popup()
