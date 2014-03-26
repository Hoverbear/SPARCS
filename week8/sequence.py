# Number sequences
so_far = [1, 1]

while len(so_far) < 20: 
  next_number = so_far[-1] + so_far[-2] # Last two numbers added together.
  so_far.append(next_number) # Add to the last spot of the list.

print(so_far)

# Can you make a function that returns a list with a size the user specifies?
# For example:
#   sequence(20)
# Would return the first 20 items of the sequence.
# Tip:
#   def sequence(number_of_items):
#     ** Your stuff goes here **
