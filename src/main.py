from Extracting.parsing import receiving_data
#from src.settings import settings
from Validation.valid import Users_valid, list_users
from src.Extracting import connect_api
from src.Extracting.connect_api import api_request
from src.Loading.add_data import add_data
from src.Loading.crud_data import insert,select,delete,update
from src.Loading.database_creation import database_creation
from src.Loading.connection import connection
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
#logging.debug("A DEBUG Message")
#logging.info("An INFO")
#logging.warning("A WARNING")
#logging.error("An ERROR")
#logging.critical("A message of CRITICAL severity")



if __name__ == "__main__":

    n = input('укажите сколько пользователей хотите получить ')
    try:
        int(n)
        print('Вы ввели ',n)
    except:
        print('Нужно указать целое число')
        logging.error("неправильно задано число пользователей")

    #n='2'
    try:
        res=receiving_data(n)
        try:
            new=list_users(res)
        except:
            print('Не удалось проверить правильность полученных данных')
            logging.error("функция проверки валидности не сработала")

       # print(new)
        try:
            database_creation()
            print('Выполнено создание таблиц')
        except:
            print('Не удалось создать таблицы')
            logging.error("Не удалось создать таблицы")
        for i in new:
            add_data(i)
        print('Выполнено добавление данных')
    except:
        print('Не удалось получить данные из API')
        logging.error("отсутствует подключение к API")

connection.close()