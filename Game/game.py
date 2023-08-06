import random
option=["Rock","Paper","Scissors"]

move=True

personCount=0

systemCount=0

TieCount=0


while move:
    computer=random.choice(option)
    user=input("Enter your Move :- ")

    if user not in option:
        print("Enter valid Move ")
    else:
         if user==computer:
                print(f"Computer choice:- {computer}")
                print("Game Tie")
                TieCount+=1
                
         elif user=="Rock" and computer=="Scissors ":
               print(f"Computer choice:- {computer}")
               print("You won")
               personCount+=1


         elif user=="Paper" and computer=="Rock":
               print(f"Computer choice:- {computer}")
               print("You won")
               personCount+=1      
              


         elif user=="Scissors " and computer=="Paper":
               print(f"Computer choice:- {computer}")
               print("You won")
               personCount+=1  


         else:
             print(f"Computer choice:- {computer}")
             print("You Loose")
             systemCount+=1 



         print(f"User-Points:- {personCount} Computer-Points:- {systemCount} Game-Tie-Count:-{TieCount}") 


         exit=input("Do you want to Quit Enter (Yes/No) :- ") 


         if(exit=="Yes" or exit=="yes" ) :
              move=False