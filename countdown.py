import time
x = int(input('Insert time(in second) : '))
y = input('Type "yes" to start : ')
if y == "yes":
    while x >= 0:
        print(x)
        x -=1
        time.sleep(0.2)
else:
    print("Okay")