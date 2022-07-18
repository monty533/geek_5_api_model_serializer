import requests
import json

URL = 'http://localhost:9089/stu_api/'

# for get the data or read the data


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data(1)

# for post the data or inserting or create the data


def post_data():
    data = {
        'roll': 103,
        'name': 'nitin kumar',
        'city': 'delhi'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print('recieve_data', data)


post_data()


def update_data():
    data = {
        'id': 1,
        'name': 'john',
        'city': 'pepsi',
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


# update_data()


def delete_data():
    data = {
        'id': 3
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


# delete_data()
