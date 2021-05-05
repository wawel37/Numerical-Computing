import numpy as np
import collections
from random import shuffle
from copy import deepcopy

def cost(table, solved):
    result = 0
    N = len(table)
    temp = np.zeros((9,9))
    counter = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == -1:
                temp[i][j] = solved[counter]
                counter += 1
            else:
                temp[i][j] = table[i][j]
    
    #columns
    for row in temp:
        result += N - len(np.unique(row))

    #row
    for i in range(N):
        result += N - len(np.unique(temp[:,i]))

    #squares
    for j in range(0,7,3):
        for i in range(0,7,3):
            result += N - len(np.unique(temp[i:i+3,j:j+3]))

    return result

def swap(path):
    swapped = deepcopy(path)
    n = len(path)

    a = np.random.randint(0,n-1)
    b = np.random.randint(0,n-1)
    while a == b:
        a = np.random.randint(0,n-1)
        b = np.random.randint(0,n-1)

    swapped[a], swapped[b] = swapped[b], swapped[a]
    return swapped
    

def annealing(table, solved):
    T = 0.5
    counter = 0
    for _ in range(20000):
        prev_cost = cost(table, solved)
        swapped = swap(solved)
        if cost(table, swapped) <= cost(table, solved):
            solved = swapped
            counter = 0
        else:
            if np.random.uniform(0,1) < np.exp((cost(table,solved) - cost(table,swapped)/T)):
                solved = swapped
                counter = 0
            else:
                counter += 1
        T *= 0.9999
        if counter == 100:
            #T += 0.3*0.5
            counter = 0

        print(prev_cost)

    return solved

table = np.empty((9,9),int)

filename = "sudoku3.txt"
with open(filename,"r") as f:
    text = f.read().split("\n")
    text = text[:-1]
    for row,line in enumerate(text):
        chars = line.split(" ")
        for col in range(len(chars)):
            table[row][col] = int(chars[col])

print(table)

count0 = 0
counter = [0 for i in range(10)]
for i in table:
    for j in i:
        if j == -1:
            continue
        counter[j] += 1

solved = []
for i in range(1, 10):
    for j in range(9-counter[i]):
        solved.append(i)
    
print(count0 == len(solved))

shuffle(solved)
print(solved)
print(cost(table,solved))

solved = np.array(solved)

solved = anneling(table, solved)

print(cost(table,solved))







