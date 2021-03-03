import matplotlib.pyplot  as plt
import numpy as np

from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure()
for x in np.linspace(-1,1,50):
    y = np.linspace(1,2-x**2, 40)
    x = np.tile(x, 50)
    plt.plot(x,y)

plt.show()