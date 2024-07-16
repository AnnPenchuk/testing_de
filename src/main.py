import logging

from Extracting import extract
from Validation import list_users
from Loading import add_data


logging.basicConfig(filename="../logs/py_log.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt='%d/%m/%Y %I:%M:%S %p')


def main(n):
    res = extract(n)
    new = list_users(res)
    for i in new:
        add_data(i)


if __name__ == "__main__":
    # n = input('укажите сколько пользователей хотите получить ')
    n='1'
    main(n)
