text_list = open("data.txt","r").readlines()

for counter,line in enumerate(text_list):
    loc =line.find("kiss")
    if loc !=-1:
        print("fount on line:",counter+1 ,"Position ",loc)

