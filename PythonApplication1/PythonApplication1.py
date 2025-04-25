import requests
import random

random_id = random.randint(1, 100)

url = f'https://jsonplaceholder.typicode.com/posts/{random_id}'

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    print("ID:", data['id'])
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print("Error :", response.status_code)

