import requests
import json
import hashlib
from sys import argv

list_emails = ['eehzntm5@hotmail.com',
               'manuruel@yahoo.com',
               'russellebb912@hotmail.com',
               'jnkitchener@btinternet.com',
               'ras-nie@web.de',
               'ghagen4@gmail.com',
               'mattdhoey@gmail.com'
               ]


def get_profile_data_json(query):
    base_url = 'https://ru.gravatar.com/'
    hash_email = hashlib.md5(query.encode())

    response = requests.get(f'{base_url}{hash_email.hexdigest()}.json')

    if response.status_code != 200:
        return json.dumps({"result": "There is no connection to the server"})

    data = response.json()['entry'][0]

    data['email_hash'] = data.pop('hash')
    data['url'] = data.pop('profileUrl')
    data['alias'] = data.pop('preferredUsername')
    data['thumb'] = data.pop('thumbnailUrl')

    if data.get('currentLocation') is not None:
        data['location'] = data.pop('currentLocation')

    if type(data['name']) is dict:
        data['name']['person'] = data['name'].pop('formatted')
    elif type(data['name']) is list and len(data['name']) > 0:
        data['name'][0]['person'] = data['name'][0].pop('formatted')

    return json.dumps({'result': data})


if __name__ == '__main__':

    query = argv[1]
    result = get_profile_data_json(query)
    print(result)
