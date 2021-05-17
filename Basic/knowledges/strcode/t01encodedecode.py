# coding='utf8'

s = '汉字'
print(s)
# 汉字
s2b = s.encode('utf-8')     # 用utf8编码成二进制
print(s2b)
# b'\xe6\xb1\x89\xe5\xad\x97'
b2gbk = s2b.decode('gbk')   # 用gbk解码发现乱码
print(b2gbk)
# 姹夊瓧
b2utf8 = s2b.decode('utf-8')    # 用utf8解码正确get到原本文字
print(b2utf8)
# 汉字
