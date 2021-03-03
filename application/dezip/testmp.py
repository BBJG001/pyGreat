import multiprocessing as mp
import string  # 导入string这个模块
import zipfile
import time

l_letter = list(string.ascii_letters)
l_digitsl = list(string.digits)
l_punctation = list(string.punctuation)

# ll = l_letter+l_digitsl+l_punctation
ll = l_letter+l_digitsl
# ll = l_digitsl

# def getkeys():
#     for i in ll:
#         for j in ll:
#             for k in ll:
#                 yield (str(i)+str(j)+str(k))    # 这是个迭代器

def getkeys(i):
    kl = []

    for j in ll:
        for k in ll:
            # yield (str(i)+str(j)+str(k))  # 这是个生成器
            kl.append(str(i)+str(j)+str(k))
    return kl

# keys = getkeys()
# for k in keys:      # 这个k相当于xx.__next__()
#     print(k)

def job(keys):
    zFile = zipfile.ZipFile(r'E:\Test.zip')
    for k in keys:
        try:
            zFile.extractall(pwd=bytes(k, 'utf8'))
            print("Found Passwd:", k)
            return k
        except:
            pass


# 还是多进程有效果，测试的多线程效果跟串行差不多
def multicore():
    ts = time.time()
    pool = mp.Pool()
    stop = mp.Event()
    # res = pool.map(job, [getkeys(i) for i in ll])
    # print(res)
    multi_res = [pool.apply_async(job, (getkeys(i).__iter__())) for i in ll.__iter__()]
    # for res in multi_res:
    #     if not res==None:
    #         print(res)
    print([res.get() for res in multi_res])
    te = time.time()
    print('t_multicore:', te-ts)

def normal():
    ts = time.time()
    for i in ll:
        if not job(getkeys(i))==None:
            te = time.time()
            print('t_normal:', te - ts)
            return
    te = time.time()

def testextract():
    zFile = zipfile.ZipFile(r'E:\Test.zip')
    k = '123'
    # zFile.extractall(pwd=bytes(k, 'utf8'))
    # # zFile.extractall(pwd=k.encode('utf-8'))
    # print("Found Passwd:", k)
    # return k

    try:
        # zFile.extractall(pwd=bytes(k, 'utf8'))
        zFile.extractall(pwd=k.encode('utf-8'))
        print("Found Passwd:", k)
        return k
    except:
        pass

if __name__ == '__main__':
    multicore()

    # normal()

    # print(testextract())

    # for i in getkeys(3):
    #     print(type(i))
    #     print(i)
