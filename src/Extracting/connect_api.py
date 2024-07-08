import requests

def api_request():
    quantity='5'
    url = "https://randomuser.me/api/?results="
    url = "".join([url, quantity])
    response = requests.get(url)
    res = response.json()
    return res



