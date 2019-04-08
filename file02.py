import sys
# mydata = open("C:/Users/usman/Documents/myapp/testing99/test01/download.png", "rb").read(1024)

# for x in mydata:
#     print(x, end="")

if len(sys.argv)== 1:
    print("not arg given---",len(sys.argv))
    sys.exit
print("not arg given---",len(sys.argv))
print(sys.argv[0],sys.argv[1])
print("_______________________")

# with open("C:/Users/usman/Documents/myapp/testing99/test01/download.png", "rb") as mydata02:
with open(sys.argv[1], "rb") as mydata02:
    byte = mydata02.read(1024)
    while byte != b"":
        print(byte,end="")
        byte = mydata02.read(1)
