from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

n = 5
x = np.linspace(1, n, 100)
# print(x)
y1 = np.log(x)
y2 = x
y3 = x*np.log(x)
y4 = x**2
y5 = [reduce(lambda x,y:x*y,range(1,k+1)) for k in range(1, n+1)]

plt.plot(x, y1, label='O(logn)')
plt.plot(x, y2, label='O(n)')
plt.plot(x, y3, label='O(nlogn)')
plt.plot(x, y4, label='x^2')
plt.plot(range(1, n+1), y5, label='n!')

plt.ylim(0, 40)
plt.legend()

plt.show()

