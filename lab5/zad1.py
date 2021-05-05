import numpy as np
from math import sqrt
from copy import deepcopy
import matplotlib.pyplot as plt

N = 50
points = np.random.uniform(0, 1,(N,2))

def distance(pointA, pointB):
    return sqrt((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)

def arbitrarySwap(path):
    N = len(path)
    a = b = 0
    while a == b:
        a = np.random.randint(0, N)
        b = np.random.randint(0, N)
    
    path[[a,b]] = path[[b,a]]

def consecutiveSwap(path):
    N = len(path)
    a = np.random.randint(0, N)
    b = (a + 1) % N

    path[[a,b]] = path[[b,a]]

def cost(path):
    cost = 0
    N = len(path)
    for i in range(N):
        cost += distance(path[i], path[(i+1) % N])
    
    return cost

def anneling(path):
    T = 0.5
    for _ in range(200000):
        swapped = deepcopy(path)
        arbitrarySwap(swapped)
        if cost(swapped) < cost(path):
            path = swapped
        else:
            if np.random.uniform(0,1) < np.exp((cost(swapped) - cost(path)/T)):
                path = swapped
        T *= 0.9995
        print(cost(path))
    
    return path

result = anneling(points)


y = result[:,1]
x = result[:,0]

print('x',x)
print('y', y)
print(result)

plt.plot(x,y)
plt.show()