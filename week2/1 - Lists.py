# Lists are space for you to store a growing or shrinking number of items, such as numbers, strings, or even other lists! (Or anything else we cover later)
# You can find out more at http://docs.python.org/3/tutorial/datastructures.html

# Lets make a variable that holds an empty list.
my_list = []

# Before you ask, yes we can make lists with things in them as well.
my_list_with_things_in_it = ["Something", 100, "Something else"]

# You can print a list.
print(my_list) # Shows us [], since it's an empty list.

# You can access specific items in a list by addressing them with [number]
# Note how it starts at 0!
my_list = ["Zero Index", "First Index", "Second Index"]
print(my_list[0]) # Zero Index
print(my_list[2]) # Second Index
my_list[0] = "Totally something else"
print(my_list) # ["Totally something else", "First Index", "Second Index"]

# Wnat to know if something is in a list?
my_list = [1,2,3]
1 in my_list # True!
if 2 in my_list:
	print("2 is in my list!")

# You can add things to a list.
my_list.append("Something")
print(my_list) # Shows us ["Something"]

# You can remove things from a list.
my_list.remove("Something")
print(my_list) # Shows us [], since the list is empty again.

# You can also remove things by their position in the list.
my_list.append("Something")
print(my_list) # Shows us ["Something"]
del my_list[0] # Note: Lists start at 0!
print(my_list) # Shows us []

# You can also combine lists together.
my_list = ["Some", "Things"]
my_list.extend(["Another", "List", "of", "things"])
print(my_list) # Shows us ['Some', 'Things', 'Another', 'List', 'of', 'things']

# What if we want the length of a list?
my_list = ["Some", "Things"]
the_length = len(my_list)
print(the_length) # Shows us 2.

# How about if I want to know how many times something appears in the list?
my_list = [1, "One", 1, "One", 1, "One", 1]
numbers = my_list.count(1) # Since we're getting numbers, we need to 'cast' them to strings in order to print!
words = my_list.count("One")
print("Numbers: " + str(numbers) + ", Words: " + str(words))

# More to come, but first, lets look at loops!