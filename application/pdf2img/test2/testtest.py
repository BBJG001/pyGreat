# coding=gbk
import os

output_path = '//test2/cameraSR/1__�ǳ���4Dʱ����ֳ����µ��¿���Ա��ȫ��ɢ�о�_¬��.pdf'
path = r'C:\Users\Administrator\Desktop\�½��ļ���\123'
# print(output_path.rsplit('/', 1))
# print(path.rsplit('\\', 1))
# print(output_path.split('.')[0])
print(list(range(1)))
# print(output_path[:output_path.rfind('.')])
# print(os.listdir(output_path))
# print(os.path.dirname(output_path))

# picture_path = output_path[:output_path.rfind('.')]

# fl = [os.path.join(output_path, fn) for fn in os.listdir(output_path)]
# print(fl)
#

# endn = 100
# n = int(100 / 30)
# for i in range(n+1):
#     print(list(range(i * 30, i*30+30))) if i < n else print(list(range(i * 30, endn+1)))

# if not os.path.exists(path):
#     os.mkdir(path)

for fn in os.listdir(r'/test2/cameraSR'):
    print(fn)
