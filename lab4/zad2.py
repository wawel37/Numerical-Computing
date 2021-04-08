import numpy as np
from scipy import integrate

f1 = lambda x: np.exp(-x**2) * np.log(x)**2
f2 = lambda x: 1/(x**3-2*x-5)
f3 = lambda x: x**5*np.exp(-x)*np.sin(x)


def simpsonIntegralv2(x, y):
    N = len(x)
    h = (x[1]-x[0]) * 2

    integral = 0
    for i in range(0, N - 2, 2):
        integral += (h/6)*(y[i] + 4* y[i+1] + y[i + 2])
    return integral

x = list(np.arange(1, 100, 1))
y = [f1(i) for i in x]

print("difference: ", abs(simpsonIntegralv2(x,y) - integrate.simps(y,x)))

y = [f2(i) for i in x]

print("difference: ", abs(simpsonIntegralv2(x,y) - integrate.simps(y,x)))

y = [f3(i) for i in x]

print("difference: ", abs(simpsonIntegralv2(x,y) - integrate.simps(y,x)))


