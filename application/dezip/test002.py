import sys, zipfile, rarfile, threading, time
import getopt, tkinter, datetime, os, subprocess
from tkinter import filedialog

###输入压缩文件
print("选择要解压的文件")
path = filedialog.askopenfilename()
while os.path.splitext(path)[-1] not in ['.rar', '.zip'] and path != "":
    print("文件个是不是rar或者zip,重新选择")
    path = filedialog.askopenfilename()
filename = os.path.split(path)[-1]
print("文件名为" + filename)
fileType = os.path.splitext(path)[-1]
if fileType == '.rar':
    print('这是一个rar类型的压缩文件')
    fileGet = rarfile.RarFile(path)
    if fileGet.needs_password() == False:
        print("【文件没有密码】")
    else:
        print('RAR 有问题，解决不了')

elif fileType == '.zip':
    print('这是一个 "zip" 类型的压缩文件')
    fileGet = zipfile.ZipFile(path)
    is_encrypted = fileGet.infolist()[0].flag_bits & 0x1
    if is_encrypted == 0:
        print("【文件没有密码】")

###选择解压字典
print("选择一个字典文件夹")
pwdDirfile_path = filedialog.askdirectory()
pwdDirfile_list = [file for file in os.listdir(pwdDirfile_path) if file[-4:] in ['.txt', '.TXT']]

j = 1
realpassword = ""


def GETthePWD(pwdDirfile, fileGet):
    global realpassword
    global j
    # print('当前跑的字典是: "%s"'%pwdDirfile)
    pwdfile = open(pwdDirfile_path + '\\' + pwdDirfile)
    pwdList = pwdfile.readlines()
    pwdfile.close()
    for pwd in pwdList:
        try:
            password = pwd.strip("\n")
            fileGet.extractall(pwd=password.encode())
            realpassword = password
            realpasswordfile = open(os.path.split(path)[0] + "\\密码.txt", "a")
            realpasswordfile.write("文件名: %s\n密码 : %s\n\n" % (password, filename))
            realpasswordfile.close()
            break
        except:
            # print("search count : %d,test password : %s, err:%s" % (j, password, sys.exc_info()[0]))
            # print("search count : %7d test password : %s"%(j, password),end="\n")
            print("测试了 %d 次" % j, end="\r")
            j = j + 1
            if realpassword != "":
                break


funNum = eval(input("输入想要同时跑的字典数,注意在电脑承受范围内，不要太大\n>>> "))
STARTtime = time.time()
while pwdDirfile_list != []:
    TASK = []
    FILEGET = []
    for i in range(funNum):
        FILEGET.append(zipfile.ZipFile(path))

    m = 0
    for i in pwdDirfile_list[:funNum]:
        TASK.append(threading.Thread(target=GETthePWD, args=(i, FILEGET[m])))
        m += 1
    for task in TASK:
        task.start()
    for task in TASK:
        task.join()
    for i in pwdDirfile_list[:funNum]:
        pwdDirfile_list.remove(i)
    if realpassword != "":
        print("跑了 %d 次" % j)
        print("search count : %d,real password is : %s               " % (j, realpassword))
        break
ENDtime = time.time()
print(ENDtime - STARTtime)
time.sleep(300)
