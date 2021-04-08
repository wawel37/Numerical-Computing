import numpy as np
from random import randint
import matplotlib


f2 = lambda x: 1/(x**3-2*x-5)
f3 = lambda x: x**5*np.exp(-x)*np.sin(x)

def trapez(x, y):
    N = len(x)

    integral = 0
    for i in range(N - 1):
        h = x[i + 1] - x[i]
        integral += (y[i] + y[i+1])*h/2
    
    return integral

x = list(np.arange(0, 100, 1))
y = [f2(i) for i in x]

print("Difference: ", abs(trapez(x,y) - np.trapz(y, x)))

y = [f3(i) for i in x]

print("Difference: ", abs(trapez(x,y) - np.trapz(y, x)))
