class Myclass(object):
    __slots__ =("number","name")
    def __init__(self,passed_number):
        self.number=passed_number

x=Myclass(100)
print(x.number)

x.name ="hellow world"

print(x.name)

x.text ="test"