import requests
import json

user={
    "id":"gildong",
    "password":"192837"
}

url= "http://www.naver.com"
response=requests.get(url)

print("status code:",response.status_code)
print(response.text)