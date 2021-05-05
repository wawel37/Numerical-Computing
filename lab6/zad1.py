import numpy as np
import decimal as dec
import math
from sys import maxsize
import mpmath as mp
import matplotlib.pyplot as plt



f1 = lambda x: mp.cos(x)*mp.cosh(x) - 1
f2 = lambda x: 1/x - mp.tan(x) if x != 0 else maxsize
f3 = lambda x: 2**(-x) + mp.exp(x) + 2*mp.cos(x) - 6
f1d = lambda x: mp.cos(x)*mp.sinh(x) - mp.sin(x)*mp.cosh(x)
f2d = lambda x: -1/(x**2) - 1/(mp.cos(x)**2)
f3d = lambda x: mp.exp(x) - (2**(-x)*mp.log(2) -2*mp.sin(x))
funcs = [f1, f2, f3]
funcsD = [f1d, f2d, f3d]
intervals = [(3/2*math.pi, 2*math.pi), (0, math.pi/2), (1,3)]
precisions = [math.pow(10,-7), math.pow(10, -15), math.pow(10, -33)]
DEC = mp.mpf




def bisection(f, a, b, precision, E):
    mp.mp.dps = precision

    if mp.sign(f(a)) == mp.sign(f(b)):
        print("no root")
        return (maxsize, maxsize)

    middle = DEC(a) + (DEC(b)-DEC(a))/2
    numOfSteps = 0
    while abs(DEC(a) - DEC(b)) > E:
        middle = DEC(a) + (DEC(b)-DEC(a))/2
        if mp.sign(f(middle)) != mp.sign(f(a)):
            b = middle
        else:
            a = middle
        numOfSteps += 1

    return (middle, numOfSteps)


def newTon(f, fd, precision, E, maxIterations, a, b):
    mp.mp.dps = precision
    a = DEC(a)
    b = DEC(b)

    iterator = 0
    middle = DEC(a) + (DEC(b) - DEC(a))/2

    if mp.sign(f(a)) == mp.sign(f(b)):
        print("no root")
        return maxsize, maxsize

    while abs(f(middle)) > E and iterator < maxIterations:
        middle = DEC(middle) - (DEC(f(middle))/DEC(fd(middle)))
        iterator += 1
    
    return middle, iterator


def secant(f, precision, maxIterations, E, a, b):
    mp.mp.dps = precision
    
    if mp.sign(f(a)) == mp.sign(f(b)):
        print("no root")
        return (maxsize, maxsize)
    
    a = DEC(a + 1e-4)
    b = DEC(b - 1e-4)

    iterator = 0
    
    while abs(DEC(a) - DEC(b)) > E and maxIterations > iterator:
        middle = DEC(b) - f(b) * (DEC(b)-DEC(a))/(f(b) - f(a))
        a = b
        b = middle

    return middle, iterator
    
print("")
print("newton:")
for precision in precisions:

    print("")
    print("precision: ", precision)
    for i in range(3):
        root, steps = newTon(funcs[i], funcsD[i], 64, precision, 50, intervals[i][0], intervals[i][1])
        print("root: ", root)
        print("steps: ", steps)

print("")
print("secant:")
for precision in precisions:

    print("precision: ", precision)
    print("")
    for i in range(3):
        root, steps = secant(funcs[i], 64, 50, precision, intervals[i][0], intervals[i][1])
        print("root: ", root)
        print("steps: ", steps)

    
print("")
print("bisection:")
for precision in precisions:

    print("precision: ", precision)
    print("")
    for i in range(3):
        root, steps = bisection(funcs[i], intervals[i][0], intervals[i][1], 64, precision)
        print("root: ", root)
        print("steps: ", steps)


for i in range(3):
    X = np.linspace(intervals[i][0], intervals[i][1], 100)
    Y = [funcs[i](X[j]) for j in range(len(X))]
    plt.plot(X,Y)
    plt.show()

    
