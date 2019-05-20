class Mycalss:
    def __init__(self,num_passed):
        self.num=num_passed
    
    @property
    def num(self):
        print("getting number.....")
        return self.__num
    @num.setter
    def num(self,num_passed):
        print("setting number...")
        if num_passed>1000:
            print("rounded to 10000")
            self.__num =1000
        else:
            self.__num =num_passed

x=Mycalss(1230)
print("------")
print(x.num)
x.num=9000
print("------")
print(x.num)