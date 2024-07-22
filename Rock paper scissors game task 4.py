print("############################# WELCOME TO ROCK PAPER SCISSOR GAME ###################################")
import random
ccount = 0
ucount = 0
def User_Option():
    uchoice = input("Choose Rock,Paper or Scissor: ")
    if uchoice in ["Rock", "rock", "r", "R"]:
        uchoice = "r"
    elif uchoice in ["Paper", "paper", "p", "P"]:
        uchoice = "p"
    elif uchoice in ["Scissor", "scissor", "s", "S"]:
        uhoice = "s"
    else:
        print("Try again!!")
        User_Option()
    return uchoice
def Computer_Option():
    Cchoice = random.randint(1, 3)
    if Cchoice == 1:
        Cchoice = "r"
    elif Cchoice == 2:
        Cchoice = "p"
    else:
        Cchoice = "s"
    return Cchoice
while True:
    print("")
    uchoice = User_Option()
    Cchoice = Computer_Option()
    print("")
    
    if uchoice == "r":
        if Cchoice == "r":
            print("Both chose Rock. Match Tie !! ")
        
        elif Cchoice == "p":
            print("You chose rock.The computer chose paper.Computer Won !!")
            ccount+= 1
            
        elif Cchoice == "s":
            print("You chose rock. The computer chose scissor. You Won !!")
            ucount += 1

    elif uchoice == "p":
        if Cchoice == "r":
            print("You chose paper. The computer chose rock. You Won !!")
            ucount += 1
        
        elif Cchoice == "p":
            print("You chose paper. The computer chose paper. Match Tie !! ")
            
            
        elif Cchoice == "s":
            print("You chose paper. The computer chose scissor. Computer Won !!")
            ccount += 1

    elif uchoice == "s":
        if Cchoice == "r":
            print("You chose scissor. The computer chose rock. Computer Won !!")
            ccount += 1
        
        elif Cchoice == "p":
            print("You chose scissor. The computer chose paper. You Won !!")
            ucount += 1
            
        elif Cchoice == "s":
            print("You chose scissor. The computer chose scissor. Match Tie !! ")

    print("Player wins: " + str(ucount))
    print("Computer wins: " + str(ccount))
    uchoice = input("Do you want to play again? (y/n)")
    if uchoice in ["Y", "y", "yes", "Yes"]:
        pass
    elif uchoice in ["N", "n", "no", "No"]:
        break
    else:
        break
             

