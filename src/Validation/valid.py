import logging

from pydantic import BaseModel, EmailStr, Field
import re


def password_valid(password: str) -> str:
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    password_validation = 'YES'

    if re.match(pattern, password) is None:
        password_validation = 'NO'

    return password_validation


class UsersValid(BaseModel):
    email: EmailStr
    password: str
    gender: str
    name_title: str
    name_first: str
    name_last: str = Field(max_lenght=50)
    street_number: int
    street_name: str = Field(max_lenght=50)
    city: str = Field(max_lenght=90)
    state: str = Field(max_lenght=90)
    country: str = Field(max_lenght=90)
    postcode: str = Field(max_lenght=20)
    latitude: str = Field(max_lenght=20)
    longitude: str = Field(max_lenght=20)
    username: str = Field(max_lenght=70)
    age: int
    phone: str
    cell: str = Field(max_lenght=30)
    nat: str = Field(max_lenght=60)
    picture: str
    password_md5: str
    timezone_offset: str = Field(max_lenght=10)
    timezone_description: str = Field(max_lenght=60)


def list_users(res):
    list_valid = []
    try:
        for i in res:
            valid = UsersValid(
                email=i['email'],
                password=i['password'],
                gender=i['gender'],
                name_title=i['name_title'],
                name_first=i['name_first'],
                name_last=i['name_last'],
                street_number=i['street_number'],
                street_name=i['street_name'],
                city=i['city'],
                state=i['state'],
                country=i['country'],
                postcode=i['postcode'],
                latitude=i['latitude'],
                longitude=i['longitude'],
                username=i['username'],
                age=i['age'],
                phone=i['phone'],
                cell=i['cell'],
                nat=i['nat'],
                picture=i['picture'],
                password_md5=i['password_md5'],
                timezone_offset=i['timezone_offset'],
                timezone_description=i['timezone_description'])
            password_validation=password_valid(i['password'])
            dict = {'email': valid.email, 'password': valid.password, 'password_validation':password_validation, 'gender': valid.gender,
                    'name_title': valid.name_title,
                    'name_first': valid.name_first, 'name_last': valid.name_last, 'street_number': valid.street_number,
                    'street_name': valid.street_name, 'city': valid.city, 'state': valid.state, 'country': valid.country,
                    'postcode': valid.postcode, 'latitude': valid.latitude, 'longitude': valid.longitude,
                    'username': valid.username, 'age': valid.age,
                    'phone': valid.phone, 'cell': valid.cell,
                    'nat': valid.nat, 'password_md5': valid.password_md5, 'timezone_offset': valid.timezone_offset,
                    'timezone_description': valid.timezone_description, 'picture': valid.picture}
            list_valid.append(dict)
        return list_valid
    except:
        print('Не удалось проверить правильность полученных данных')
        logging.error("функция проверки валидности не сработала")
