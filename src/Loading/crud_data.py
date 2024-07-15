from src.Loading.connection import connection


def insert(connection,name,columns,values,foreign_key):
    with connection().cursor() as cursor:
        query = f'''INSERT INTO {name} ({columns}) VALUES {values} RETURNING {foreign_key}'''
        cursor.execute(query,values)
        print("данные добавлены в таблицу ",name)
        res_id = cursor.fetchall()[0][0]
        return res_id



def select(name):
    with connection().cursor() as cursor:
        query = f'''
        SELECT * FROM {name} '''
        cursor.execute(query)
        res = cursor.fetchall()
        for i in res:
            print(i)



def delete(name,condition):
    with connection().cursor() as cursor:
        query = f'''
        DELETE FROM {name} 
             WHERE {condition}'''
        cursor.execute(query)


def update(new,name,columns,condition):
    new_values=new[0]['email']
    with connection().cursor() as cursor:
        query = f'''
        UPDATE {name} 
        SET {columns}='{new_values}'
        WHERE {condition}'''
        cursor.execute(query)
