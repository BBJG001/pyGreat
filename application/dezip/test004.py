# python获取大小写字母、数字，各种字符

# # 通过string模块获得
import string  # 导入string这个模块
#
print(string.digits)            # 输出包含数字0~9的字符串
print(string.ascii_letters)     # 包含所有字母(大写或小写)的字符串
print(string.ascii_lowercase)   # 包含所有小写字母的字符串
print(string.ascii_uppercase)   # 包含所有大写字母的字符串
print(string.punctuation)       # 包含所有标点的字符串


# # 通过ascii码表获得
# print([chr(i) for i in range(65, 91)])    # 所有大写字母
# print(''.join([chr(i) for i in range(65, 91)]))    # 所有大写字母
# print([chr(i) for i in range(97, 123)])   # 所有小写字母
# print([chr(i) for i in range(48, 58)])    # 所有数字

# l_letter = list(string.ascii_letters)
# l_digitsl = list(string.digits)
# l_punctation = list(string.punctuation)
#
# ll = l_letter+l_digitsl+l_punctation
#
# def getkeys():
#     for i in ll:
#         for j in ll:
#             for k in ll:
#                 yield (str(i)+str(j)+str(k))    # 这是个迭代器
#
# keys = getkeys()
# for k in keys:      # 这个k相当于xx.__next__()
#     print(k)
#
# # 还是多进程有效果，测试的多线程效果跟串行差不多
# def multicore():
#     pool = mp.Pool(processes=6)

print(chr(65))
