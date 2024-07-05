from API.api import api_request
from Validation.valid import Users_valid, list_users
from src.Database.data import create,insert,select,delete,update



if __name__ == "__main__":
    res=api_request()
    res2=list_users(res)
    update(res)



