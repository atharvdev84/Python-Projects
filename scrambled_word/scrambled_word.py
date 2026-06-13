import random
def lis():
     word_list = [
     "apple", "banana", "orange", "grape", "mango", "peach", "cherry", "lemon", "melon", "berry",
     "chair", "table", "sofa", "shelf", "clock", "candle", "mirror", "window", "door", "floor",
     "river", "ocean", "forest", "mountain", "valley", "island", "desert", "beach", "cloud", "storm",
     "tiger", "lion", "zebra", "horse", "monkey", "panda", "rabbit", "eagle", "shark", "whale",
     "school", "college", "teacher", "student", "lesson", "class", "board", "pen", "pencil", "book",
     "music", "dance", "song", "guitar", "piano", "drum", "violin", "radio", "movie", "actor",
     "happy", "sad", "angry", "brave", "calm", "quick", "slow", "bright", "dark", "funny",
    "water", "fire", "earth", "wind", "light", "sound", "energy", "power", "force", "space",
     "train", "plane", "truck", "car", "bike", "bus", "road", "bridge", "tunnel", "engine",
     "bread", "butter", "cheese", "milk", "coffee", "sugar", "salt", "rice", "pasta", "pizza",
    "phone", "laptop", "screen", "mouse", "keyboard", "camera", "charger", "battery", "signal", "network",
     "family", "friend", "people", "child", "parent", "brother", "sister", "uncle", "aunt", "cousin"
     ]
     word= random.choice(word_list)
     return word

def main():
    print("Welcome to the Word Scramble Game!")
    print("Unscramble the letters to form a valid word.")
    word = lis()
    shuffle_word=list(word)
    random.shuffle(shuffle_word)
    scrambled_word="".join(shuffle_word)
    attempt=3
    while attempt>0:      
        print(f"Scrambled word: {scrambled_word}")
        user_guess = input("Your guess: ")
        if user_guess==word:
            print("congtatulation")
            break
        else:
            print("try again")
            attempt-=1
        if attempt==0:
            print(f"you lose the word was {word}")          
main()
