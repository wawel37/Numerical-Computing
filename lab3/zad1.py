import numpy as np
from matplotlib import pyplot as plt
from math import factorial
from sys import maxsize

def f(x):
    return 1/(1 + x**2)

def getIntervals(interval, N):
    return np.linspace(interval[0], interval[1], N + 1)

def newton(s, k):
    l = np.prod([s - i for i in range(k)])
    m = factorial(k)
    return l/m





interval = (-5, 5)
N = 10
X = getIntervals(interval, N)

dynamic = [[maxsize for i in range(N + 1)] for j in range(N + 1)]
for i in range(N + 1):
    dynamic[0][i] = f(X[i])

for j in range(1, N + 1):
    for i in range(N):
        dynamic[j][i] = dynamic[j - 1][i + 1] - dynamic[j - 1][i]


delta = [dynamic[j][0] for j in range(N + 1)]

def Wn(X, N, x, f, delta):
    result = 0
    h = X[1] - X[0]
    s = (x - X[0])/h
    for k in range(N + 1):
        result += newton(s, k)*delta[k]

    return result


x = getIntervals(interval, 10000)
y1 = [Wn(X, N, x[i], f, delta) for i in range(10001)]
y2 = [f(x[i]) for i in range(10001)]
intervalDistance = getIntervals(interval, 30)
error = [abs(f(intervalDistance[i]) - Wn(X, N, intervalDistance[i], f, delta)) for i in range(31)]
plt.plot(x, y1, "r")
plt.plot(x, y2, "y")
plt.plot(intervalDistance, error, "b")
plt.show()




