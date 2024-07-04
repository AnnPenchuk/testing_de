import requests

def api_request():
    users=[]
    quantity=input('Сколько пользователей Вы хотите получить?')
    url = "https://randomuser.me/api/?results="
    url = "".join([url, quantity])
    #print("url:", url)


    response = requests.get(url)

    res=response.json()
    for x in res['results']:
        email=x['email']
        password=x['login']['password']
        dict = {'email':email, 'password':password}
        #print('email=',email)
        #print('password=', password)
        users.append(dict)

    #print(users)

    return users


