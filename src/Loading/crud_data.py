import logging

from src.Loading.connection import connection


def insert(connection, name,columns,values,foreign_key):
    try:
        with connection().cursor() as cursor:
            query = f'''INSERT INTO {name} ({columns}) VALUES {values} RETURNING {foreign_key}'''
            cursor.execute(query,values)
            res_id = cursor.fetchall()[0][0]
            logging.debug(f"данные добавлены в таблицу {name}.")
            return res_id
    except Exception as e:
        logging.debug(f"Не удалось добавить данные в таблицу {name}.\n{e}")


def select(name):
    try:
        with connection().cursor() as cursor:
            query = f'''
            SELECT * FROM {name} '''
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                print(i)
    except Exception as e:
        logging.error(f"Не удалось получить данные из таблицы {name}.\n{e}")


def delete(name,condition):
    try:
        with connection().cursor() as cursor:
            query = f'''
            DELETE FROM {name} 
                 WHERE {condition}'''
            cursor.execute(query)
    except Exception as e:
        logging.error(f"Не удалось удалить данные из таблицы {name}.\n{e}")


def update(new,name,columns,condition):
    new_values=new[0]['email']
    try:
        with connection().cursor() as cursor:
            query = f'''
            UPDATE {name} 
            SET {columns}='{new_values}'
            WHERE {condition}'''
            cursor.execute(query)
    except Exception as e:
        logging.error(f"Не удалось обновить данные в таблицу {name}.\n{e}")
