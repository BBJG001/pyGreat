# import re
#
# str = 'code // annotation'
#
# # ret = re.findall('o', str)  # 返回所有满足匹配条件的结果,放在列表里
# ret = re.findall('\/\/[^\n]*', str)  # 返回所有满足匹配条件的结果,放在列表里，不明白这里为什么要对斜杠（/）转义
# # [^\n]*    匹配不是（^）换行符（\n）的任意字符若干次（*）
# ret2 = re.sub('\/\/[^\n]*', '', str)
# print(ret2)
# # print('\/\/')

ll = [1, 3, 5, 3, 4, 3]
for i in ll[:]:

    if i==3:
        ll.remove(i)
    if i==5:
        break

print(ll)