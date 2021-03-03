import pickle
import os
import numpy as np
import jieba
import pandas as pd
import re

from gensim.models import word2vec

SEQUENCE_LENGTH = 10


# 本程序数据来自一次文本情感识别的比赛数据，数据是微博博文，总共220万余条。
# 数据进行了人工标注，将博文分为0其他 1喜欢 2伤心 3厌恶 4生气 5幸福  六种情感

# 数据太多了，用这个函数提取一部分来训练和测试
# 从原始数据中提取部分用来训练和测试，参数为结束和开始的下标
def getdata(begin, end, datapath):
    '''
    :param begin:
    :param end:
    :return:
    '''
    datafile = os.path.join('data', 'dataSource', 'data.csv')
    content = pd.read_csv(datafile, sep='\t', escapechar='\\')

    text = content['blogs']
    emotion = content['points']

    output_train = pd.DataFrame({'blogs': text[begin:end], 'points': emotion[begin:end]})
    output_train.to_csv(datapath, index=False)


# 去掉数据中的标点符号
def clean_str(string):
    '''
    :param string:
    :return:
    其中的标点分别取自zhon.hanzi.punctuation和string.punctuation
    '''
    string = re.sub(r'[＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､　、〃〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏﹑﹔·！？｡。 ]', '', string)
    string = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', '', string)

    return string


# 数据预处理（每个句子拆解成一个词列表）
def load_data_preprocess(path):
    content = pd.read_csv(path, escapechar='\\')
    with open('data/stopwords.txt', encoding='utf8') as f:
        stopwords = f.read().splitlines()

    # 分词
    x_text = content['blogs']
    x_text = [clean_str(sent) for sent in x_text]
    x_text = [list(jieba.cut(sent)) for sent in x_text]
    # 去除停用词
    for line in x_text:
        for cell in line[:]:
            if cell in stopwords:
                line.remove(cell)
    # 将输出生成矩阵
    y = np.array(content['points'])

    return [x_text, y]


# 填充句子，使所有句子长度等于sequence_length
# 确定一个padding size，固定句子向量的宽度，可以简单的调用keras.sequence来做
def pad_sentences(sentences, padding_word="<PAD/>", sequence_length=SEQUENCE_LENGTH):
    """
    :param sentences:
    :param padding_word:
    :return: padded_sentences
    """
    padded_sentences = []
    for i in range(len(sentences)):
        sentence = sentences[i]
        if sequence_length > len(sentence):
            num_padding = sequence_length - len(sentence)
            new_sentence = sentence + num_padding * [padding_word]  # 给不够长的句子空位补上<PAD/>这种符号
            padded_sentences.append(new_sentence)
        else:
            padded_sentences.append(sentence[:sequence_length])

    return padded_sentences


def do_data_helper():
    dp = r'data/data.csv'  # data path

    # 切取所有数据中的一部分来测试
    if not os.path.exists(dp):
        getdata(0, 10000, dp)

    # 预处理，去标点，句子拆分成词的列表（每个句子拆成一个词的列表），去停用词
    sentences, labels = load_data_preprocess(dp)  # 载入word_x，y
    print('preprocess demo res:\n', sentences[:50])

    # 把句子的列表补成等长的，过长的舍去多余的，不够长的填充一些字符，通常填充相同的无效字符，
    sentences_padded = pad_sentences(sentences)  # 补成定长句子
    print('padding demo res:\n', sentences_padded[0:2])

    # 构造生成词向量的模型
    if not os.path.exists('data/models/w2vmodel.model'):
        model = word2vec.Word2Vec(
            sentences_padded, sg=1, size=100, window=1,
            min_count=1, negative=3, sample=0.001, hs=1, workers=4
        )
        model.save('data/models/w2vmodel.model')
    else:
        model = word2vec.Word2Vec.load('data/models/w2vmodel.model')

    for i in range(len(sentences_padded)):
        newdata = np.array([np.array(model[word]) for word in sentences_padded[i]])
        sentences_padded[i] = newdata

    return np.array(sentences_padded), np.array(labels)  # 返回x，y


if __name__ == '__main__':
    x, y = do_data_helper()
    print(x)