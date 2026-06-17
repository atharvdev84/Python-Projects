import json,save
def view():
    with open(r"F:\Coding\To-Do list\To-Do_data.json","r") as f:#Use your own data.json path
        data=json.load(f)
        for i,task in enumerate(data,start=1):
            print(f"{i}.",task)

def add():
    """Allow user to add their task"""
    add=input("enter the task you wanna add : ").lower()
    status="Pending"
    info= {
        "Task" : add,
        "Status" : status
    }
    save.save_data(info)

def remove():
    "Allow user to remove their task if done"
    view()
    with open(r"F:\Coding\To-Do list\To-Do_data.json","r") as f:#Use your own data.json path
        data=json.load(f)
        if len(data)==0:
            print("Empty List")
            return
        try:
            remove=int(input("enter the task you wanna remove : "))
        except ValueError:
            print("index only")
        else:
            if len(data)==0:
                print("list is empty")
            elif remove<1 or remove>len(data):
                print("invalid")
            else:
                data.pop(remove-1)
                save.save_data2(data)

def edit():
    with open(r"F:\Coding\To-Do list\To-Do_data.json","r") as f:#Use your own data.json path
        data=json.load(f)
        if len(data)==0:
            print("Empty List")
            return
        view()
        try:
            user=int(input("enter the number which you wanna change : "))
        except ValueError:
            print("Invalid")
        else:
            if user<1 or user>len(data):
                print("Select number from Menu")
            else:
                new_data=data[user-1]
                new_value=input("Enter what new task you want : ")
                new_data["Task"]=new_value
                save.save_data2(data)

def status():
    with open(r"F:\Coding\To-Do list\To-Do_data.json","r") as f:#Use your own data.json path
        data=json.load(f)
        view()
        try:
            user=int(input("enter which task is completed : "))
        except ValueError:
            print("Invalid")
        else:
            if user<1 or user>len(data):
                print("Select number from Menu")
            else:
                new_data=data[user-1]
                new_data["Status"]="Done"
                save.save_data2(data)

def filter():
     print("""
          Main Menu
    1.Done Task
    2.Pending Task 
    3.All Task
        """)
     
     with open(r"F:\Coding\To-Do list\To-Do_data.json","r") as f: #Use your own data.json path
        data=json.load(f)
        try:
            user=int(input("enter the choice : "))
        except ValueError:
            print("Invalid")
        else:
            if user<1 or user>len(data):
                print("Select number from Menu")
            else:
                for i in data:
                    if user==1:
                        if i["Status"]=="Done":
                            print(i)
                    elif user==2:
                        if i["Status"]!="Done":
                            print(i)   