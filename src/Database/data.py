import psycopg2

connection = psycopg2.connect(
        host="127.0.0.1",
        user="admin",
        password="password",
        database="de_projects",
        port = "6432"
    )
connection.autocommit=True


def create():
    cursor = connection.cursor()
    name='registration_data'
    columns='email VARCHAR(255),username VARCHAR(255), password VARCHAR(255),password_md5 VARCHAR(255),password_validation VARCHAR(255)'
    query = f'''
    CREATE TABLE IF NOT EXISTS {name} (
         user_id serial PRIMARY KEY, {columns}, dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )'''.format(name,columns)
    cursor.execute(query)
    cursor.close()
    connection.close()


def insert():
    cursor = connection.cursor()
    name='registration_data'
    columns='email,username, password,password_md5,password_validation'
    values='aynz.khrymy@example.com', 'username', 'password','password_md5','password_validation'
    query = f'''
    INSERT INTO {name} ({columns})
     VALUES {values}'''.format(name,columns,values)
    print(query)
    cursor.execute(query)
    cursor.close()
    connection.close()


def select():
    cursor = connection.cursor()
    name='registration_data'
    query = f'''
    SELECT * FROM {name} '''.format(name)
    cursor.execute(query)
    res = cursor.fetchall()
    print(res)
    cursor.close()
    connection.close()


def delete():
    cursor = connection.cursor()
    name='registration_data'
    condition='user_id=2'
    query = f'''
    DELETE FROM {name} 
         WHERE {condition}'''.format(name,condition)
    cursor.execute(query)
    cursor.close()
    connection.close()


def update(new):
    a=new[0]['email']
    cursor = connection.cursor()
    name='registration_data'
    columns='email'
    condition = 'username=username'
    new_values=a
    query = f'''
    UPDATE {name} 
    SET {columns}='{new_values}'
    WHERE {condition}'''.format(name,columns,new_values,condition)
    cursor.execute(query)
    cursor.close()
    connection.close()