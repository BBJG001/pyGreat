from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread        # 代替scipy下的

# 读入一个txt文件
text = open('articles.txt', 'r').read()

# 生成词云
wordcloud = WordCloud().generate(text)

# 读入图片
# bg_pic = imread('lyf.jpg')
bg_pic = imread('lyf.jpg')
# 配置词云参数
wc = WordCloud(
    # 设置字体
    # font_path = 'BeaverScratches.ttf',    # 这里字体报错
    # 设置背景色
    background_color='white',       # 词云生成在除这个背景色之外的其他位置
    # 允许最大词汇
    max_words=200,
    # 词云形状
    mask=bg_pic,
    # 最大号字体
    max_font_size=100,
)

# 生成词云
wc.generate(text)
# 保存图片
wc.to_file('word.jpg')