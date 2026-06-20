import save,datetime
def ask(money:int,field:str,yy:int,mm:int,dd:int):
    """take input and return date to list """
    print(f"your total amount is rupees {money:,}")
    print(f"you spend your {money:,} rupees on {field}")
    date=datetime.date(yy,mm,dd)
    return {
        "amount":money,
        "category":field,
        "date":f"{date:%y,%m,%d}"
    }

def asking():
    try:
        amount:int=int(input("enter the amount of money you spend : "))
        category:str=input("enter where you spend the money : ")
        year:int=int(input("which year : "))
        month:int=int(input("which month : "))
        day:int=int(input("which day : "))
    except ValueError:
        print("invalid")
        return 
    else:
        user_data=ask(amount,category,year,month,day)
        save.save_data(user_data)
        return user_data
