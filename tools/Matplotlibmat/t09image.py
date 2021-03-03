import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
# 九宫格，每个格点一个层次的颜色深度

# plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
plt.imshow(a, interpolation='bilinear', cmap=plt.get_cmap('rainbow'), origin='lower')
# interpolation可选值可参见 https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
# origin    可选值upper（左上->右下）、lower（左下->右上）

plt.colorbar(shrink=.92)    # 旁边的颜色条缩减

# 隐藏轴上的坐标
plt.xticks(())
plt.yticks(())

plt.show()