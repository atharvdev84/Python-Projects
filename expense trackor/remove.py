import view,json,save

def remove():
    """Allow to remove the item from the save data"""
    view.view()
    with open("F:\Coding\expense trackor\data.json","r") as f:
        data=json.load(f)
    try:
        user=int(input("enter the number of the list you wanna remove  : "))
    except ValueError:
        print("invalid")
    else:
        if not data:
            print("list is empty")
            return    
        else:
            data.pop(user-1)
            new_data=data
            save.save_data2(new_data)
            
def edit():
    """This function allow us to edit our list"""
    with open("F:\Coding\expense trackor\data.json","r") as f:
        read=f.read()
        data=json.loads(read)
        try:
            view.view()
            index=int(input("enter the number of th list which you wanna edit : "))
            if index<1 or index>len(data):
                print("invalid index")
                return
            
        except ValueError:
            print("invalid")
        else:
            print("1.Amount" \
                  "\n2.Category" \
                    "\n3.Date")
            
            user=input("enter the number or name that you wanna edit : ").lower()
            if user=="1" or user=="amount":
                try:
                    change_amount=int(input("enter new amount : ")) 
                except ValueError:
                    print("Invalid")
                else:
                    data[index-1]["amount"]=change_amount

            elif user=="2" or user=="category":
                change_category=input("enter new category : ")
                data[index-1]["category"]=change_category

            elif user=="3" or user=="date":
                try:
                    year:int=int(input("which year : "))
                    month:int=int(input("which month : "))
                    day:int=int(input("which day : "))
                except ValueError:
                    print("invalid")
                    return 
                else:
                    data[index-1]["date"]=f"{year}-{month}-{day}"
    save.save_data2(data)