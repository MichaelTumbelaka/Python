import random

while True:
    x = input("Rock, Paper, Scissor? ")
    y = random.randint(0, 2)
    list1 = ["Rock", "Paper", "Scissor"]
    pilihan = list1[y]
    if y == 0:
        if x == "Rock":
            print("Its a tie")
        elif x == "Scissor":
            print("You lose")
        elif x == "Paper":
            print("You win")
            break
    elif y == 1:
        if x == "Rock":
            print("You lose")
        elif x == "Paper":
            print("Its a tie") 
        elif x == "Scissor":
            print("You win")
            break
    elif y == 2:
        if x == "Paper":
            print("You lose")
        elif x == "Scissor":
            print("Its a tie")
        elif x == "Rock":
            print("You win")
            break
    
    

    
        
    