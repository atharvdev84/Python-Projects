def game(low=0,high=100,number=0):
    
    print(low,high,number)
    mid=(low+high)//2
    print(mid)

    user=input("enter high or low or correct : ")
    if user=="high":
        return game(low=mid+1,high=high,number=number)
    elif user=="low":
        return game(low=low,high=mid-1,number=number)
    elif user=="correct":
        print("Congratulation")
    else:
        print('invalid')
        return game(low,high)
    
game(number=25)
