def selectsort(alist):
    n = len(alist)
    for i in range(n-1):
        index_min = i
        for j in range(i+1, n):
            if alist[j]<alist[index_min]:
                index_min = j
        alist[i], alist[index_min] = alist[index_min], alist[i]

if __name__ == '__main__':
    ll = [3,6,2,4,7,5,8,1,0]
    print(ll)
    selectsort(ll)
    print(ll)
