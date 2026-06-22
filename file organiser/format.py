import os,shutil
def folder_name():
    user=input("do you wanna name your folder where you wanna organise file y/n : ").lower()
    if user=="y" or user=="yes" or user=="sure" or user=="ok":
        name=input("Enter the folder name where you wanna organise file : ")
        return name
    else:
        return "n"

def text_format(data):
    """Format .txt files or text"""
    folder=folder_name()
    data2=os.listdir(data)
    count_text=0
    for i in data2:
        join=os.path.join(data,i)
        check=os.path.isfile(join)
        if check==True:
            if folder=="n":
                join2=os.path.join(data,"Text")
            else:
                join2=os.path.join(data,f"{folder}")
            if i.endswith((".txt",".doc",".docx",".rtf")):
                if os.path.exists(join2):
                    pass
                else:
                    os.mkdir(join2)
                try:
                    shutil.move(join,join2)
                except PermissionError:
                    print("Permission denied")
                else:
                    count_text+=1
    print(f"Moved {count_text} Text files")
                    
    
def image_format(data):
    folder=folder_name()
    """Format .img files or image"""
    data2=os.listdir(data)
    count_image=0
    duplicate=0
    for i in data2:
        join=os.path.join(data,i)
        check=os.path.isfile(join)
        if check==True:
            if folder=="n":
                join2=os.path.join(data,"Image")
            else:
                join2=os.path.join(data,f"{folder}")
            if i.endswith((".img",".jpg",".png",".gif",".bmp",".webp")):
                if os.path.exists(join2):
                    pass
                else:
                    os.mkdir(join2)
                try:
                    final_path=os.path.join(join2,i)
                    if os.path.exists(final_path):
                        duplicate+=1
                        name,ext=os.path.splitext(i)
                        path2=f"{name}_{duplicate}{ext}"
                        new_path=os.path.join(join2,path2)
                        shutil.move(join,new_path)
                    else:
                        shutil.move(join,join2)
                except PermissionError:
                    print("Permission denied")
                else:
                    count_image+=1
    print(f"Moved {count_image} Image files")
        

def video_format(data):
    folder=folder_name()
    """Format .mp4 files or video"""
    data2=os.listdir(data)
    count_video=0
    for i in data2:
        join=os.path.join(data,i)
        check=os.path.isfile(join)
        if check==True:
            if folder=="n":
                join2=os.path.join(data,"Video")
            else:
                join2=os.path.join(data,f"{folder}")
            if i.endswith((".mp4",".mov",".mkv",".avi",".fiv",".wmv")):
                if os.path.exists(join2):
                    pass
                else:
                    os.mkdir(join2)
                try:
                    shutil.move(join,join2)
                except PermissionError:
                    print("Permission denied")
                else:
                    count_video+=1
    print(f"Moved {count_video} Video files")

def Audio_format(data):
    folder=folder_name()
    """Format .mp3 files or audio"""
    data2=os.listdir(data)
    count_audio=0
    for i in data2:
        join=os.path.join(data,i)
        check=os.path.isfile(join)
        if check==True:
            if folder=="n":
                join2=os.path.join(data,"Audio")
            else:
                join2=os.path.join(data,f"{folder}")
            if i.endswith((".mp3",".wav",".aac",".flac",".ogg")):
                if os.path.exists(join2):
                    pass
                else:
                    os.mkdir(join2)
                try:
                    shutil.move(join,join2)
                except PermissionError:
                    print("Permission denied")
                else:
                    count_audio+=1
    print(f"Moved {count_audio} Audio files")

def Pdf_format(data):
    folder=folder_name()
    """Format .pdf files or pdf"""
    data2=os.listdir(data)
    count_pdf=0
    for i in data2:
        join=os.path.join(data,i)
        check=os.path.isfile(join)
        if check==True:
            if folder=="n":
                join2=os.path.join(data,"Pdf")
            else:
                join2=os.path.join(data,f"{folder}")
            if i.endswith(".pdf"):
                if os.path.exists(join2):
                    pass
                else:
                    os.mkdir(join2)
                try:
                    shutil.move(join,join2)
                except PermissionError:
                    print("Permission denied")
                else:
                    count_pdf+=1
    print(f"Moved {count_pdf} Pdf files")
                

def All_format(data):
    text_format(data),image_format(data),video_format(data),Audio_format(data),Pdf_format(data)