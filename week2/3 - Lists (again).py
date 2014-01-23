# More lists! Lets talk about an application of these ideas.

# So here's the task, lets make a dictionary checker!

# There are a few steps:

# Open our list of words. (It's really big!)
dictionary_file = open("words")
dictionary = []
for item in dictionary_file:
	dictionary.append(item.strip("\n"))

# Accept some input
while True:
	word = input("Which word would you like to check?: ").lower()
	print("Checking " + word)
	if word in dictionary:
		print("That's a word!")
	else:
		print("You're joking, that's not a word!")