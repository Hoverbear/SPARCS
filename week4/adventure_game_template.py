#This is a template for a basic adventure game.
#--------------------------------------------
def display_inventory(inv):
    """
    This function will print all the other items in your
    inventory out. 
    """
    print("---------------")
    print("Your inventory:")
    for i in inv:
        print(str(i))
    print("---------------")


def welcome():
    """
    This function will print out a welcome message to start the game. 
    """
    print("=====================")
    print("Welcome to <INSERT YOUR GAME NAME HERE>!")
    #add addition messages here
    print("=====================")
    

def main():
    #inventory, store items in your inventory using this list.
    inv = list() 

    #room number, use this variable to keep track of room numbers as 
    #characters move around:
    room= 0 #start in room 0

    resp = None #place holder for user responses
    print("") #print a blank line for styling
    while(True): #go through the loop forever
        if room == 0:
            print("Your are in room 0")
            #add in addition instructions here...
            print(" l - to go left")
            print(" r - to go right")
            print(" i - to veiw your inventory")
            resp = input("What do you want to do? ") 
            if resp == "i":
                display_inventory(inv)
                continue #loop back to the top of the loop
            elif resp == "l":
                room = 1 ##change your room number to whatever you want
                continue
            elif resp == "r":
                room = 2 #change to your own room numbers to fit your plot
                continue
            else:
                print("That was not a valid option...")
                continue
        if room == 1:
            print("your are in room 1")
        if room == 2:
            print("your are in room 1")


if __name__ == "__main__":
    welcome()
    main()
