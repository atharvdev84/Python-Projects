history=[]
def instruction():
    rule = """
    1 additon 
    2 subtraction
    3 mutliplication 
    4 division
    """
    print(rule)

    while True:
        ask = input("enter  what you wanna do [sub mul div add exit] or [history] : ")
        num1 = int(input("enter the first number : "))
        num2 = int(input("enter the second number : "))

        def add(num1, num2):
            return num1+num2

        def sub(num1, num2):
            return num1-num2

        def mul(num1, num2):
            return num1*num2

        def div(num1, num2):
            return num1/num2

        
        if ask == "exit":
            print("thanks for coming")
            break
        elif ask == "add":
            sum=add(num1, num2)
            print(sum)
            history.append(sum)
        elif ask == "sub":
            diff=sub(num1, num2)
            print(diff)
            history.append(diff)
        elif ask == "mul":
            x=mul(num1, num2)
            print(x)
            history.append(x)
        elif ask == "div":
            divide=div(num1, num2)
            print(divide)
            history.append(divide)
        elif ask == "history":
            for i in history:print(i)
        else:
            print("error")

instruction()