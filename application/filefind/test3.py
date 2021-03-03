import os
import re
import shutil

path = r'E:\ZYD\temporary\2019-2020上学期\英语\15篇文章贯通六级词汇'
outpath = r'E:\ZYD\temporary\2019-2020上学期\英语\15篇文章贯通六级词汇\articles'

flist = os.listdir(path)

restr = 'Unit.{2}'

# cataf = open(os.path.join(path, 'catalog.txt'), 'w')
for f in flist:
    fp = os.path.join(path, f)
    if not fp.endswith('.exe'):
        filelist = os.listdir(fp)
        for file in filelist:
            filepath = os.path.join(fp, file)
            shutil.copy(filepath, outpath)
            # if len(filepath)==62:
            #     newname = filepath[:-11]+'0'+filepath[-11:]
            #
            #     print(newname)
            #
            # substr = re.search(restr, filepath).group()
            # if substr.endswith('-'):
            #     print(substr[:-2]+'0'+substr[-2:])





    # print(f, file=cataf)

    # fl = f.split('.')
    # newname = 'P'+fl[0].zfill(3)+'.'.join(fl[1:-1])+'.mp4'
    # newpath = os.path.join(path, newname)
    # newpath = os.path.join(path, f[1:])


    # os.rename(fp, os.path.join(path, f.replace(' ','.')))

    # newname = f.split('：')[1][:-5]+'.mp4'
    #
    # newpath = os.path.join(path, newname)
    #
    # os.rename(fp, newpath)
    # print(f+' over')

# cataf.close()