

def receiving_data(res):
    users = []
    for x in res:
        email = x.get('email')
        gender = x.get('gender')
        name_title = x.get('name').get('title')
        name_first = x.get('name').get('first')
        name_last = x.get('name').get('last')
        street_number = x.get('location').get('street').get('number')
        street_name = x.get('location').get('street').get('name')
        city = x.get('city', 'NULL')
        state = x.get('state', 'NULL')
        country = x.get('country', 'NULL')
        postcode = x.get('postcode', 'NULL')
        latitude = x.get('coordinates', 'NULL')
        longitude = x.get('coordinates', 'NULL')
        username = x.get('login').get('username')
        age = x.get('dob').get('age')
        phone = x.get('phone')
        cell = x.get('cell')
        nat = x.get('nat')
        picture = x.get('picture').get('thumbnail')
        password = x.get('login').get('password')
        password_md5 = x.get('md5', 'NULL')
        timezone_offset = x.get('location').get('timezone').get('offset')
        timezone_description = x.get('location').get('timezone').get('description')
        dict = {'email': email, 'password': password, 'gender': gender, 'name_title': name_title,
                'name_first': name_first, 'name_last': name_last, 'street_number': street_number,
                'street_name': street_name, 'city': city, 'state': state, 'country': country,
                'postcode': postcode, 'latitude': latitude, 'longitude': longitude, 'username': username, 'age': age,
                'phone': phone, 'cell': cell,
                'nat': nat, 'password_md5': password_md5, 'timezone_offset': timezone_offset,
                'timezone_description': timezone_description, 'picture': picture}
        users.append(dict)

    return users
