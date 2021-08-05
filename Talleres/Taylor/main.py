import sympy as sy
import numpy as np

x = sy.Symbol('x')
f= 1/(1-x)

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

def taylor(function, xo, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x, i).subs(x,xo))/(factorial(i))*(x-xo)**i
        i += 1
    return p

print (taylor(f, 0, 4))
