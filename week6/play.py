from turtle import *
color('red', 'yellow')
begin_fill()
# Draw somethng
while True:
  iterations = 0
  while iterations < 120:
    forward(5)
    left(3)
    iterations += 1
  forward(20)
end_fill()
done()
