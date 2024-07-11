import requests

def api_request(n):
    quantity=n
    url = "https://randomuser.me/api/?results="
    url = "".join([url, quantity])
    response = requests.get(url)
    res = response.json()
    return res



