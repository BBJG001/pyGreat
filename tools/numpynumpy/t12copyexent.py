import numpy as np

aa = np.arange(7)

print(aa.repeat([5], 0))
# [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 6 6 6 6 6]
print(aa.repeat([2,3]))

print(np.repeat([3,4],axis=1))

print(np.tile(aa, 4))