#import random module for random option generation
import random

options=['rock','paper','scissor']
print("\t\tROCK-PAPER-SCISSORS")

#value assignment
ch='y'
User_point=0
Bot_point=0

while(ch=='y'):
    user=input("\nEnter your option (ROCK-PAPER-SCISSORS) :")
    bot=random.choice(options)
    print("user :",user,"--  bot :",bot)
    if user=='rock':
        if bot=='rock':
            print("match draw")
        elif bot=='paper':
            print("Bot Won ")
            Bot_point=Bot_point+1
        elif bot=='scissor':
            print("User Won ")
            User_point=User_point+1
    elif user=='paper':
        if bot=='paper':
            print("match draw")
        elif bot=='scissor':
            print("Bot Won")
            Bot_point=Bot_point+1
        elif bot=='rock':
            print("User Won")
            User_point=User_point+1
    elif user=='scissor':
        if bot=='scissor':
            print("match draw")
        elif bot=='rock':
            print("Bot Won")
            Bot_point=Bot_point+1
        elif bot=='paper':
            print("User Won")
            User_point=User_point+1
    ch=input("are you want play again (y/n) :")
#display the score
print("\n\t\tUser_Scored: ", User_point)
print("\t\tBot_Scored : ", Bot_point)
print("\n\t\tThanks for playing")
