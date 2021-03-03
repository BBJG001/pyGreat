import matplotlib.pyplot as plt

plt.figure(figsize=(5.31,8.54))

plt.xlim(0.5, 13)
plt.ylim(0.9, 21)
# plt.axis('equal')
plt.axis('scaled')

for i in range(23):
    plt.plot((0,13.5),(i,i))
for j in range(14):
    plt.plot((j,j),(0,21.7))

plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)
plt.margins(0,0)

plt.savefig('../data/grid.png', pad_inches=0)

plt.show()
