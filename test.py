usman = 10
print ("hellow world",usman)
usman01 = usman + 100
print(usman01)
username = input("Enter your name")
print(username)
a = int(input("a number a "))
b = int(input(" a number b "))
print ("the sum is ", a + b)

if username.lower() == "usman":
    print ("the name is usman")
    if username.upper() == "USMAN":
        print("name is usman second time")
while a <= 100:
    print(a)
    if a%2 ==0:
        print(a, "is s even number")
        break
    a+=1

mylist={1,10,100,500}
for a in mylist:
        print(a)

for a in range(0,10,2):
    print("--",a)