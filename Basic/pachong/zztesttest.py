# 1. 查看首页
# import requests
# from bs4 import BeautifulSoup
# import time
#
# testurl = 'https://blog.csdn.net/willow_zhu/article/details/104601533'
#
# def getnum():
#     res = requests.get(testurl)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     numspan = soup.find(name='span', attrs={'class': 'read-count'})
#     return int(numspan.text.split()[-1])
#
# ts = time.time()
# ns = getnum()
# print(ns)
# for i in range(100):
#     time.sleep(1)
#     print('\rthe No.{} test'.format(i+1), end='')
#     num = getnum()
#     if num != ns:
#         print('\n',num)
#         te = time.time()
#         print('interval time:', te-ts, 's')
#         break

# print([([1,2,3], 'a')]*3)

# dd = {'a':0}
# dd['a'] +=1
# print(dd)

# from multiprocessing import Process,Manager
# import time
#
# def func1(shareList,shareValue,shareDict,lock):
#     with lock:
#         for i in range(5):
#             shareValue.value+=1
#             time.sleep(1)
#         shareDict['a'] += 1
#         time.sleep(1)
#         shareDict[1]='1'
#         time.sleep(1)
#         shareDict[2]='2'
#         for i in range(len(shareList)):
#             shareList[i]+=1
#
# if __name__ == '__main__':
#     manager=Manager()
#     list1=manager.list([1,2,3,4,5])
#     dict1=manager.dict({'a':1})
#     array1=manager.Array('i',range(10))
#     value1=manager.Value('i',1)
#     lock=manager.Lock()
#     print(type(dict1))
#     proc=[Process(target=func1,args=(list1,value1,dict1,lock)) for i in range(20)]
#     for p in proc:
#         p.start()
#     for i in range(50):
#         time.sleep(1)
#         # print(list1)
#         # print(dict1)
#         # print(array1)
#         print(value1)
#     # for p in proc:
#     #     p.join()
#     for i in range(50):
#         time.sleep(1)
#         print(list1)
#         print(dict1)
#         print(array1)
#         print(value1)

i = 2
print(id(i))