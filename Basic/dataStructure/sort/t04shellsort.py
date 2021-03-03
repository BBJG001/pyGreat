def shellsort(alist):
    n = len(alist)
    gap = n//2  # 5/2=2.5   5//2=2  取整

    while gap >= 1:
        # 这样同时执行几个子序列排序的方式就比较好写，可以直接写成rang（gap，n）
        # 内部就跟插入排序是一样的
        for i in range(gap, n):
            j = i
            while j>0:
                if alist[j]<alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                    j -= gap
                else:
                    break
        # 缩短gap
        gap //= 2
        # for j in range(i, , -gap)
        #     if alist[j]<alist[j-gap]:
        #         alist[j], alist[j-gap] = alist[j-gap], alist[j]
        #     else:
        #         break

if __name__ == '__main__':
    ll = [3,6,2,4,7,5,8,1,0,9]
    print(ll)
    shellsort(ll)
    print(ll)