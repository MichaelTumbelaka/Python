import random

def dadu():
    while True:
        print("DICE ROLL SIMULATOR")
        print("-------------------")
        x = input("Wanna roll?(y/n) ")
        if x == "y":
            z = random.randint(1, 6)
            print(f'You gave rolled : {z}')
        else:
            print("Bye")
            break
dadu()