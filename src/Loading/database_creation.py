from src.Loading.connection import connection

def database_creation():
    cursor = connection.cursor()
    query = f'''
    CREATE TABLE IF NOT EXISTS users (
         user_id serial PRIMARY KEY, gender VARCHAR(255), name_title VARCHAR(255), name_first VARCHAR(255), name_last VARCHAR(255), age int, nat VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
    cursor.execute(query)

    query = f'''
        CREATE TABLE IF NOT EXISTS registration_data (
             user_id serial PRIMARY KEY, email VARCHAR(255), username VARCHAR(255), password VARCHAR(255), password_md5 VARCHAR(255), password_validation VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
    cursor.execute(query)

    query = f'''
            CREATE TABLE IF NOT EXISTS media_data (
                 user_id serial PRIMARY KEY, picture BYTEA, dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
    cursor.execute(query)

    query = f'''
            CREATE TABLE IF NOT EXISTS contact_details (
                 user_id serial PRIMARY KEY, phone VARCHAR(255), cell VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
    cursor.execute(query)

    query = f'''
                CREATE TABLE IF NOT EXISTS locations (
                     user_id serial PRIMARY KEY, city_id int, street_name VARCHAR(255), street_number int, postcode VARCHAR(255), latitude int, longitude int, dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
    cursor.execute(query)

    query = f'''
                  CREATE TABLE IF NOT EXISTS cities (
                       city_id serial PRIMARY KEY, city VARCHAR(255), state VARCHAR(255), country VARCHAR(255), timezone_offset VARCHAR(255),timezone_description VARCHAR(255), dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
    cursor.execute(query)

    cursor.close()
    connection.close()

