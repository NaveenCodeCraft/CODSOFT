def add(a,b):
    c=a+b
    print("\nResult(",a,"+",b,"):",c)
def sub(a,b):
    c=a-b
    print("\nResult(",a,"-",b,"):",c)
def mul(a,b):
    c=a*b
    print("\nResult(",a,"*",b,")",c)
def div(a,b):
    c=a/b
    print("\nResult(",a,"/",b,"):",c)

print("SIMPLE CALCULATOR")
print("The available operations are ...")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4,Division")
while True:
    num1=float(input("\nEnter the first number : "))
    num2=float(input("Enter the second number : "))
    choice=input("Enter your operation: ")
    if(choice=='1'):
        add(num1,num2)
    elif(choice=='2'):
        sub(num1,num2)
    elif(choice=='3'):
        mul(num1,num2)
    elif(choice=='4'):
        div(num1,num2)
    else:
        print("Invalid operation")
    
