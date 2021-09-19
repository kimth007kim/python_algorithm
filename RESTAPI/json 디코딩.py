import json

user={
    "id":"gildong",
    "password":"192837",
    "age":30,
    "hobby":["football","programming"]
}

json_data=json.dumps(user)
print("json_data",json_data)

data=json.loads(json_data)
print("data",data)


for i in data:
    print(i)