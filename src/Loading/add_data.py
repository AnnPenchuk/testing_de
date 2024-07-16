from src.Loading.crud_data import insert,select,delete,update
from src.Loading.connection import connection
from src.Loading.database_creation import database_creation

def add_data(i):
    database_creation(connection)
    name = 'users2'
    columns = 'gender,name_title, name_first,name_last,age,nat'
    values = (i['gender'], i['name_title'], i['name_first'], i['name_last'], i['age'], i['nat'])
    foreign_key = 'user_id'
    number=insert(connection,name, columns, values,foreign_key)


    name = 'registration_data2'
    columns = 'user_id, email,username, password, password_md5,password_validation'
    values =(number, i['email'], i['username'], i['password'], i['password_md5'], i['password_validation'])
    insert(connection,name, columns, values,foreign_key)

    name = 'media_data2'
    columns = 'user_id, picture'
    values = (number, i['picture'])
    insert(connection,name, columns, values,foreign_key)

    name = 'contact_details2'
    columns = 'user_id, phone, cell'
    values = (number, i['phone'], i['cell'])
    insert(connection,name, columns, values,foreign_key)

    name = 'locations2'
    columns = 'user_id, street_name,street_number,postcode,latitude,longitude'
    values = (number,i['street_name'], i['street_number'], i['postcode'], i['latitude'], i['longitude'])
    foreign_key = 'city_id'
    number=insert(connection,name, columns, values,foreign_key)

    name = 'cities2'
    columns = 'city_id,city,state,country,timezone_offset,timezone_description'
    values = (number, i['city'],i['state'],i['country'],i['timezone_offset'],i['timezone_description'])
    insert(connection,name, columns, values,foreign_key)