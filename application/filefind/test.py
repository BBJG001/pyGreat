import os

path = r'C:\Users\Administrator\Desktop\实验室设备管理系统'
ll = os.listdir(path)
ll2 = [os.path.join(path, fp) for fp in ll]
# ll2 = ll

# for i in range(len(ll2)):
#     fi = ll2[i]
#     if not fi.endswith('.doc') and not fi.endswith('.docx'):
#         print(fi)
#         ll2.remove(fi)
#         i-=1

# ll2_ = ll2
# ll3 = [v for v in ll2]
# print(id(ll2))
# print(id(ll2_))
# print(id(ll3))
# print(id(ll2[:]))

for ff in ll2[:]:
    if not ff.endswith('.doc') and not ff.endswith('.docx'):
        print(ff)
        ll2.remove(ff)

print(ll2)
print(os.path.join('D:/test', 'test2'))
print('2020R11L036358打印预览_files'.endswith('.doc'))
print('2020R11L036358打印预览_files'.endswith('.docx'))

