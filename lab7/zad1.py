import numpy as np
from numpy.linalg import svd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from copy import deepcopy

DENSITY = 200

# getting the [x, y, z] vectors needed for drawing it
def getSphere(N):
    s = np.random.uniform(0, 2*np.pi, N)
    t = np.random.uniform(0, np.pi, N)
    x = np.cos(s) * np.sin(t)
    y = np.sin(s) * np.sin(t)
    z = np.cos(t)
    return x, y, z

x, y, z = getSphere(DENSITY)
S = np.row_stack([x, y, z])

#generating random 3x3 matrices with values 0-1
A1 = np.random.uniform(0, 1, (3,3))
A2 = np.random.uniform(0, 1, (3,3))
A3 = np.random.uniform(0, 1, (3,3))

#getting our ellipses
ellip1 = A1 @ S
ellip2 = A2 @ S
ellip3 = A3 @ S

#svd
U1, E1, V1 = svd(A1)
U2, E2, V2 = svd(A2)
U3, E3, V3 = svd(A3)



#plot 1

axis1 = deepcopy(U1)
for i in range(len(axis1)):
    for j in range(len(axis1[i])):
        axis1[i][j] *= E1[j]

figure = plt.figure()
plot3D = figure.gca(projection='3d')
plot3D.scatter(x,y,z)
plot3D.scatter(ellip1[0], ellip1[1], ellip1[2], color="green")
plot3D.quiver(0, 0, 0, axis1[0], axis1[1], axis1[2], color="red")
plot3D.set_title("A1")
plt.show()

#plot 2

axis2 = deepcopy(U2)
for i in range(len(axis2)):
    for j in range(len(axis2[i])):
        axis2[i][j] *= E2[j]

figure = plt.figure()
plot3D = figure.gca(projection='3d')
plot3D.scatter(x,y,z)
plot3D.scatter(ellip2[0], ellip2[1], ellip2[2], color="green")
plot3D.quiver(0, 0, 0, axis2[0], axis2[1], axis2[2], color="red")
plot3D.set_title("A2")
plt.show()

#plot 3
axis3 = deepcopy(U3)
for i in range(len(axis3)):
    for j in range(len(axis3[i])):
        axis3[i][j] *= E3[j]

figure = plt.figure()
plot3D = figure.gca(projection='3d')
plot3D.scatter(x,y,z)
plot3D.scatter(ellip3[0], ellip3[1], ellip3[2], color="green")
plot3D.quiver(0, 0, 0, axis3[0], axis3[1], axis3[2], color="red")
plot3D.set_title("A3")
plt.show()

#100 > proportion plot
B = np.random.uniform(0,1,(3,3))
U, E, V = svd(B)
while E[0] < E[-1]*100:
    B = np.random.uniform(0,1,(3,3))
    U, E, V = svd(B)

ellipse = B @ S

#plot 4
##
# works properly cuz form the one dimension perspective,
# the ellipse looks flat, because of the singular values ratio
##
figure = plt.figure()
plot3D = figure.gca(projection='3d')
plot3D.scatter(ellipse[0], ellipse[1], ellipse[2], color="green")
plot3D.set_title("Task 4")
plt.show()

#task 5
B = np.random.uniform(0,1,(3,3))
U, E, V = svd(B)
#SV
ellipse1 = V @ S
#SEV
ellipse2 = (V * E) @ S
#SUEV
ellipse3 = (V * E) @ U @ S

figure = plt.figure()
plot3D = figure.gca(projection='3d')
plot3D.scatter(ellipse1[0], ellipse1[1], ellipse1[2], color="green")
plot3D.set_title("SV")
plt.show()

figure = plt.figure()
plot3D = figure.gca(projection='3d')
plot3D.scatter(ellipse2[0], ellipse2[1], ellipse2[2], color="green")
plot3D.set_title("SEV")
plt.show()

figure = plt.figure()
plot3D = figure.gca(projection='3d')
plot3D.scatter(ellipse3[0], ellipse3[1], ellipse3[2], color="green")
plot3D.set_title("SUEV")
plt.show()
