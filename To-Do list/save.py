import json
def save_data(user):
    with open("F:\Coding\To-Do list\To-Do_data.json","r") as f:#Use your own data.json path
        data=json.load(f)

    if not isinstance(data,list):
        data=[data]
    data.append(user)

    with open("F:\Coding\To-Do list\To-Do_data.json","w") as f:#Use your own data.json path
        json.dump(data,f,indent=4)

def save_data2(user):
    with open("F:\Coding\To-Do list\To-Do_data.json","w") as f:#Use your own data.json path
        json.dump(user,f,indent=4)