# 画棱柱
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from matplotlib import cm

#Create the profile
Radii = [1, 1.5, 1, 0.8, 1.3, 0.6, 0.5]
Zradii = [0, 1, 5, 10, 12, 14, 16]

radius = CubicSpline(Zradii, Radii, bc_type=((1, 0.5), (1, 0.0)))

# Make data
thetarange = np.linspace(0, 2 * np.pi, 100)
zrange = np.linspace(min(Zradii), max(Zradii),100)
X = [radius(z)*np.cos(thetarange) for z in zrange]
Y = [radius(z)*np.sin(thetarange) for z in zrange]
Z = np.array([[z] for z in zrange])

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(-2, 2)
ax.set_ylim3d(-2, 2)
ax.set_zlim3d(0, 20)
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)

#Plot the circles
for zz in Zradii:
    XX = radius(zz)*np.cos(thetarange)
    YY = radius(zz)*np.sin(thetarange)
    ax.plot(XX,YY,zz, lw=1, color='k')

plt.show();