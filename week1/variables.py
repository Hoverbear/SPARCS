# Create a variable that contains the result of 2 + 2 (4)
my_num = 2 + 2
print(my_num + 2) # Results in 6.

# Reassign the variable to 2.
my_num = 2
print(my_num + 2) # Results in 4.

# Change (mutate) a variable.
my_num = my_num + 2 # Should be 4 now.
print(my_num + 2)   # Results in 6.

# Another way to change a variable.
my_num += 2         # Add 2 to whatever my_num is.
print(my_num)       # Results in 6

# Showing this works on strings to.
my_string = "Hello, my name is "
my_string += "Andrew"
print(my_string)