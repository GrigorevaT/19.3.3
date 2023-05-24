import requests
import json

base_url = "https://petstore.swagger.io"
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# POST

data_post = {
    "id": 0,
    "username": "tamarap",
    "firstName": "tamara",
    "lastName": "petrova",
    "email": "tp@mail.ru",
    "password": "123456",
    "phone": "81234567890",
    "userStatus": 0
}

response_post = requests.post(f'{base_url}/v2/user', headers=headers, json=data_post)
data_post = json.dumps(data_post)

print('Создаем нового пользователя:')
print(response_post.status_code)
print(response_post.json())

# GET

response_get = requests.get(f'{base_url}/v2/user/tamarap', headers=headers)

print('Получаем пользователя по username:')
print(response_get.status_code)
print(response_get.json())

# PUT
data_user = response_get.json()
user_id = data_user["id"]
data_put = {
    "id": f'{user_id}',
    "username": "tamarap",
    "firstName": "tamara",
    "lastName": "ivanova",
    "email": "tp@mail.ru",
    "password": "123456",
    "phone": "81234567890",
    "userStatus": 0
}

response_put = requests.put(f'{base_url}/v2/user/tamarap', headers=headers, json=data_put)
data_put = json.dumps(data_put)

print('Меняем данные пользователя:')
print(response_put.status_code)
print(response_put.json())

# GET

response_get_new = requests.get(f'{base_url}/v2/user/tamarap', headers=headers)

print('Получаем измененные данные пользователя:')
print(response_get_new.status_code)
print(response_get_new.json())

# DELETE

response_del = requests.delete(f'{base_url}/v2/user/tamarap', headers=headers)

print('Удаляем пользователя:')
print(response_del.status_code)
print(response_del.json())
