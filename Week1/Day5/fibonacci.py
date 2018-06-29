
import unittest

def fib(n):

    # Compute the nth Fibonacci number
    if n<0:
        raise IndexError("Not possible")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
       x= fibonacci(n)
       

    return x

def fibonacci(n):
    count=1
    x=0
    y=1
    temp=0
    while n!=count:
        temp=x+y
        count=count+1
        x,y=y,temp
    return temp
