import logging
import requests


def api_request(quantity: int) -> dict:
    try:
        url='https://randomuser.me/api/?results='
        url_ ="".join([url, str(quantity)])
        response = requests.get(url_)

        if response.status_code == 200:
            logging.debug('Выполнено подключение к API')
            return response.json()
        else:
            logging.error(f"Не удалось подключиться к API - status {response.status_code}")
    except Exception as e:
        logging.error(f"Не удалось подключиться к API.\n{e}")
