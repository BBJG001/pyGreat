def quicksort(alist, begin, end):
    if begin>=end:
        return
    mid_value = alist[begin]
    low = begin
    high = end

    # 对确定本轮迭代中mid_value在alist[begin： end]中的位置
    while low < high:
        # 左移
        while low < high and alist[high] >= mid_value:
            # 在思想上，将mid_value就当做一个分界线，如果有相同的mid_value，尽量把这些相同值放在同一侧，这里选择了放在左侧
            high -= 1
        alist[low] = alist[high]
        # low += 1  # 宁可多加一步比较，写在这里会让小指针与大指针错过
        # 右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        # high -= 1
    # 从循环退出时，low=high
    alist[low] = mid_value

    # 对左右两部分再递归进行快速排序
    # quicksort(alist[:low])    # 这么传参是不对滴，切片会生成一个新的list，这样只是对新的list做排序，不会返回到原list中
    # quicksort(alist[low+1:])  # 所以对函数进行了整体改动，加入了传入了其实终止值

    # 对mid_value(确定位置后)左边进行quicksort
    quicksort(alist, begin, low-1)
    # 对mid_value(确定位置后)右边进行quicksort
    quicksort(alist, low+1, end)

if __name__ == '__main__':
    ll = [3,6,2,4,7,5,8,1,0,9]
    print(ll)
    quicksort(ll, 0, len(ll)-1)
    print(ll)
