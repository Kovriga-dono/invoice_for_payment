Для запуска требуется установить необходимые пакеты и запустить тест, поочерёдно вызвав команды в консоли. 

pip install -r requirements.txt
pytest -v -s --alluredir results

для выгрузки allure отчета необходимо вызвать в терминале следующую команду:
allure serve results