import logging

from src.Loading.connection import connection

def database_creation():
    try:
        cursor = connection.cursor()
        query = f'''CREATE TABLE IF NOT EXISTS users3 (
             user_id serial PRIMARY KEY, gender VARCHAR(255), name_title VARCHAR(255), name_first VARCHAR(255), name_last VARCHAR(255), age int, nat VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
        cursor.execute(query)

        query = f'''CREATE TABLE IF NOT EXISTS registration_data3 (
    user_id int PRIMARY KEY, email VARCHAR(255), username VARCHAR(255), password VARCHAR(255), password_md5 VARCHAR(255), password_validation VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) 
    REFERENCES users3 (user_id)
        ON DELETE cascade)'''
        cursor.execute(query)

        query = f'''CREATE TABLE IF NOT EXISTS media_data3 (
    user_id int PRIMARY KEY, picture VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) 
    REFERENCES users3 (user_id)
        ON DELETE cascade)'''
        cursor.execute(query)

        query = f'''CREATE TABLE IF NOT EXISTS contact_details3 (
    user_id int PRIMARY KEY, phone VARCHAR(255), cell VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) 
    REFERENCES users3 (user_id)
        ON DELETE cascade)'''
        cursor.execute(query)

        query = f'''CREATE TABLE IF NOT EXISTS locations3 (
    user_id int PRIMARY KEY, city_id serial UNIQUE, street_name VARCHAR(255), street_number int, postcode VARCHAR(255), latitude VARCHAR(255), longitude VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) 
    REFERENCES users3 (user_id)
        ON DELETE cascade)'''
        cursor.execute(query)

        query = f'''CREATE TABLE IF NOT EXISTS cities3 (
    city_id int PRIMARY KEY, city VARCHAR(255), state VARCHAR(255), country VARCHAR(255), timezone_offset VARCHAR(255), timezone_description VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) 
    REFERENCES locations3 (city_id)
        ON DELETE cascade)'''
        cursor.execute(query)

        cursor.close()
       # connection.close()
    except:
        print('Не удалось создать таблицы')
        logging.error("Не удалось создать таблицы")