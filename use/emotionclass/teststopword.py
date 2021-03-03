from nltk.corpus import stopwords
import jieba
from zhon.hanzi import punctuation as zhonpun
from string import punctuation as engpun
import re

# 从nltk中获取英文停用词
stopwords1 = stopwords.words('english')
# ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

#
with open('../data/stopwords.txt', encoding='utf8') as f:
    stopwords2 = f.read().splitlines()

def clearn_str(string):
    # 写法失败
    # string = re.sub(r''+zhonpun, '', string)
    # string = re.sub(r''+str([engpun]), '', string)

    # 筛除掉中文标点
    string = re.sub(r'[＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､　、〃〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏﹑﹔·！？｡。 ]', '', string)
    # 筛除掉英文标点
    string = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', '', string)
    return string

# 读取一份测试文件
with open('data.txt', encoding='utf8') as f:
    sentenceslist = f.read().splitlines()   # 每行作为一个元素封装成列表
    # ['1.sentences：可以是一个List，对于大语料集，建议', '2.sg： 用于设置训练算法，默认为0，对应CBOW算法', '3.size：是指输出的词的向量维数，默认为100。']
preprocessed = [clearn_str(x) for x in sentenceslist]
print(preprocessed)

res = [list(jieba.cut(sent)) for sent in sentenceslist]     # 用jieba分词
# [['1', '.', 'sentences', '：', '可以', '是', '一个', 'List', '，', '对于', '大', '语料', '集', '，', '建议'], ['2', '.', 'sg', '：', ' ', '用于', '设置', '训练', '算法', '，', '默认', '为', '0', '，', '对应', 'CBOW', '算法'], ['3', '.', 'size', '：', '是', '指', '输出', '的', '词', '的', '向量', '维数', '，', '默认', '为', '100', '。']]
# 去停用词
for line in res:
    for cell in line[:]:    # line[:],深copy,避免因为循环删除跳过对某些想的筛选
        if cell in stopwords2:
            line.remove(cell)
# [['sentences', 'List', '语料', '集', '建议'], ['sg', ' ', '用于', '设置', '训练', '算法', '默认', 'CBOW', '算法'], ['size', '指', '输出', '词', '向量', '维数', '默认', '100']]
