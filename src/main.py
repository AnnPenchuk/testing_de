from Extracting.parsing import receiving_data
from Validation.valid import Users_valid, list_users
from src.Extracting import connect_api
from src.Extracting.connect_api import api_request
from src.Loading.crud_data import insert,select,delete,update
from src.Loading.database_creation import database_creation
from src.Loading.connection import connection

if __name__ == "__main__":
    new=receiving_data()
    #res2=list_users(res)
    #database_creation()
    name = 'registration_data2'
    columns = 'email,username, password,password_md5,password_validation'
    values = ('aynz.khrymy@example.com', 'username', 'password', 'password_md5', 'password_validation')
    #insert(name, columns, values)
    name = 'registration_data2'
    columns = 'email'
    condition = 'user_id =1'
    print(new)
    #update(new,name,columns,condition)

