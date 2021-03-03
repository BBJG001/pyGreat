import os
from application.filefind.getallsub import getAllSub

# fl = getAllSub(r'E:\ZYD\temporary\DesktopMirror\ZL')[1]
# for ff in fl:
#     print(ff)
#     print(ff.split('\\')[-1])
# print(fl)

# l1 = ['a', 'b']
# l2 = ['c']
# print(l1+l2)

dl, fl = getAllSub(r'C:\Users\Administrator\Desktop\新建文件夹 (4)')
# for ff in fl:
#
#     newname = ff[:-28]+ff[-4:]
#
#     print(newname)
#
#     os.rename(ff, newname)

for dd in dl:
    print(dd.split('\\')[-1])
