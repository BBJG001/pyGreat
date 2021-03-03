# 一种写法
f = open(file='../data/test01.txt', mode='r', encoding='UTF-8')
# file：文件路径
# mode：文件操作模式，读、写、追加。。。
# encoding：文件的编码方式
print(f.read())
# test
# 测试
f.close()   # 文件操作完成之后需要手动close()

# 另一种写法,with结构
with open(file='../data/test01.txt', mode='r', encoding='UTF-8') as f:
    print(f.read())
    # test
    # 测试
# with的范围结束之后打开的文件就自主关闭了，无需手动关闭

################## 文件的读、写、追加
with open(file='../data/test01.txt', mode='r', encoding='UTF-8') as f:
    print(f.read())
    # test
    # 测试
with open(file='../data/test01.txt', mode='rb') as f:
    print(f.read())
    # b'test\r\n\xe6\xb5\x8b\xe8\xaf\x95'

# 写文件
with open(file='../data/test02.txt', mode='w', encoding='UTF-8') as f:
    f.write('test02\n测试02')
with open(file='../data/test03.txt', mode='wb') as f:
    f.write('test02\n测试02'.encode('utf8'))  # 既然是wb（以二进制）写入，就要给文本内容编码成二进制，直接传入文本会报错
    # 直接查看时候不会以二进制码显示

# 追加
with open(file='../data/test04.txt', mode='a', encoding='UTF-8') as f:
    # test04.txt
    # test04
    # 测试04
    f.write('测试04追加')
    # 如果mode='ab'，write的时候就要对内容encode()




# 绝对路径
# f = open('d:\模特主妇护士班主任.txt',mode='r',encoding='UTF-8')
# content = f.read()
# print(content)
# f.close()

#bytes ---->str
# f = open('模特主妇护士班主任',mode='r',encoding='utf-8')
# content = f.read()
# f.write('fjsdlk')
# f.close()

# f = open('模特主妇护士班主任',mode='rb',)
# content = f.read()
# print(content)
# f.close()
# f = open('log',mode='r+',encoding='utf-8')
# print(f.read())
# f.close()

# f = open('log',mode='r+b')
# print(f.read())
# f.write('大猛，小孟'.encode('utf-8'))
# f.close()



#对于w:没有此文件就会创建文件
f = open('../others/log1', mode='w', encoding='utf-8')
f.write('骑兵步兵哈佛IE未发生都我阿尔法慰问金')
f.close()

#先将源文件的内容全部清除，再写。
f = open('../others/log1', mode='w', encoding='utf-8')
f.write('附近看到类似纠纷')
f.close()


# f = open('log',mode='w+',encoding='utf-8')
# f.write('aaa')
# f.seek(0)
# print(f.read())
# f.close()


# f = open('log',mode='wb')
# f.write('附近看到类似纠纷'.encode('utf-8'))
# f.close()

# f = open('log',mode='a',encoding='utf-8')
# f.write('佳琪1')
# f.write('佳琪')
# f.close()
#
# f = open('log',mode='a',encoding='utf-8')
# f.write('佳琪')
# f.close()



# f = open('log',mode='a+',encoding='utf-8')
# f.write('佳琪')
# f.seek(0)
# print(f.read())
# f.close()


# f = open('log',mode='ab')
# f.write('佳琪'.encode('utf-8'))
# f.close()


#功能详解

# obj = open('log',mode='r+',encoding='utf-8')
# content = f.read(3)  # 读出来的都是字符
# f.seek(3)  # 是按照字节定光标的位置
# f.tell() 告诉你光标的位置
# print(f.tell())
# content = f.read()
# print(content)
# f.tell()
# f.readable()  # 是否可读
# line = f.readline()  # 一行一行的读
# line = f.readlines()  # 每一行当成列表中的一个元素，添加到list中
# readline判断结尾：
#   if not f.readline():
#       break   # 不会被空白行歧义，空白行至少会有一个/n，这里的判空会被文件末尾的EOF命中
# f.truncate(4)
# for line in f:
#     print(line)
# f.close()







# f = open('log',mode='a+',encoding='utf-8')
# f.write('佳琪')
# count = f.tell()
# f.seek(count-9)
# print(f.read(2))
# f.close()

# with open('log',mode='r+',encoding='utf-8') as f,\
#         open('log',mode='w+',encoding='utf-8') as f1:

