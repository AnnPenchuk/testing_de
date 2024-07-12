from src.Loading.crud_data import insert,select,delete,update
from src.Loading.connection import connection

def add_data(i):
    name = 'users3'
    columns = 'gender,name_title, name_first,name_last,age,nat'
    values = (i['gender'], i['name_title'], i['name_first'], i['name_last'], i['age'], i['nat'])
    try:
        insert(connection,name, columns, values)
    except:
        print('Ну удалось добавить данные в таблицу ',name)

    name = 'registration_data3'
    columns = 'user_id, email,username, password, password_md5,password_validation'
    foreign_key='user_id'
    foreign_key_tab='de_projects.public.users3'
    cursor = connection.cursor()
    query = f'''(SELECT max({foreign_key}) FROM {foreign_key_tab})'''
    cursor.execute(query)
    number=cursor.fetchall()[0][0]
    values =(number, i['email'], i['username'], i['password'], i['password_md5'], 'password_validation')
    try:
        insert(connection,name, columns, values)
    except:
        print('Ну удалось добавить данные в таблицу ',name)

    name = 'media_data3'
    columns = 'user_id, picture'
    values = (number, i['picture'])
    try:
        insert(connection,name, columns, values)
    except:
        print('Ну удалось добавить данные в таблицу ',name)

    name = 'contact_details3'
    columns = 'user_id, phone, cell'
    values = (number, i['phone'], i['cell'])
    try:
        insert(connection,name, columns, values)
    except:
        print('Ну удалось добавить данные в таблицу ', name)

    name = 'locations3'
    columns = 'user_id, street_name,street_number,postcode,latitude,longitude'
    values = (number,i['street_name'], i['street_number'], i['postcode'], i['latitude'], i['longitude'])
    try:
        insert(connection,name, columns, values)
    except:
        print('Ну удалось добавить данные в таблицу ', name)
        logging.error('Ну удалось добавить данные в таблицу ', name)

    name = 'cities3'
    columns = 'city_id,city,state,country,timezone_offset,timezone_description'
    foreign_key = 'city_id'
    foreign_key_tab = 'de_projects.public.locations3'
    cursor = connection.cursor()
    query = f'''(SELECT max({foreign_key}) FROM {foreign_key_tab})'''
    cursor.execute(query)
    number = cursor.fetchall()[0][0]
    values = (number, i['city'],i['state'],i['country'],i['timezone_offset'],i['timezone_description'])
    try:
        insert(connection,name, columns, values)
    except:
        print('Ну удалось добавить данные в таблицу ', name)
        logging.error('Ну удалось добавить данные в таблицу ', name)

    # name = 'registration_data2'
    # columns = 'email'
    # condition = 'user_id =1'
    # update(new,name,columns,condition)

