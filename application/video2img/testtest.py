# import os
#
# p1 = r'E:\Test\v2idemo.flv'
# p2 = 'E:\\Test\\v2idemo.flv'
# p3 = 'E:/Test/v2idemo.flv'
# path = r'E:\Test\v2idemo.flv'
#
# # print(p1.split('\\'))
# # print(p2.split('\\'))
# # print(p1.split('\\'))
# filename = path.split(os.sep)[-1].split('.')[0]
# print(filename)

# print('s'.zfill(3))
# print('s'.rjust(3, '0'))
#
# plist = path.split(os.sep)
# print(plist)
# filename = plist[-1].split('.')[0]
# print(filename)
#
#
# print(p1.split(os.sep))
# print(p2.split(os.sep))
# print(p1.split(os.sep))
#
# print(os.sep)

import os

path = r'E:\Test'
filelist = os.listdir(path)
for fi in filelist:
    if fi.endswith('.mp4'):
        video2img1(fi)