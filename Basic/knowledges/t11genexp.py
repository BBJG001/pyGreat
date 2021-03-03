# 列表推导式
l = [i for i in range(10)]
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([2*x for x in range(10)])
print([3*x**2+5*x+8 for x in range(10)])

#生成器表达式
g1 = (i for i in range(10))
print(g1)
# <generator object <genexpr> at 0x00000228C7A824C8>
for i in  g1:
    print(i, end=' ')
print()
# 0 1 2 3 4 5 6 7 8 9
# 注意这时候生成器g1已经被用完了，就是指针已经走到了末尾，无法再__next__()了

g2 = (i for i in range(10, 20))
print(g2)
# <generator object <genexpr> at 0x00000228C7A824C8>
print(list(g2))
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# 注意这时候生成器g2已经被用完了，就是指针已经走到了末尾，无法再__next__()了


# 括号不一样
# 返回的值不一样，生成器表达式几乎不占用内存

老母鸡=('鸡蛋%s'%i for i in range(10))   #生成器表达式
print(老母鸡)
for 蛋 in 老母鸡:
    print(蛋)

g = (i*i for i in range(10))    # 到此，表达式中的代码还一点儿没执行
g.__next__()    # 一个next支持for循环一轮