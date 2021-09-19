import json

user = {
    "id":"gildong",
    "password":"192837",
    "age":30,
    "hobby":["football","programming"]
}

json_data=json.dumps(user,indent=4)
print(json_data)