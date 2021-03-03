# 导入 wordcloud 模块和 matplotlib 模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ---------------------------- 通过文件 -------------------------------
# # 读入一个txt文件
# text = open('articles.txt', 'r').read()
#
# # 生成词云
# wordcloud = WordCloud().generate(text)

# ----------------------------- 自定义字典 ------------------------------
# 读入一组词频字典文件
text_dict = {
    'you': 2993,
    'and': 6625,
    'in': 2767,
    'was': 2525,
    'the': 7845,
}
wordcloud = WordCloud().generate_from_frequencies(text_dict)


# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
# 保存图片
wordcloud.to_file('test.jpg')