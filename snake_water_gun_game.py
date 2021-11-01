import random
import os

def game1(comp, you):
    if comp==you:
        return "it's a tie"
    if comp=="water":
        if you=="snake":
            return True
        elif you=="gun":
            return False
    elif comp=="gun":
        if you=="snake":
            return False
        elif you=="water":
            return True
    elif comp=="snake":
        if you=="gun":
            return True
        elif you=="water":
            return False
    else:
        return None

def game2(p1, p2):
   
    if p1=="water" and p2=="water" or p1=="snake" and p2=="snake" or p1=="gun" and p2=="gun":
        return "Its a tie"
    if p1=="water":
        if p2=="snake":
            return True
        elif p2=="gun":
            return False
    elif p1=="gun":
        if p2=="snake":
            return False
        elif p2=="water":
            return True
    elif p1=="snake":
        if p2=="gun":
            return True
        elif p2=="water":
            return False
    else:
        return None

while(True):
    print('''
      \t Welcome to Snake Water Gun game
                press 1 for play with computer
                press 2 for muliplayer
                Press 3 for Exit
            Game Hint:
                Snake can't survive in front of gun
                snake can drink water
                Gun will drown in water
    ''') 
    game=input("Enter your options: ")
    
    if game=="1":
        while(True):
            print("comp choosed Water, Snake, Gun")
            randNo = random.randint(1,3)
            if randNo==1:
                    comp="water"
            elif randNo==2:
                    comp="snake"
            elif randNo==3:
                    comp="gun"
            you=input("[Your turn: Water ,Snake, Gun] What you choose: ")
            you=you.lower()

            g1=game1(comp, you)
            enter="it's a tie"
            print(F"Comp choose: {comp}, You choose: {you}")
            if g1 is True:
                print("Congratultaions, You WON")
                break
            elif g1 is False:
                print("You Loose")
                break
            elif g1 is None:
                print("please enter valid options")
            else:
                print("It's a tie")
                break

    elif game=="2":
        while(True):
            p1=input("Player one turn: Snake, Water, Gun Choose your option: ")
            p1=p1.lower()
            os.system('cls')
            p2=input("Player two turn: Snake, Water, Gun Choose your option: ")
            p2=p2.lower()
            os.system('cls')
            g2=game2(p1, p2)
            print(F"Player one choose: {p1}, Player two choose: {p2}")
            if g2 is True:
                print("Player 2 WON")
                break
            elif g2 is False:
                print("Player 1 WON")
                break
            elif g2 is None:
                print("please entr valid options")
            else:
                print("It's a tie")
                break
    elif game=="3":
        exit()
    else:
        print("Please Enter Valid option")

    


