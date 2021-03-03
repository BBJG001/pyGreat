#-*- coding:utf-8 -*-
# from scipy.misc import imread
from matplotlib.pyplot import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from collections import Counter
from application.wordcloudwc.tools import *
# 读入文件，windows下过滤编码错误
# wdic = dicfromfile('wcinput.txt')
wdic = dicfromexcel('data/wcinput2019.xlsx')
# wdic = dicfromexcel('wcinput2020.xlsx')
# wdic = dicfromexcel('wcinputstep.xlsx')




# 配置词云参数
wc = WordCloud(
    # 设置字体
    font_path = 'C:/Windows/Fonts/STKAITI.TTF', background_color='white',
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
wc.to_file('./wdcd2019.jpg')