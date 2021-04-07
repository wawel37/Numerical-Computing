import numpy as np
from copy import deepcopy


def decomposition(A):
    N = len(A)

    for diag in range(0, N - 1):
        for row in range(diag + 1, N):
            multiplier = A[row][diag]/A[diag][diag]
            A[row][diag + 1:N] -= multiplier * A[diag][diag+1:N]
            A[row][diag] = multiplier
    

A = np.array([[2,-1,-2],[-4,6,3],[-4,-2,8]]).astype(float)



decomposition(A)

print(A)

