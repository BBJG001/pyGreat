# !/usr/bin/python
# -*- coding:utf-8 -*-

from gensim import corpora, models, similarities
from pprint import pprint

# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


if __name__ == '__main__':
    f = open('22.LDA_test.txt')
    stop_list = set('for a of the and to in'.split())   #造了一波停止词
    # texts = [line.strip().split() for line in f]
    # pprint(texts) #pprint()打印的好看一些
    texts = [[word for word in line.strip().lower().split() if word not in stop_list] for line in f]    #去停止词
    print('Text = ')
    pprint(texts)

    dictionary = corpora.Dictionary(texts)  #制作词典
    V = len(dictionary)
    corpus = [dictionary.doc2bow(text) for text in texts]   # 通过词典做成词包向量，基于出现次数（1，4）第一个词出现4次
    corpus_tfidf = models.TfidfModel(corpus)[corpus]    # 制作带权值的词包向量（1，0.25）

    print('TF-IDF:')
    for c in corpus_tfidf:
        print(c)

    print('\nLSI Model:')
    lsi = models.LsiModel(corpus_tfidf, num_topics=2, id2word=dictionary)   # 两个主题，传入词典
    topic_result = [a for a in lsi[corpus_tfidf]]
    pprint(topic_result)
    print('LSI Topics:')
    pprint(lsi.print_topics(num_topics=2, num_words=5)) # 只取前5个词
    similarity = similarities.MatrixSimilarity(lsi[corpus_tfidf])   # similarities.Similarity()，把主题模型喂进去计算相似度
    print('Similarity:')
    pprint(list(similarity))

    print('\nLDA Model:')
    num_topics = 2
    lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dictionary,  # 可以直接放预料，也可以放tfidf处理过的带权值的语料，aerf、贝塔，如果某个主题的算出来权值小于0.001这一项就不要了
                          alpha='auto', eta='auto', minimum_probability=0.001)
    doc_topic = [doc_t for doc_t in lda[corpus_tfidf]]
    print('Document-Topic:\n')
    pprint(doc_topic)
    for doc_topic in lda.get_document_topics(corpus_tfidf):
        print(doc_topic)
    for topic_id in range(num_topics):
        print('Topic', topic_id)
        # pprint(lda.get_topic_terms(topicid=topic_id))
        pprint(lda.show_topic(topic_id))
    similarity = similarities.MatrixSimilarity(lda[corpus_tfidf])
    print('Similarity:')
    pprint(list(similarity))
    # LDA在短文档中不见得是好的
    hda = models.HdpModel(corpus_tfidf, id2word=dictionary) # 不放tfidf，直接放语料也是可以的
    topic_result = [a for a in hda[corpus_tfidf]]
    print('\n\nUSE WITH CARE--\nHDA Model:')
    pprint(topic_result)
    print('HDA Topics:')
    print(hda.print_topics(num_topics=2, num_words=5))
