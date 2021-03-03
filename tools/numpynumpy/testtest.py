import numpy as np


#
# # a = np.arange(30).reshape((3,10))
# # print(np.array_split(a,4,axis=1))
#
# # print(5.5%2)
#
# l1 = [2,3,4]
# l2 = l1
#
# l1[1] = 8
# print(l2)
#
# # s1 = 'asd'
# # s2 = s1
# # s1 = s1+'123'
# # print(s1)
#
# # t1 = (1,2,3)
# # t2 = t1
# # t1[1] = 7
#
# d1 = {1:'a',2:'b'}
# d2 = d1
# d1[2] = 'c'
# print(d2)

# print(np.arange(10))
# print(3)

def testclip():
    np.random.seed(1)
    arr = np.arange(30).reshape(10, 3)
    print(arr)
    arr1=arr[:, 0:2]
    arr2=arr[:, 2:]   # 这种拿出来是二维的

    print(arr2[3], arr1[3])


if __name__ == '__main__':
    testclip()
