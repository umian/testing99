employees={"Bobe":1234,"Moke":6589,"Usman":9999}
print(employees)
if ("Bob" in employees):
    print("BOB found")

print(employees["Moke"])
print("__________________________________________")
def my_func():
    return (50,900),(25,55)

x,y = my_func()
print(x[1])
print(y[0])

for name, number in employees.items():
    print(name, number)