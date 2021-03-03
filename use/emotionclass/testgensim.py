from gensim.models import word2vec
import logging

# 用来打印日志
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 这样传入会把list的每个元素字符串拆解掉，每个字母当做一个词来训练
sentences1 = ['this is a sentence', 'this is the second sentence']
# 传入的正确格式
sentences2 = [['this', 'is', 'a', 'sentence'], ['this', 'is', 'the', 'second', 'sentence']]
# 也可以是把文档中所有的词提取出来的长列表，但是要保证它是二维的
# 无需去重，因为Word2Vec建议训练模型时把词频考虑在内
sentences3 = [['this', 'is', 'a', 'sentence', 'this', 'is', 'the', 'second', 'sentence']]

# 模型构建
model = word2vec.Word2Vec(
    sentences2, sg=1, size=20, window=1,
    min_count=1, negative=3, sample=0.001, hs=1, workers=4
)
'''
Word2Vec参数说明
    1.sentences：可以是一个List，对于大语料集，建议使用BrownCorpus,Text8Corpus或LineSentence构建。
    2.sg： 用于设置训练算法，默认为0，对应CBOW算法；sg=1则采用skip-gram算法。
    3.size：是指输出的词的向量维数，默认为100。大的size需要更多的训练数据,但是效果会更好. 推荐值为几十到几百。
    4.window：为训练的窗口大小，8表示每个词考虑前8个词与后8个词（实际代码中还有一个随机选窗口的过程，窗口大小<=5)，默认值为5。
    5.alpha: 是学习速率
    6.seed：用于随机数发生器。与初始化词向量有关。
    7.min_count: 可以对字典做截断. 词频少于min_count次数的单词会被丢弃掉, 默认值为5。
    8.max_vocab_size: 设置词向量构建期间的RAM限制。如果所有独立单词个数超过这个，则就消除掉其中最不频繁的一个。每一千万个单词需要大约1GB的RAM。设置成None则没有限制。
    9.sample: 表示 采样的阈值，如果一个词在训练样本中出现的频率越大，那么就越会被采样。默认为1e-3，范围是(0,1e-5)
    10.workers:参数控制训练的并行数。
    11.hs: 是否使用HS方法，0表示: Negative Sampling，1表示：Hierarchical Softmax 。默认为0
    12.negative: 如果>0,默认值5,则会采用negative samping，用于设置多少个noise words
    13.cbow_mean: 如果为0，则采用上下文词向量的和，如果为1（default）则采用均值。只有使用CBOW的时候才起作用。
    14.hashfxn： hash函数来初始化权重。默认使用python的hash函数
    15.iter： 迭代次数，默认为5。
    16.trim_rule： 用于设置词汇表的整理规则，指定那些单词要留下，哪些要被删除。可以设置为None（min_count会被使用）或者一个接受()并返回RU·E_DISCARD,uti·s.RU·E_KEEP或者uti·s.RU·E_DEFAU·T的函数。
    17.sorted_vocab： 如果为1（defau·t），则在分配word index 的时候会先对单词基于频率降序排序。
    18.batch_words：每一批的传递给线程的单词的数量，默认为10000
'''
# 模型使用
print(model['sentence'])
# [-0.00286479 -0.02174874  0.01972866  0.00954327  0.0162768  -0.01666331
#   0.02029363  0.01125568 -0.02085656 -0.01663973 -0.00263778 -0.00698208
#   0.01800852 -0.0031168  -0.01798444  0.01557341  0.00888846 -0.00809331
#  -0.01056736  0.02072779]

# 保存模型
model.save('w2vtest.model')
# 模型加载
model2 = word2vec.Word2Vec.load('w2vtest.model')
# 模型使用
print(model2['sentence'])
# [-0.00286479 -0.02174874  0.01972866  0.00954327  0.0162768  -0.01666331
#   0.02029363  0.01125568 -0.02085656 -0.01663973 -0.00263778 -0.00698208
#   0.01800852 -0.0031168  -0.01798444  0.01557341  0.00888846 -0.00809331
#  -0.01056736  0.02072779]