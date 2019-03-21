try:
    with open("c:/users/usman/desktop/test_file_pv.txt","a") as myfile:
        file_lenght= myfile.write("hellow worlk\n")
        myfile.close()
        print(file_lenght)
except OSError as err:
    print(err)

myfile02 = open("c:/users/usman/desktop/test_file_pv.txt","r")
for text in myfile02:
    print(text,end="")

myfile02.close

text_data=open("c:/users/usman/desktop/test_file_pv.txt","r").read()
print(text_data)

employees={}
myfile03 = open("data.csv","r").readlines()
for line in myfile03:
    raw_emp=line.split(",")
    employees[raw_emp[0]]=int(raw_emp[1].rstrip())
    print(employees)
print("-------------------")
