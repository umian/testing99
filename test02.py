def say_hellow(name = "unkown"):
    print("say hello", name)

def count_down():
    for a in range(1,10,1):
        print("count",a)


myname = input("Enter you name:")
say_hellow()
count_down()

code=""

while code != "exit":
    code = input("enter a command:")
    exec(code)

for z in range(32,1000):
    print(chr(z), end="")
    