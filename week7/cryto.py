message = input("tell me what your message to encrypt is: ")

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

k = 10

secret = ""

for c in message.upper():
  secret+=(alpha[(alpha.index(c)+k)%len(alpha)])

print(secret)
