#-*- coding:utf-8 -*-
# from scipy.misc import imread
from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from collections import Counter
from application.wordcloudwc.tools import *
# 读入文件，windows下过滤编码错误


def main():
    namespace = [
        # '2019',
        # '2020',
        '2021'
    ]

    for ni in namespace:
        wdic = dicfromexcel('./data/wcinput{}.xlsx'.format(ni))
        wc = WordCloud(
            # 设置字体
            font_path = '/System/Library/fonts/PingFang.ttc', background_color='white',
            max_words=200, max_font_size=100,
            width=200, height=200, relative_scaling=1,
            scale=3
        )
        # 生成词云
        wc.generate_from_frequencies(wdic)
        # 生成图片并显示
        # plt.figure()
        plt.imshow(wc)
        plt.axis('off')
        plt.show()
        # 保存图片
        wc.to_file('./data/wdcd{}.jpg'.format(ni))

if __name__ == '__main__':
    main()