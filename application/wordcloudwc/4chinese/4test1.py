#-*- coding:utf-8 -*-
# from scipy.misc import imread
from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from collections import Counter
from application.wordcloudwc.tools import dicfromfile
# 读入文件，windows下过滤编码错误
text = open('data/4test.txt', encoding='utf-8', errors='ignore').read()
# 使用 jieba 分词
text_jieba = list(jieba.cut(text))
# 使用 counter 做词频统计，选取出现频率前 100 的词汇
c = Counter(text_jieba)
common_c = c.most_common(100)

# 读入图片
# bg_pic = imread('Anne_Hathaway.png')

# 配置词云参数
wc = WordCloud(
    # 设置字体
    font_path = 'C:/Windows/Fonts/STKAITI.TTF',
    # 设置背景色
    background_color='white',
    # 允许最大词汇
    max_words=200,
    # 词云形状
    # mask=bg_pic,
    # 最大号字体
    max_font_size=100,

    scale=2
)
# 生成词云
wc.generate_from_frequencies(dict(common_c))
# 生成图片并显示
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()
# 保存图片
wc.to_file('anne.jpg')