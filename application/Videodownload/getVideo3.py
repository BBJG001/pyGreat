import os

# 需要一个支持的工具包，如果没有，就自动安装
retu = os.popen('you-get').read()
if not 'OPTION' in retu:
    print('安装支持插件ing，请稍后 . . .')
    os.system('pip install you-get')  # 安装you-get工具
    print('环境已OK！')
else:
    print('环境已OK！')


downlist=[]

# # 循环拼接搞网址，用的是bilibili的，它的网址比较单一化
# # https://www.bilibili.com/video/av16378934?p=1
# # 上面是它第一个教程的网址，多观察几个就发现，这些网址只有 p=n 只有这个n不同，所有的教程是1-18
downloadPath = r'https://www.bilibili.com/video/av87978495?p='
for page in range(1, 44):
    url = downloadPath + str(page)  # 这有点儿爬虫的意思，拼接url地址
    downlist.append(url)


# 手动搞网址，莫烦自己网站上的，网址比较个性化，不能批量化搞，一个个复制下来
# downlist = [
#     'https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/1-1-why/',
#     'https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-8-pd-plot/',
# ]

savePath = r'E:\Test\CNNWed2'   # 根据你的物理环境自行设定，不存在的话会自行创建这么一个文件夹
# 如果savePath不存在，就新建这么一个目录
if not os.path.exists(savePath):
    os.makedirs(savePath)

for i in range(0, len(downlist)):
    cmd = 'you-get ' + downlist[i] + ' -o ' + savePath
    os.system(cmd)

# 在我这里默认的分辨率看起来还蛮清晰，如果想要更高的分辨率，可以参看参考文献
'''
参考文献：
    https://www.zhihu.com/question/23805794
'''
