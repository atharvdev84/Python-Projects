import random
detail = ["r", "p", "s"]
computer_score = 0
score = 0

for i in range(10):
    computer = random.choice(detail)
    print(computer)
    user = input("enter rock paper or sissior [r/p/s] : ")

    if user == computer:
        print("it's a tie")
    elif user == "r" and computer == "p":
        print("computor won")
        computer_score += 1
    elif user == "p" and computer == "s":
        print("computor won")
        computer_score += 1
    elif user == "s" and computer == "r":
        print("computor won")
        computer_score += 1
    elif user == "p" and computer == "r":
        print("player won")
        score += 1
    elif user == "s" and computer == "p":
        print("player won")
        score += 1
    elif user == "r" and computer == "s":
        print("player won")
        score += 1
    else:
        print("invalid")

print(f"your total score is {score}")
print(f"computer total score is {computer_score}")
