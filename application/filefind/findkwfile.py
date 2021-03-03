from application.findfile.getallsub import getAllSub
from application.findfile.getallsub import getAllSub2


# 根据keyword从flist中筛选满足条件的文件/文件夹路径
def getkwfile(flist, keyword):
    res = []
    for ff in flist:
        if keyword in ff.split('\\')[-1]:  # 切分出文件名来再判断，可以缩短判断时间
            res.append(ff)
    return res


if __name__ == '__main__':
    path = r'E:\ZYD\temporary\DesktopMirror\ZL'
    keyword = 'doc'
    subList = getAllSub(path)[0] + getAllSub(path)[1]
    resList = getkwfile(subList, keyword)
    print(len(resList))
    print(resList)
