import os
<<<<<<< HEAD
from application.filefind.getallsub import getAllSub

path = '/Users/baibianjingang/Downloads/thumbnail-service-rs-master'
=======
from application.findfile.getallsub import getAllSub

path = r'D:\Anaconda3\envs'
>>>>>>> dev2
dl, fl = getAllSub(path)
ll = dl+fl
print(len(ll))
for il in ll:
    # print(il)
    fname = il.split('\\')[-1]
    # print(fname)
<<<<<<< HEAD
    if 'gen' in fname:
=======
    if 'pyinstaller' in fname:
>>>>>>> dev2
        print(il)
