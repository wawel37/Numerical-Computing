import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from numpy.linalg import svd


#function for low Rank approximation with k first significant elements
def lowRankAprox(IMG, k):
    U, E, V = svd(IMG)
    Uk = np.array(U[:,:k])
    Ek = np.diag(E[:k])
    Vk = np.array(V[:k,:])
    return Uk@Ek@Vk

#Getting the file into the array and the resolution
FILE_NAME = 'lena_gray.bmp'
RESOLUTION = 512
IMG = np.asarray(Image.open('lena_gray.bmp'))

#arrays needed to draw a plot
Ks = []
differences = []

#drawing the photo with k = 16, 32, ..., 512 first significant elements using low rank approximation
for k in range(16, RESOLUTION + 1, 16):
    Ks.append(k)
    #getting new compresed array
    compressedArray = lowRankAprox(IMG, k)
    compressedIMG = Image.fromarray(compressedArray).convert("RGB")
    compressedIMG.save("result_" + str(k) + ".jpg")

    #getting compresed array of difference between original picture and ours
    compressedArray = np.subtract(IMG, compressedArray)
    differences.append(np.linalg.norm(compressedArray))
    compressedIMG = Image.fromarray(compressedArray).convert("RGB")
    compressedIMG.save("difference_result_" + str(k) + ".jpg")


#plot
plt.plot(Ks, differences)
plt.title('Relation between k and substraction of IMG matrix and low rank approximation')
plt.show()
