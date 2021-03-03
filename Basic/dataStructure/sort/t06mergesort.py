def mergesort(alist):
    n = len(alist)
    # 如果切分到最后一个，直接返回
    if n<=1:
        return alist
    mid = n//2  # 取整除

    # 获得左半部分和有半部分的合并结果
    sub_left = mergesort(alist[:mid])
    sub_right = mergesort(alist[mid:])

    # 定义左右指针
    left_pointer, right_pointer = 0, 0
    # 初始化本轮的归并结果
    result = []

    # 利用两个指针归并当前两个左右子序列
    while left_pointer<len(sub_left) and right_pointer<len(sub_right):
        if sub_left[left_pointer] < sub_right[right_pointer]:
            result.append(sub_left[left_pointer])
            left_pointer += 1
        else:
            result.append(sub_right[right_pointer])
            right_pointer += 1
    # 其中一个指针到头之后（pointer指在最后，[pointer:]就是一个空列表），
    # 将另一个子序列的剩余部分加到结果中
    result += sub_left[left_pointer:]
    result += sub_right[right_pointer:]

    return result

if __name__ == '__main__':
    ll = [3,6,2,4,7,5,8,1,0,9]
    print(ll)
    ll = mergesort(ll)
    print(ll)