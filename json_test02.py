import json

with open("data.json","r") as myfile:
    mydata=json.load(myfile)

# print(mydata[0]["name"])

id_to_find =int(input("Enter an ID: "))

result = [myitem for myitem in mydata if myitem["id"] == id_to_find]

if len(result) >0:
    print("Name: ", result[0]["name"])
    print(result[0]["price"])
    for games in result[0]["games"]:
        print(games,end= "-")
else:
    print("not fount ID ",id_to_find)
