import sys, os, time

print("clearing screen")
if sys.platform.startswith("win"):
    os.system("cls")
else:
    os.system("clear")
print("done")

width, heigth = os.get_terminal_size()

print("running on ",sys.platform)
print("python version", end="")
print(sys.version_info)
# print(sys.modules)
print(os.get_terminal_size())
print("lenght: ",width)
print("height: ",heigth)

for x in range(1,11):
    print(x, time.strftime("%H:%M:%S"))
    time.sleep(.5)