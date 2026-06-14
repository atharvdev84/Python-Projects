import random

def convertor(convert1, convert2, factor):
    total_question = 10
    numbers = 100
    score = 0

    for i in range(total_question):
        computer = random.randint(0, numbers)
        result = computer*factor
        print(f"{computer} {convert1} to {convert2} =")

        try:
            user_answer = int(input("enter the answer : "))
        except:
            print("invalid")
            continue

        if user_answer == result:
            print("correct")
            score += 1
        else:
            print(f"inccorect. correct answer was {result}")

    print(f"your score is {score}")


print("""
1. cm ---> m    |   5. cm ---> mm
2. m ---> cm    |   6. mm ---> cm
3. g ---> kg    |   7. km/h ---> m/s
4. kg ---> g    |   8. m/s ---> km/h 
select the number beside unit to start asking question
""")

try:
    ask = int(input(" enter the number beside unit : "))
    if ask == 1:
        convertor("cm", "m", 0.01)
    elif ask == 2:
        convertor("m", "cm", 100)
    elif ask == 3:
        convertor("g", "kg", 0.001)
    elif ask == 4:
        convertor("kg", "g", 1000)
    elif ask == 5:
        convertor("cm", "mm", 10)
    elif ask == 6:
        convertor("cm", "mm", 0.1)
    elif ask == 7:
        convertor("km/h", "m/s", 1/3.6)
    elif ask == 8:
        convertor("m/s", "km/h", 3.6)
    else:
        pass
except:
    print("invalid")
