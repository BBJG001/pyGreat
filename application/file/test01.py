# 方式1
with open('data/test01.txt', encoding='utf8') as f:
    wordlist1 = f.read().split('\n')     # .read()获得所有内容； .split('\n')按'\n'分割成列表
print(wordlist1)
# ['123', 'zhang', '王', '李钊']
# 注：这种情况如果最后一行是一个空行，列表中会有一个空字符''

# 方式1
with open('data/test01.txt', encoding='utf8') as f:
    wordlist2 = f.read().splitlines()     # .read()获得所有内容； .splitlines()按'\n'分割成列表
print(wordlist2)
# ['123', 'zhang', '王', '李钊']

# 方式2
wordlist3 = []
with open('data/test01.txt', encoding='utf8') as f:
    for line in f.readlines():  # readlines()的结果['123\n', 'zhang\n', '王\n', '李钊']
        wordlist3.append(line.strip('\n'))   # strip('\n')去掉字符串中的'\n'
print(wordlist3)
# ['123', 'zhang', '王', '李钊']

# 方式3
wordlist4 = []
with open('data/test01.txt', encoding='utf8') as f:
    for line in f:
        wordlist4.append(line.strip('\n'))
print(wordlist4)
# ['123', 'zhang', '王', '李钊']

