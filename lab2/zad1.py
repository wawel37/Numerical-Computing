import numpy as np
from sys import maxsize

def findBiggestModuleIndexAt(A, idx):
    N = len(A[idx])
    maxModule = -maxsize
    idx = 0
    for i in range(N):
        if maxModule < abs(A[idx][i]):
            maxModule = abs(A[idx][i])
            idx = i

    return idx

def swapRows(A, row1, row2):
    for i in range(len(A)):
        A[i][row1], A[i][row2] = A[i][row2], A[i][row1]

def addRow(A, row1, row2, multiplier):
    for i in range(len(A)):
        A[i][row1] += A[i][row2] * multiplier

    


def partialGaussJordan(A):
    N = len(A)

    #main loop
    for i in range(1):
        maxModuleIdx = findBiggestModuleIndexAt(A, i)

        

        if maxModuleIdx != i:
            swapRows(A, maxModuleIdx, i)

        for i in range(N - 1):
            for j in range(N):
                print(A[j][i], end="")
            print("")  
        
        for j in range(0, N - 1):
            if j != i:
                addRow(A, j, i, -(A[i][j]/A[i][i]))   
        


N = 4
A = [[i + 1 for j in range(N)] for i in range(N + 1)]
print(A)

partialGaussJordan(A)