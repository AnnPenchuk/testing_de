from src.Loading.connection import connection


#def create():
 #   cursor = connection.cursor()
 #   name='registration_data3'
 #   columns='email VARCHAR(255),username VARCHAR(255), password VARCHAR(255),password_md5 VARCHAR(255),password_validation VARCHAR(255)'
 #   query = f'''
 #   CREATE TABLE IF NOT EXISTS {name} (
 #        user_id serial PRIMARY KEY, {columns}, dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  #  )'''.format(name,columns)
  #  cursor.execute(query)
  #cursor.close()
  #connection.close()



def insert(name,columns,values):
     cursor = connection.cursor()
     query = f'''INSERT INTO {name} ({columns}) VALUES {values}'''
     print(query)
     cursor.execute(query, values)
     cursor.close()
     connection.close()


def select(name):
    cursor = connection.cursor()
    query = f'''
    SELECT * FROM {name} '''
    cursor.execute(query)
    res = cursor.fetchall()
    for i in res:
        print(i)
    cursor.close()
    connection.close()


def delete(name,condition):
    cursor = connection.cursor()
    query = f'''
    DELETE FROM {name} 
         WHERE {condition}'''
    cursor.execute(query)
    cursor.close()
    connection.close()


def update(new,name,columns,condition):
    new_values=new[0]['email']
    cursor = connection.cursor()
    query = f'''
    UPDATE {name} 
    SET {columns}='{new_values}'
    WHERE {condition}'''
    cursor.execute(query)
    cursor.close()
    connection.close()