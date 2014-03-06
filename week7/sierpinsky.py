# Derived from https://qfunction.wordpress.com/2009/11/11/turtle-graphics-in-python-cool/

from turtle import *

def striangle(depth,base):
   down()
   if depth == 0:
      begin_fill()
      for i in 0,1,2:
         forward(base)
         left(120)
      end_fill()
   else:
      for i in 0,1,2:
         striangle(depth-1,base)
         up()
         forward(base*2**depth)
         left(120)
         down()

reset()
speed(10)
striangle(6,5)
done()
