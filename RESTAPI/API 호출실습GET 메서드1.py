import requests
import json

target="https://jsonplaceholder.typicode.com/users/1"
response= requests.get(url=target)
user= response.text
print(user)


userdata= json.loads(user)
print(userdata)
for i in userdata:
    print(i,userdata[i])