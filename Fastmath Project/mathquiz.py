import random
import time
total_question = 10

score = 0
mistake = 0
slow_answer = 0
for i in range(total_question):

    computer = random.randint(0, 20)
    computer2 = random.randint(0, 10)

    print(f"{computer} x {computer2} = ")

    starting_time = time.time()

    user_answer = int(input("enter the answer : "))
    result = computer*computer2

    ending_time = time.time()
    total_time = ending_time-starting_time

    if total_time > 5:
        print("slow")
        slow_answer += 1
        continue
    else:
        pass

    if user_answer == result:
        print("correct")
        score += 1
    else:
        mistake += 1

        print(f"Inccorect. Correct answer was {result}")

accuracy = (score/total_question)*100

print(f"the total score is {score}")
print(f"the total mistake was {mistake}")
print(f"the total slow answer was {slow_answer}")
print(f"your accuracy is {accuracy}")
