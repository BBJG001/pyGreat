import os

# 从指定path下递归获取所有文件
def getAllFile(path, fileList):
    dirList = []    # 存放文件夹路径的列表
    for ff in os.listdir(path):
        wholepath = os.path.join(path, ff)
        # wholepath = path+'/'+ff
        if os.path.isdir(wholepath):
            dirList.append(wholepath)   # 如果是文件添加到结果文件列表中

        if os.path.isfile(wholepath):
            fileList.append(wholepath)  # 如果是文件夹，存到文件夹列表中

    for dir in dirList:
        getAllFile(dir, fileList)   # 对于dirList列表中的文件夹，递归提取其中的文件，fileList一直在往下传，所有的文件路径都会被保存在这个列表中

# 从文件路径列表中筛选出指定后缀的文件
# 这里可以从源列表中删除 非后缀 项，也可以新建一个 后缀列表，遍历源列表向后缀列表中.append()后缀项
# 后者更容易一些，我这里选择了前者，还费劲解决了一波list循环remove的问题。。。
# list循环remove http://itdarcy.wang/index.php/20200109/381
def getSufFilePath(fileList, suffix):
    # print(len(fileList))
    for ff in fileList[:]:
        if not ff.endswith(suffix):
                fileList.remove(ff)

def getDocFilePath(fileList):
    # print(len(fileList))
    for ff in fileList[:]:
        if not ff.endswith('.doc') and not ff.endswith('.docx'):
            fileList.remove(ff)


if __name__ == '__main__':
    flist = []
    findpath = r'D:\BaiduNetdiskDownload\20套项目'
    getAllFile(findpath, flist)
    # print('allfile:', len(flist))
    # getSufFilePath(flist, '.doc')
    #
    # print('Docfile:', len(flist))
    # for ff in flist:
    #     print(ff)

    print('allfile:', len(flist))
    getDocFilePath(flist)

    print('Docfile:', len(flist))
    for ff in flist:
        print(ff)
