# Loops! Loops! Loops!
# The above is an example of a loop. Loops are for when you want to do something repeatedly, or to work with a list.

# First, some useful things for us to know.
my_range = range(10)
# This creates an "iterator" which is sort of like a list, in fact, we can use a cast to make a list out of it.
print(list(my_range)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# We're not going to get into what iterators actually are quite yet, so lets just think of them as lists.

# A normal range
range(10) # 0 to 10 (Not including 10!)
# Specify a starting point.
range(5,10) # 5 to 10 (Not including 10!)
# By steps.
range(0,10,2) # [0,2,4,6,8] (Again, no 10)

# Okay, now that we know how to use ranges, lets try looping!
for number in range(10):
	print(str(number)) # Holy jeez, this prints out 0 to 9!
	
for number in range(0, 10, 2):
	another_list = list(range(number, 10))
	print(another_list) # What do you think this prints?

# Ranges are cool, and useful, but what if I wanted to use one of those handy list things?
for item in ["My", "Handy", "List"]:
	print("One item of the list is: " + item)
# Well isn't that useful! Lets try some more!

# So loops are handy, but what if we don't know how many times we want to loop? For example, I want to loop until the user inputs "Potato".
# Thankfully, there's something called a "while" loop.
while input("Enter 'Potato' to finish the loop: ") != "Potato":
	print("That's not 'Potato', I'll keep going.")
print("You got out of the loop!")

# Okay, that works, our tool box is growing really big now! There's just one more thing about loops that we should talk about: What if I want to finish early?
# For example: We want loop through a list of names and say hi to everyone, except if we see "Selena Gomez", then we should stop, because she's magic.
names = ["Simon", "Andrew", "Frosty", "Oscar", "Fred", "Selena Gomez", "Someone who doesn't get printed"]
for name in names:
	if name == "Selena Gomez":
		print("OMG IT'S SELENA GOMEZ.")
		break
	print("Hello there, " + name + "!")
	
	
# *** CHALLENGE TIME ***
# Okay, here's a fun problem... Actually, this is an interview question for hiring REAL programmers.
# Here's the problem:
#	For all the numbers from 0 to 100 (not including 100),
#	If a number is divisible by 3, print out "Fizz"
#	If a number is divisible by 5, print out "Buzz"
#	Otherwise, just print out the number.
# Hint: You'll want to use the modulo operator we talked about earlier. (4 % 2 == 0, or "The remainder of 4 divided by 2 is zero")
# *** END OF CHALLENGE TIME ***

# Congratulations! Lets cover more about lists!