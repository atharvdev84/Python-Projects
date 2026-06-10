import random
computer = random.randint(1, 100)
print(computer)
score = 0

while True:
    try:
        user = int(input("enter the number between 1 to 100 : "))
        if user > 100:
            print("number greator than 100 is invalid")
        elif user == computer:
            print(f"Congratulation you win on {score} try")
            break
        elif user > computer:
            print("Too high")
            score += 1
        elif user < computer:
            print("Too low")
            score += 1
        else:
            print("invalid")
    except:
        print("error")
        continue
