import requests
import json

URL = 'http://localhost:9089/stu_create/'

data = {
    'name': 'rahul',
    'roll': 101,
    'city': 'delhi',
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)

python_data = r.json()
print(type(python_data))
print(python_data)
