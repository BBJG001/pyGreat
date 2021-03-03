import pickle

obj = {1:'a', 2:'b'}

# 将指定的Python对象通过pickle序列化作为bytes对象返回，而不是将其写入文件
pickleobj = pickle.dumps(obj)
# b'\x80\x03}q\x00(K\x01X\x01\x00\x00\x00aq\x01K\x02X\x01\x00\x00\x00bq\x02u.'

# 将通过pickle序列化后得到的字节对象进行反序列化，转换为Python对象并返回
reobj = pickle.loads(pickleobj)
# {1: 'a', 2: 'b'}

# 将指定的Python对象通过pickle序列化后写入打开的文件对象中，等价于`Pickler(file, protocol).dump(obj)`
with open('../data/pickle.txt', 'wb') as f:
    pickle.dump(obj, f)
with open('../data/pickle.data', 'wb') as f:
    pickle.dump(obj, f)

# 从打开的文件对象中读取pickled对象表现形式并返回通过pickle反序列化后得到的Python对象
with open('../data/pickle.txt', 'rb') as f:
    res1 = pickle.load(f)
print(type(res1))   # <class 'dict'>
print(res1)         # {1: 'a', 2: 'b'}
with open('../data/pickle.data', 'rb') as f:
    res2 = pickle.load(f)
print(type(res2))   # <class 'dict'>
print(res2)         # {1: 'a', 2: 'b'}
