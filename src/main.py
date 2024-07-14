from Extracting.parsing import receiving_data
# from src.settings import settings
from Validation.valid import Users_valid, list_users
from src.Extracting import connect_api
from src.Extracting.connect_api import api_request
from src.Loading.add_data import add_data
from src.Loading.crud_data import insert,select,delete,update
from src.Loading.database_creation import database_creation
from src.Loading.connection import connection
import logging
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

if __name__ == "__main__":
  #  n = input('укажите сколько пользователей хотите получить ')
    n='2'
    res=receiving_data(api_request(n).get('results'))
    new=list_users(res)
    database_creation()
    for i in new:
            add_data(i)
    print('Выполнено добавление данных')

