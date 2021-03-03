# 导入 wordcloud 模块和 matplotlib 模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ---------------------------- 通过文件 -------------------------------
# # 读入一个txt文件
# text = open('articles.txt', 'r').read()
#
# # 生成词云
# wordcloud = WordCloud().generate(text)

def dicfromfile(path):
    text_dict = {}
    with open(path) as f:
        for line in f:
            cell = line.split(' ')
            text_dict[str(cell[0])] = int(cell[1])
    return text_dict

# print(dicfromfile('wcinput.txt'))

wordcloud = WordCloud().generate_from_frequencies(dicfromfile('wcinput.txt'))


# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
# 保存图片
wordcloud.to_file('test.jpg')