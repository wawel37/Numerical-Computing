import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft

N = 5
LENGTH = 500
DOMAIN = np.arange(0,1,1/LENGTH)

def generateSinusoidal(f):
    return np.sin(2 * np.pi * f * DOMAIN)

signals = []
sum = [0 for i in range(LENGTH)]
sum2 = []
freqs = [10,20,40,80,160]
for i in range(N):
    f = freqs[i]
    newSignal = generateSinusoidal(f)
    signals.append(newSignal)
    sum += newSignal
    toExtend = newSignal[i*LENGTH//N:(i+1)*LENGTH//N]
    sum2.extend(toExtend)

plt.plot(DOMAIN, sum)
plt.title("First signal in domain")
plt.show()

plt.plot(DOMAIN, sum2)
plt.title("Second signal in domain")
plt.show()

y = fft(sum)
plt.plot(np.real(y))
plt.title("First signal in frequency domain - real value")
plt.show()

plt.plot(np.imag(y))
plt.title("First signal in frequency domain - imaginary value")
plt.show()

y = fft(sum2)
plt.plot(np.real(y))
plt.title("Second signal in frequency domain - real value")
plt.show()

plt.plot(np.imag(y))
plt.title("Second signal in frequency domain - imaginary value")
plt.show()



