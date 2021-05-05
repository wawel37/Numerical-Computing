import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def generateImg(density, N):
    result = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if np.random.uniform(0,1) <= density:
                result[i][j] = 1
    
    return result

def singleEnergy16(i, j, img):
    region = img[max(0, i-2) : i+3,
                 max(0, j-2) : j+3]
    
    #getting the number of zeros at the radius = 2
    result = 16 - (np.sum(region) - img[i,j] - singleEnergy8(i, j, img))
    #adding number of ones at the radius = 1
    result += singleEnergy8(i, j, img)
    return result

def singleEnergy8(i, j, img):
    region = img[max(0, i-1) : i+2,
                 max(0, j-1) : j+2]
    return np.sum(region) - img[i, j]

def singleEnergy4(i,j,img):
    result = 0
    if i > 0:
        result += img[i-1][j]
    if i < len(img) - 1:
        result += img[i + 1][j]
    if j > 0:
        result += img[i][j - 1]
    if j < len(img) - 1:
        result += img[i][j + 1]
    
    return result

def reverseSingleEnergy4(i,j,img):
    return 4 - singleEnergy4(i, j, img)

def reverseSingleEnergy8(i,j,img):
    return 8 - singleEnergy8(i, j, img)

def reverseSingleEnergy16(i,j,img):
    region = img[max(0, i-2) : i+3,
                 max(0, j-2) : j+3]

    result = (np.sum(region) - img[i,j] - singleEnergy8(i, j, img))
    result += (9 - singleEnergy8(i, j, img))

    return result
    




def cost(img, energyFunction):
    N = len(img)
    result = 0
    for i in range(N):
        for j in range(N):
            if img[i][j] == 1:
                result += energyFunction(i,j,img)
    
    return result

def simpleSwap(img):
    N = len(img)
    x1 = np.random.randint(0, N)
    x2 = np.random.randint(0, N)
    y1 = np.random.randint(0, N)
    y2 = np.random.randint(0, N)

    a = img[x1][y1]
    b = img[x2][y2]
    while (x1 == x2 and y1 == y2) or (a == b):
        x1 = np.random.randint(0, N)
        x2 = np.random.randint(0, N)
        y1 = np.random.randint(0, N)
        y2 = np.random.randint(0, N)
        a = img[x1][y1]
        b = img[x2][y2]


    img[x1][y1], img[x2][y2] = img[x2][y2], img[x1][y1]

def anneling(img, energyFunction):
    T = 0.5
    numOfIters = len(img) * 15
    for _ in range(numOfIters):
        swapped = deepcopy(img)
        simpleSwap(swapped)
        if cost(swapped, energyFunction) < cost(img, energyFunction):
            img = swapped
        else:
            if np.random.uniform(0,1) < np.exp((cost(swapped, energyFunction) - cost(img, energyFunction)/T)):
                img = swapped
        T *= 0.9
        if(cost(img, energyFunction) == 0):
            break 
    
    return img

def drawImage(density, N, energyFunction):

    img = generateImg(density, N)

    fig, axes = plt.subplots(nrows = 1, ncols = 2)
    axes[0].imshow(img, cmap= 'gray')

    result = anneling(img, energyFunction)

    axes[1].imshow(result, cmap = 'gray')
    plt.show()


drawImage(0.4, 10, singleEnergy16)


