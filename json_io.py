import json

employees={"Bob":123,"Steve":324,"John":2303,"usman":984534}

print(employees)

with open("employees.json","w") as myfile:
    json.dump(employees,myfile)

with open("employees.json","r") as myfile01:
    employee02=json.load(myfile01)

print(employee02)

print(employee02["Bob"])