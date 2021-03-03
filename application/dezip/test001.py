# coding=UTF-8
"""
用字典暴力破解ZIP压缩文件密码
用户可以自己指定想要破解的文件和破解字典，多线程破解
"""
import zipfile
import threading
import optparse
# 用 extractall()这个函数抽取文件，密码正确则返回正确，密码错误测
# 抛出异常。
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print("Found Passwd:",password)
        return password
    except:
        pass

def main():
    parser=optparse.OptionParser('usage%prog -f <zipfile> -d <dictionary>')
    parser.add_option('-f',dest='zname',type='string',help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',help='specify dictionary file')
    options,args=parser.parse_args()
    if options.zname==None|options.dname==None:
        print(parser.usage)
        exit(0)
    else:
        zname=options.zname
        dname=options.dname
    zFile=zipfile.ZipFile(zname)
    dFile=open(dname,'r')
    for line in passFile.readlines():
        password=line.strip('\n')
        t=threading.Thread(target=extractFile,args=(zFile,password))
        t.start()

if __name__=="__main__":
    main()
