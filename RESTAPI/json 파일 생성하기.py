import json

user={
    "id":"gildong",
    "password":"192837",
    "age":30,
    "hobby":["football","programming"]

}

with open("user json", "w", encoding="utf-8") as file:
    json.dump(user,file,indent=4)