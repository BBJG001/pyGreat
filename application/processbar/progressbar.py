# format    https://www.runoob.com/python/att-string-format.html
import time

# # 打印进度条
# total = 198
# for i in range(80, 90):
#     print('这次的准确率是%.2f'%(i/total))
# # 对上面的一个改进
# for i in range(80, 90):
#     print('这次的准确率是%i%%'%(i/total *100))
#     # %i相当于为一个整形数占位，%i这个语法中，%作为一种转义字符，意思大概就是让i代整数，但是%作为转义字符了，要想输出%怎么办呢——%%
#     # print('这次的准确率是%.2f%%'%(i/total *100))

# # 打印进度条
# for i in range(total+1):
#     # print('\r当前核算进度 : %i%% [%i/%i]' % (i/total*100, i, total), end='')
#
#     print('\r当前核算进度 : %.2f%%\t' % (i/total*100), end='')
#     print('['+'>'*int(i/total*60)+'-'*int(60-i/total*60)+']', end='')
#     # ‘\r’的意思是让指针回到行首
#     # 其中'+'是被重载过的，就是根据参数的不同而调用不同的函数体，如果'+'两边是字符串，其功能就是进行字符串的拼接
#     # '*'也是重载过的，‘>’*5就等价于'>>>>>'
#     time.sleep(0.02)

def bar(now, total):
    print('\r[ %d / %d]' % (now, total), end='')
    # print('\r[ {} / {}]'.format(now, total), end='')

# [127 / 300]
def bar1(now, total, prefix='progress:'):
    size = len(str(total))
    # print('\r'+prefix+'[ %d / %d]' % (now , total), end='')
    # print('\r'+prefix+'[{} / {}]'.format(now, total), end='')
    print('\r'+prefix+'[{:>3d} / {}]'.format(now, total), end='')
    # https://www.runoob.com/python/att-string-format.html

# [32.38%]
def bar2(now, total, prefix='progress:'):
    print('\r'+prefix+'[ %.2f%% ]' % (now / total * 100), end='')

# progress: 70.71%	[>>>>>>>>>>>>>>>>>>>>>--------]
def bar3(now, total, length=30, prefix='progress:'):
    print('\r'+prefix+' %.2f%%\t' % (now / total * 100), end='')
    print('['+'>'*int(now/total*length)+'-'*int(length-now/total*length)+']', end='')


if __name__ == '__main__':
    all = 198

    for i in range(all):  # i属于[0, total)
        # bar(i+1, all)
        bar1(i+1, all)
        # bar2(i+1, all)
        # bar3(i+1, all, 60, '进度：')
        time.sleep(0.1)   # 为了更好的观察效果，稍微延时一下