def binarysearch(alist, item):
    '''二分查找_递归实现'''
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binarysearch(alist[:mid], item)
        else:
            return binarysearch(alist[mid + 1:], item)
    return False


def binarysearch(alist, item):
    '''二分查找_非递归查找'''
    n = len(alist)
    begin = 0
    end = n - 1
    while begin <= end:
        mid = (begin + end) // 2
        if alist[mid] == item:
            return True
            # return mid    # 即所找值的索引
        elif alist[mid] > item:
            end = mid - 1
        else:
            begin = mid + 1
    return False


if __name__ == '__main__':
    ll = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(ll)
    print(binarysearch(ll, 6))
