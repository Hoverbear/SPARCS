def sequence(number_of_items):
  so_far = [1, 1]
  while len(so_far) < number_of_items:
    next_number = so_far[-1] + so_far[-2]
    so_far.append(next_number)
  return so_far # Don't forget to return it!

print(sequence(20))
