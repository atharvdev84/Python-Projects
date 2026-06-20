import json
def save_data(user_data):
    """it is use to save the data """
    with open("F:\Coding\expense trackor\data.json","r") as file:
        new_data=json.load(file)

    if not isinstance(new_data,list):
        new_data=[new_data]
    new_data.append(user_data)
        
    with open("F:\Coding\expense trackor\data.json","w") as file:
        json.dump(new_data,file,indent=4)
#_____________________________________________________________________________________

def save_data2(user_data):
    """it is use to save the remove data """
    with open("F:\Coding\expense trackor\data.json","w") as file:
        json.dump(user_data,file,indent=4)