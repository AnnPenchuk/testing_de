import logging
import requests



def api_request(n):
    quantity=n
    url ="https://randomuser.me/api/?results="
    url = "".join([url, quantity])
    try:
        response = requests.get(url)
        print('Выполнено подключение к API')
    except:
        print('Не удалось подключиться к API')
        logging.error("Не удалось подключиться к API")
    res = response.json()
    return res



