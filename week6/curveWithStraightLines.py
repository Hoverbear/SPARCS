from turtle import *
import random
size = 200

colours = []
for c in range(size):
   colours.append((int(random.random()*255), int(random.random()*255), int(random.random()*255)))

penup()
for p in range(0,size,10):
  goto(0,size-p)
  pendown()
  pencolor(colours[p])
  goto(p+1, 0)
  penup()
