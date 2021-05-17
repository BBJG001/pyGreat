# coding='utf8'
# 上一行可以指定本文件的默认编码
import sys

# python3的默认编码方式是utf8
# windows的默认编码方式是gbk
# 大多数的非win系统的默认编码方式是utf8

def getDefault():
    return sys.getdlopenflags()



def endecodeTest():
    s = '汉字'
    print(s)
    # 汉字
    s2b = s.encode('utf-8')  # 用utf8编码成二进制
    print(s2b)
    # b'\xe6\xb1\x89\xe5\xad\x97'
    b2gbk = s2b.decode('gbk')  # 用gbk解码发现乱码
    print(b2gbk)
    # 姹夊瓧
    b2utf8 = s2b.decode('utf-8')  # 用utf8解码正确get到原本文字
    print(b2utf8)
    # 汉字

def testFileTranscode():
    source = '../../data/source_transcode.txt'
    output = '../../data/output_transcode.txt'
    with open(source, encoding='utf8') as fin:
        content = fin.read()
    with open(output, 'w', encoding='gbk') as fout:
        fout.write(content)

def testOutput():
    source = '../../data/source_transcode.txt'
    output = '../../data/output_transcode.txt'
    with open(source, encoding='gbk') as fin:
        content = fin.read()
    with open(output, 'w', encoding='utf8') as fout:
        fout.write(content)



if __name__ == '__main__':
    testFileTranscode()