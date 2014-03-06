from turtle import *

def curve(degrees, radius, direction):
  # Degrees - A number
  # Radius - A degree (number)
  # Direction - "cw" "ccw"
  for i in range(degrees):
    forward(1)
    if direction == "cw":
      left(1)
    else:
      right(1)

curve(120, 20, "cw")
curve(120, 20, "ccw")
curve(45, 10, "cw")
curve(45, 30, "ccw")
done()
