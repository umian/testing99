import random

random.seed()

print("100 random numbers between 1 and 10")

for x in range(0,100):
    print(random.randint(1,10),end=" ")

print("")

for x in range(1,21):
    print("move",x, end="")

    myrandomnum = random.randint(1,5)

    if myrandomnum ==1:
        print(" - moving down",myrandomnum)
    else:
        print(" - staying still",myrandomnum)