import pickle

employees={"Bob":123,"Steve":324,"John":2303}

print(employees)

with open("employees.p","wb") as myfile:
        pickle.dump(employees,myfile)

with open("employees.p","rb") as myfile01:
    employees01=pickle.load(myfile01)
print(employees01)
