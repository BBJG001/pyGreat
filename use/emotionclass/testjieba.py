import jieba

with open('data.txt', encoding='utf8') as f:
    sentenceslist = f.read().splitlines()   # 读取文档按行生成列表
    # ['1.sentences：可以是一个List，对于大语料集，建议',
    # '2.sg： 用于设置训练算法，默认为0，对应CBOW算法',
    # '3.size：是指输出的词的向量维数，默认为100。',
    # ...]

# 只需要调用jieba.cut(str)就可以将str进行分词，返回在一个列表中
res = [list(jieba.cut(sent)) for sent in sentenceslist]
# [['1', '.', 'sentences', '：', '可以', '是', '一个', 'List', '，', '对于', '大', '语料', '集', '，', '建议'],
# ['2', '.', 'sg', '：', ' ', '用于', '设置', '训练', '算法', '，', '默认', '为', '0', '，', '对应', 'CBOW', '算法'],
# ['3', '.', 'size', '：', '是', '指', '输出', '的', '词', '的', '向量', '维数', '，', '默认', '为', '100', '。'],
# ...]]

print('I love you'.split(' '))
# ['I', 'love', 'you']