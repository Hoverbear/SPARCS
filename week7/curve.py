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

def rectangle(height, width):
  # Height - The height of the rectangle.
  # Width - The width of the rectangle
  forward(height)
  left(width)
  backward(height)
  right(width)

curve(360, 20, "cw")
rectangle(60, 20)
done()
