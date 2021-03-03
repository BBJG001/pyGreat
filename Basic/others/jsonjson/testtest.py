import json

# 构造生成json的字典
data = {
    '一班': ['张一', '张二', '张三', '张四'],
    '二班': ['王一', '王二', '王三', '王四'],
    '三班': ['李一', '李二', '李三', '李四'],
    '四班': ['赵一', '赵二', '赵三', '赵四']
}

with open('jsondata2.json', 'w', encoding='utf8') as f:
    json.dump(data, f)
    # 会转换成字符串写入文件

# 读取数据
with open('jsondata2.json', 'r', encoding='utf8') as f:
    jsonfromfile = json.load(f)
    for item in jsonfromfile.values():
        for cell in item:
            print(cell)
        print()
