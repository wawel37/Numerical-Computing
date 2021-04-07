import numpy as np
from sys import maxsize
from time import time
from matplotlib import pyplot as plt
from copy import deepcopy

def findBiggestModuleIndexAt(A, idx):
    N = len(A)
    maxModule = -maxsize
    result = idx
    for i in range(idx, N):
        if maxModule < abs(A[idx][i]):
            maxModule = abs(A[idx][i])
            result = i

    return result

def generateMatrix(N):
	A = np.random.random_sample((N,N))
	B = np.random.random_sample((N,))
	return A,B

def gaussSolve(A, B):

    N = len(A)

    for i in range(N):
        maxModuleIdx = findBiggestModuleIndexAt(A, i)

        if maxModuleIdx != i:
            A[[maxModuleIdx, i]] = A[[i, maxModuleIdx]]
            B[maxModuleIdx], B[i] = B[i], B[maxModuleIdx]

        for j in range(N):
            if i != j:
                multiplier = A[j][i] / A[i][i]

                A[j] += - multiplier * A[i]
                B[j] += - multiplier * B[i]           
            
    return B/np.diag(A)

gaussTimes = []
basicTimes = []
leastSquaresTimes = []



for N in range(500, 1500, 100):
    A1, B1 = generateMatrix(N)
    A2, B2, A3, B3 = deepcopy(A1), deepcopy(B1), deepcopy(A1), deepcopy(B1)

    print("")
    print("---- Gauss method ----")
    start = time()
    result = gaussSolve(A1, B1)
    end = time()
    gaussTimes.append((N, end - start))
    print("N =", N, " sec:", end-start)

    print("")
    print("---- Regular method ----")
    start = time()
    basicResult = np.linalg.solve(A2, B2)
    end = time()
    basicTimes.append((N, end - start))
    print("N =", N, " sec:", end-start)


    print("")
    print("---- Least Squares method ----")
    start = time()
    lstsqResult = np.linalg.solve(A3, B3)
    end = time()
    leastSquaresTimes.append((N, end - start))
    print("N =", N, " sec:", end-start)
    
