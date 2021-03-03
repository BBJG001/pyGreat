# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.figure(figsize=(8,6))
# a = np.arange(0.0,5.0,0.02)
# plt.xlabel('横轴：时间',fontproperties = 'SimHei',fontsize = 20)
# plt.ylabel('纵轴：振幅',fontproperties = 'SimHei',fontsize = 20)
# plt.plot(a,np.cos(2*np.pi*a),'r--')
# plt.show()

import matplotlib
import matplotlib.pyplot as plt


matplotlib.rcParams['font.family'] = 'SimHei'
plt.plot([3,1,4,5,2])
plt.xlabel("横轴（值）")
plt.ylabel("纵轴（值）")
plt.savefig('test2',dpi=600)
plt.show()