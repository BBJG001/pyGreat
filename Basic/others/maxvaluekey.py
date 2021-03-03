ll = [3, 8, 5, 7, 2, 4]
print(ll.index(max(ll)))    # 获得列表最大值索引
# 1
print(ll.index(min(ll)))
# 4

dd = {'key33':33, 'key44':44, 'key77':77, 'key22':22}
print(max(dd, key=dd.get))  # 获得字典最大值的key
# key77
print(min(dd, key=dd.get))
# key22

# 当不止一个最大值时
ll2 = [3, 8, 5, 7, 8, 2, 4]
print(ll2.index(max(ll2)))
# 1
dd2 = {'key33':33, 'key44':44, 'key77':77, 'key22':22, 'key77_':77}
print(max(dd2, key=dd2.get))
# key77