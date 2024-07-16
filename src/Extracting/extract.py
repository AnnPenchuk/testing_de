import json
from src.Extracting.connect_api import api_request
from src.Extracting.parsing import receiving_data


def extract(q: int) -> json:
    api_r = api_request(quantity=q).get('results')
    r_data = receiving_data(api_r)
    return r_data
