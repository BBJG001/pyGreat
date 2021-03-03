def insertsort(alist):
    n = len(alist)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if alist[j]<alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
            else:
                break   # 这么做可以省一些步数，因为前一部分已经是有序的了，一旦发现比前面大了，就没必要再万千比较了

if __name__ == '__main__':
    ll = [3,6,2,4,7,5,8,1,0]
    print(ll)
    insertsort(ll)
    print(ll)