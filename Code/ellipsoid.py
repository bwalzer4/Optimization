import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

# Let's set up the parameters to generate some points in R^2
n = 2
m = 50

# Randomly generate points normally distributed mean 20, and std dev 5

points = np.random.normal(20, 5, size = (m, n))


# Take a look at the points

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()
plt.scatter(points[:,0], points[:,1], marker = 'o')
plt.axis('scaled')
plt.xlabel('x', size = 20)
plt.ylabel('y', size = 20)
plt.xlim([0, 40])
plt.ylim([0, 40])
plt.savefig("random_points.png")
plt.show()

import cvxpy as cp

# Set up our variables A and b which we want to minimize

A = cp.Variable((n,n), symmetric = True)
b = cp.Variable((n,1))


# Set up the PSD constraint
constraints = [A >> 0]


# Generate m constraints where Ax-b <= 1 for each point

for i in range(m):
    constraints += [cp.norm(A @ points[i].reshape(2,1) - b, 2) <= 1]

# Set up our objective function
# -log det(a) = log det(a^-1)

obj = cp.Minimize(-cp.log_det(A))

prob = cp.Problem(obj, constraints)

prob.solve()
print("Status:", prob.status)
print("Objective Value:\n", prob.value)
print("Optimal Solution for A:\n", A.value) 
print("Optimal Solution for b:\n", b.value)

# Since Ac = b then c = A^{-1}b

c = np.linalg.inv(A.value) @ b.value
print('c: \n', c)


# Q = AA

Q = A.value @ A.value
print('Q: \n', Q)

# First we need to decompose Q, the shape matrix, into
# eigenvalues and eigenvectors.

eig_vals, eig_vectors = np.linalg.eig(Q)
print('Eigenvalues:' ,eig_vals)
print('Eigenvectors:', eig_vectors)

# Now we can use the eigenvalues of the shape matrix to find the
# horizontal and vertical diameters of the ellipsoid. The the 
# eigenvalues of Q are the reciprocals of the squares of the semi-axes
# (https://en.wikipedia.org/wiki/Ellipsoid#As_quadric).

h_diameter = eig_vals[np.argmax(eig_vals)]**(-1/2) * 2
v_diameter = eig_vals[np.argmin(eig_vals)]**(-1/2) * 2

print('Horizontal Diameter:', h_diameter)
print('Vertical Diameter:', v_diameter)

# Now using the Eigenvector that corresponds to the semi-major axis 
# (the axis with a greater diameter) we caclulate the angle between
# that eigenvector and the x-axis

semimaj_vec = eig_vectors[np.argmin(eig_vals)]

# The Numpy function arctan2 calculates the angle between a vector and
# the origin in radians

angle_rad = np.arctan2(semimaj_vec[0], semimaj_vec[1])

# Convert to degrees

angle_deg = (angle_rad*180)/np.pi

print('Angle:', angle_deg)

# We can use the matplotlib.patches class to plot the ellipsoid

from matplotlib.patches import Ellipse

plt.figure(figsize = (6,6))
ax = plt.gca()

# The Ellipse function takes the center of the ellipse, xy (c), the width length (horizontal diameter),
# the height length (vertical diamter), and the angle of the ellipse

ells = Ellipse(xy=c, width=h_diameter, height=v_diameter, angle=angle_deg, edgecolor='b', facecolor='none')

ax.add_patch(ells)
plt.scatter(points[:,0], points[:,1], marker = 'o')
plt.axis('scaled')
plt.xlabel('x', size = 20)
plt.ylabel('y', size = 20)
plt.xlim([0, 40])
plt.ylim([0, 40])
plt.savefig("ellipsoid.png")
plt.show()
