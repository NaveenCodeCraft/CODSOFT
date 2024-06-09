
import random
import string

def gen_password(length):
    char=string.digits+string.ascii_letters
    password=''.join(random.choice(char) for i in range(length))    
    print("\nThe Generater password is : ",password)
        

length=int(input("Enter the length of tha password :"))
ch='y'
while ch=='y':
    if length<=0:
        print("Enter positive length")
    else:
        gen_password(length)
        ch=input("you want to generate again(y/n):")
        break

