import format
while True:
    print("if you wanna exit type exit,leave or  press enter")
    location=input("Enter your file or location path which you wanna organize : ")
    if location=="exit" or location=="" or location=="leave":
        break
 
    print("""
        MENU
    1.text_format
    2.image_format
    3.video_format
    4.Audio_format
    5.Pdf_format
    6.All_format
    7.Exit
        
        Enter the Number beside name to start using function""")

    try:
        user=int(input("enter the number which formating you wanna use : "))
    except ValueError:
        print("Invalid")
    else:
        if user==1:
            format.text_format(location)
        elif user==2:
            format.image_format(location)
        elif user==3:
            format.video_format(location)
        elif user==4:
            format.Audio_format(location)
        elif user==5:
            format.Pdf_format(location)
        elif user==6:
            format.All_format(location)
        elif user==7:
            print("Thanks for Coming")
            break
        else:
            print("Can select only number which are in MENU")