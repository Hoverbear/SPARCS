# Derived from http://johnlawrenceaspden.blogspot.ca/2009/11/program-for-twelve-year-old-programmers.html
from turtle import *

def fib(n):
    forward(30)

    if n<2:
        pass
    else:
        left(15)
        fib(n-1)
        right(30)
        fib(n-2)
        left(15)

    forward(-30)

reset()
fib(10)
done()
