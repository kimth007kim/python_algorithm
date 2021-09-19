import requests

target = "https://jsonplaceholder.typicode.com/users"
response= requests.get(url=target)

data= response.json()

print(data )