#This is a hangman game!
import random


def draw(x):
    s = ("There are "+str(x)+" body parts left.")
    if x == 6:
        print (
        "   /------\\\n"
        "  |        |\n"
        " /-\\       |\n"
        " \\-/       |\n"
        "  |        |\n"
        "--|--      |\n"
        "  |        |\n"
        " / \\       |\n"
        "/   \\      |\n"
        "           |\n"
        "  ------------"
        )
    elif x == 5:
        print (
        "   /------\\\n"
        "  |        |\n"
        " /-\\       |\n"
        " \\-/       |\n"
        "  |        |\n"
        "--|--      |\n"
        "  |        |\n"
        " /         |\n"
        "/          |\n"
        "           |\n"
        "  ------------"
        )
    elif x == 4:
        print (
        "   /------\\\n"
        "  |        |\n"
        " /-\\       |\n"
        " \\-/       |\n"
        "  |        |\n"
        "--|--      |\n"
        "  |        |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "  ------------"
        )
    elif x == 3:
        print (
        "   /------\\\n"
        "  |        |\n"
        " /-\\       |\n"
        " \\-/       |\n"
        "  |        |\n"
        "--|        |\n"
        "  |        |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "  ------------"
        )
    elif x == 2:
        print (
        "   /------\\\n"
        "  |        |\n"
        " /-\\       |\n"
        " \\-/       |\n"
        "  |        |\n"
        "  |        |\n"
        "  |        |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "  ------------"
        )
    elif x == 1:
        print (
        "   /------\\\n"
        "  |        |\n"
        " /-\\       |\n"
        " \\-/       |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "  ------------"
        )
    elif x == 0:
        print (
        "   /------\\\n"
        "  |        |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "           |\n"
        "  ------------"
        )
    return s

    
def get_random_word(words):
    return "abc"
    #return words[random.randint(0, len(words))]
    

def check_guess(word, working, char):
    r = list(working)
    for i in range(len(word)):
        if char == word[i]:
            r[i] = char
    return ''.join(r) 

def play(words):

    num_parts = 6 #man starts with 6 body parts
    word = get_random_word(words)
    working_word = "_"*len(word)
    guessed = list() 

    while(True):
        print((draw(num_parts)))
        if(num_parts == 0):
            print("YOU loose!")
        print("------------")
        print("Current word is:")
        print(working_word)
        print('------------')
        print("g -> guess a letter, h -> view previsouly guessed letters")
        i = input(">>>")
        if i=='g' or i=="G":
            i = input("Enter your guess (lowercase): ")
            print('your guess was: '+str(i))
            guessed.append(str(i))
            saved = working_word
            working_word = check_guess(word, working_word, i)
            if working_word == saved:
                num_parts -= 1
            
        elif i=='h' or i=="H":
            print(guessed)
        else: 
            print("")

        print("")
        print("")
        print("===========")

    exit() #the game is over, done playing, exit

def exit(): 
    print ("=========================")
    print("Exiting Hangman game, bye bye.")

def setup(words):
    for w in open("words"):
        words.append(w.strip()) #add the words to the list words for the game

def welcome():
    print("Welcome to the Hangman game!")
    print('---------------------------')
    print ('Loading....')
    words = list()
    setup(words)
    print("===========================")
    print("A random word as been selected from a dictionary of words....you need to guess it.")
    response = input("Ready to play? (Y/N)")
    if response == "Y" or response == "y":
        play(words)
    else:
        exit()

if __name__ == "__main__":
    welcome()
