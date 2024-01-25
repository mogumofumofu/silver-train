from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define coordinates
phi, theta = np.mgrid[0 : 2 * np.pi : 0.1, 0 : np.pi : 0.1]
x = np.cos(phi) * np.sin(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(theta)

# Plot the sphere
ax.plot_wireframe(x, y, z, color='k', rstride=2, cstride=2)
plt.show()