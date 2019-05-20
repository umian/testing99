class Vehicle:
    def __init__(self,x,y):
        self.x_pos=x
        self.y_pos=y
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        print("moving....")
        self.x_pos+=self.x_speed
        self.y_pos+=self.y_speed

    def render(self):
        print("Drivining....")

class Digger(Vehicle):
    def __init__(self,x,y):
        Vehicle.__init__(self,x,y)
    def dig(self):
        print("digging......")

class Helicopter(Vehicle):
    def __init__(self,x,y,height):
        Vehicle.__init__(self,x,y)
        self.z_pos=height


car=Vehicle(10,20)
car.update()
car.render()

digger = Digger(50,90)
digger.update()
digger.dig()
digger.update

chopper =Helicopter(1,2,3)
chopper.update
print(chopper.z_pos)

