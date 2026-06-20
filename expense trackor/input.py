import view,main,remove
while True:
    print("1.Add Expense"
          "\n2.View Expense"
          "\n3.Exit"
          "\n4.Total Expense"
          "\n5.Most_Used_Category"
          "\n6.Remove"
          "\n7.Edit list")
    try:
        user=int(input("enter the choice in number : "))
    except ValueError:
        print("invalid")
    else:
        if user==3:
            print("Thanks For Coming")
            break
        elif user==1:
            main.asking()
        elif user==2:
            view.view()
        elif user==4:
            view.total_expense()
        elif user==5:
            view.most_used_category()
        elif user==6:
            remove.remove()
        elif user==7:
            remove.edit()
        else:
            print("enter number between 1-7")