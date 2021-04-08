import numpy as np
from scipy import integrate
from math import sqrt

f1 = lambda x, y: 1/(sqrt(x + y)*(1+x+y))
f2 = lambda x, y: x**2 + y**2
f3 = lambda x, y: x + y

def trapez2D(f, x0, x1, y0, y1):
    integral = 0
    interval = 0.01
    N = int(((x1-x0)//interval)+1)
    X = np.linspace(x0, x1, N)
    Y = np.linspace(y0, y1, N)
    Xlayers = []

    for y in Y:
        sum = 0
        for i in range(N - 1):
            h = X[i + 1] - X[i]
            sum += (f(X[i],y) + f(X[i+1], y))*h/2
        Xlayers.append(sum)

    for i in range(N - 1):
        h = Y[i + 1] - Y[i]
        integral += (Xlayers[i] + Xlayers[i + 1])*h/2
    
    return integral





x0 = 0
x1 = 1
y0 = 0
y1 = 5
print("difference: ", abs(integrate.dblquad(f3, x0, x1, y0, y1)[0] - trapez2D(f3, x0, x1, y0, y1)))