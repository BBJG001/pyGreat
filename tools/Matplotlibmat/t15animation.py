from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10.0))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

# ani = animation.FuncAnimation(fig=fig,
#                               func=animate,
#                               frames=100,
#                               init_func=init,
#                               interval=20,
#                               blit=False)

ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=100,
                              init_func=init,
                              interval=20,
                              blit=False)

plt.show()

ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])