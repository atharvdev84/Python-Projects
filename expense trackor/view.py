import json
def view():
    """we can see our all task from here"""
    with open("F:\Coding\expense trackor\data.json","r") as f:
        read=f.read()
        lis_file=json.loads(read)
        for i,item in enumerate(lis_file,start=1):
            print(f"{i}.",item)

def total_expense():
    """This function allow you to tell how much total money you spend"""
    with open("F:\Coding\expense trackor\data.json","r") as f:
        read=f.read()
        lis_file=json.loads(read)
        total=0
        for item in lis_file:
            total+=item["amount"]
        print(f"your total money spent is : {total:,}")
    
def most_used_category():
    """This function tell in which catogery you spend most of your money"""
    with open("F:\Coding\expense trackor\data.json","r") as f:
        lis_file=json.load(f)
        category_count={}
        for i in lis_file:
            category=i["field"]
            if category in category_count:
                category_count[category]+=1
            else:
                category_count[category]=1
        maximum=max(category_count,key=category_count.get)
        print(f"[{maximum}]")