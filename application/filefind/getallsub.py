import os

# 方式一，使用os.walk(path)方法
def getAllSub(path):
    Dirlist = []
    Filelist = []
    for home, dirs, files in os.walk(path):
        # 获得所有文件夹
        for dirname in dirs:
            Dirlist.append(os.path.join(home, dirname))
        # 获得所有文件
        for filename in files:
            Filelist.append(os.path.join(home, filename))
    return Dirlist, Filelist

# 方式二，通过递归调用一层层获取
def getAllSub2(path, dirlist=[], filelist=[]):
    flist = os.listdir(path)
    for filename in flist:
        subpath = os.path.join(path, filename)
        if os.path.isdir(subpath):
            dirlist.append(subpath)
            getAllSub2(subpath, dirlist, filelist)
        if os.path.isfile(subpath):
            filelist.append(subpath)
    return dirlist, filelist

# 根据keyword从flist中筛选满足条件的文件/文件夹路径
def getkwfile(flist, keyword):
    res = []
    for ff in flist:
        if keyword in ff.split('\\')[-1]:  # 切分出文件名来再判断，可以缩短判断时间
            res.append(ff)
    return res

def getSuffile(fileList, suffix):
    resList = []
    for ff in fileList:
        if ff.endswith(suffix):
            resList.append(ff)
    return resList

def getSuffile2(fileList, suffix):      # 这个2看起来不用生成一个新变量，好像会省空间
    # print(len(fileList))
    for ff in fileList[:]:
        if not ff.endswith(suffix):
                fileList.remove(ff)


def getAllbySuf(path, suffix):
    pass

def getAllbykw(path, keyword):
    pass

if __name__ == "__main__":
    path = r'E:\ZYD\temporary\DesktopMirror\ZL\软著\实验室设备管理系统'
    # # Dirlist, Filelist = getAllSub(path)
    # Dirlist, Filelist = getAllSub2(path)
    # print(Dirlist)
    # print(Filelist)


