import main
while True:
    print("""
          Main Menu
    1.Add task
    2.Remove task 
    3.View task
    4.Edit task
    5.Wanna Change status of 
    6.View Pending And Done Task
    7.Exit
        """)

    try:
        user=int(input("enter the number of the task : "))
    except ValueError:
        print("invalid")
    else:
        if user==1:
            main.add()
        elif user==2:
            main.remove()
        elif user==3:
            main.view()
        elif user==4:
            main.edit()
        elif user==5:
            main.status()
        elif user==6:
            main.filter()
        elif user==7:
            print("Thanks for Coming")
            break
        else:
            print("Select number from Menu")