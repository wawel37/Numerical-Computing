import numpy as np
import time

def matrixValue(i, j, n):
    return np.exp(-2.j*np.pi*i*j/n)

def F(n):
    return np.fromfunction(lambda i, j: matrixValue(i, j, n), (n, n))

def DFT(x):
    return F(len(x)) @ x

def IDFT(y):
    n = len(y)
    return np.conj(F(n) @ np.conj(y))/n

def FFT(x):
    n = len(x)
    if n <= 1:
        return x
    
    even = FFT([x[2*i] for i in range(n//2)])
    odd = FFT([x[2*i+1] for i in range(n//2)])

    result = np.empty(n, dtype=np.complex64)
    for i in range(n//2):
        tmp = odd[i] * np.exp(-2.j*np.pi*i/n)
        result[i] = even[i] + tmp
        result[i+n//2] = even[i] - tmp
    
    return result

x = np.random.rand(4)

s = time.time()
y1 = DFT(x)
e = time.time()
print("Basic DFT: ", str(e-s) + "ns")

s = time.time()
y2 = FFT(x)
e = time.time()
print("Recursive FFT: ", str(e-s) + "ns")

s = time.time()
y3 = np.fft.fft(x)
e = time.time()
print("Numpy FFT: ", str(e-s) + "ns")

#wyniki różnią się tylko o dopuszczalne błędy dokładnosci obliczeń
print(y1)
print(y2)
print(y3)