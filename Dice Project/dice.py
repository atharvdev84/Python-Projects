import random
while True:
    try:
        a = input("enter y/n : ")
        if a == "y":
            b = random.randint(1, 6)
            c = random.randint(1, 6)
            print(f"{b, c}")
        elif a == "n":
            print("thanks for playing")
            break
        else: print("invalid")
    except:  print("error")
