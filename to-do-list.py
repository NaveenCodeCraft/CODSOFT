print("TO-DO-LIST")
list=[]
while True:
    print("\nThe available options are")
    print("1.Add task\n2.Delete task\n3.View task\n4.Exit")
    ch=input("Enter your choice(1 to 4):")
    if ch=='1':
        task=input("Enter the task to add:")
        list.append(task)
    elif ch=='2':
        rem=input("Enter the task to remove:")
        if rem in list:
            list.remove(rem)
        else:
            print("\nTask not found in the list")
    elif ch=='3':
        if list:
            print("\nYour To-Do-List is:")
            print(list)
        else:
            print("your to-do-list is empty")
    elif ch=='4':
        print("\nExiting.... ")
        break
    else:
        print("\nIvalid choice")
