import json

string='{"id":765, "email":"ivanov@mail.ru","surname":"Иванов","age":45,"friends":[123,456,789]}'
data = json.loads(string)

print(data["id"])
print(data["email"])

with open('data.json','w',encoding='UTF-8') as file:
    json.dump(data,file)