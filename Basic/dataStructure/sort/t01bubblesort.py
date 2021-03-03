def bubbltsort(alist):
    n = len(alist)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

if __name__ == '__main__':
    print(list(range(9,0,-1)))
    ll = [3,6,2,4,7,5,8,1,0]
    print(ll)
    bubbltsort(ll)
    print(ll)
