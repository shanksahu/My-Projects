import random
randNo=random.randint(0,101)
#print(randNo)
user=None
i=1
print('''             
            Hello....! User Welcome to my Game
            I will genrate a number in between 0 to 100
            You need to guess which number i have been Genrated
            Let's see in how much attmpet you can guess it right

   ''')
while user!=randNo:
    user=int(input("Enter the number You Gussed: "))
    if user==randNo:
        print(f"Congurelation You Guess the right number at your {i} attempt")
        
    elif randNo>user>=(randNo-5):
        print("You are little bit closer, guess slighlty bigger")
    elif randNo<user<=(randNo+5):
        print("You are little bit Away, guess little bit smaller")  
    elif 0<=user<randNo:
        print("You need to guess higher number")
    elif 100>=user>randNo:
        print("You need to guess smaller number")
    else:
        print("Please Guess number in between 0 to 100")
    i=i+1
# with open("Hi.txt", 'r') as f:
#     p=int(f.read())
# if i<p:
#     with open("Hi.txt", "w") as f:
#         f.write(str(i-1))

e=input("press any key to exit")
    



