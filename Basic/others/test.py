import numpy as np
import matplotlib.pyplot as plt

lx = [0,3,10,12,4,1,2,8,2]
ly = [1]*9
for i in range(1,len(lx)):
    lx[i]+=lx[i-1]

print(lx)
print(ly)
plt.figure(figsize=(15, 2))
plt.plot(lx,ly,"b",linewidth=3,marker=2)
plt.show()
