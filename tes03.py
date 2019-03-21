days = ("Monday","Tuesday","Wednesday","Thursday")
x= int(input("enter a day number:"))

print(days[x-1])

for a in days[:2]:
    print(a)

for a in days[::2]:
    print(a)

# days[0] = "Usman"

mytext = "the quick brown fox jumped over the lazy dog"

mylist=[12,20,30,40,50,1,5,100,20]
mylist.sort(reverse=True)
for counter,b in enumerate(mylist):
    print(b,counter)

for q in range(500,600,5):
    print(q)
    mylist.append(q)

for counter,b in enumerate(mylist):
    print(b,counter)   

print("______________________________________________")
print (mylist.count(20))