import json

# 构造生成json的字典
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com',
    'content':[3,5,'49']
}

# 构造json对象
jsonobj = json.dumps(data)
print(jsonobj)
# {"no": 1, "name": "Runoob", "url": "http://www.runoob.com", "content": [3, 5, "49"]}
print(type(jsonobj))
# <class 'str'>
# dumps()之后就编程一个字符串（str）

# 解析jaon对象
jsonfromstr = json.loads(jsonobj)
# {'no': 1, 'name': 'Runoob', 'url': 'http://www.runoob.com', 'content': [3, 5, '49']}
# loads()之后变成了原本的字典形式
print(jsonfromstr['url'])
# http://www.runoob.com

# 保存至json文件
with open('../data/jsondata.json', 'w') as f:
    json.dump(data, f)  # 注意区别上面的dumps()方法，这里的dump()方法是构造json对象并写入文件，dumps()方法只是构造json对象
    # 会转换成字符串写入文件

# 读取json文件
with open('../data/jsondata.json', 'r') as f:
    jsonfromfile = json.load(f)     # 注意区分上面的lodas()方法
    print('jsonfromfile:', jsonfromfile)
    # jsonfromfile: {'no': 1, 'name': 'Runoob', 'url': 'http://www.runoob.com', 'content': [3, 5, '49']}