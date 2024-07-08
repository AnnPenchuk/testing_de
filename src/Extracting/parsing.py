import requests
from src.Extracting.connect_api import api_request
def receiving_data():
    users=[]
    res=api_request().get('results')
    for x in res:
        email=x.get('email')
        password=x.get('login').get('password')
        dict = {'email':email, 'password':password}
        users.append(dict)

    print(users)

    return users


