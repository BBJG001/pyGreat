# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 10:04 上午
# @Author  : 百变金刚
# @Content : test for yaml

# 1. 大小写敏感
# 2. 使用缩进表示层级关系
# 3. 缩进时不允许使用Tab，只允许使用空格
# 4. 缩进的空格数目不重要，只要相同层级的元素左对齐即可
# 5. # 表示注释，从它开始到行尾都被忽略

import yaml

def traversePrint(iter, sp=0):
    # 错误方案，'asdf', 'a'都是可迭代的
    # if hasattr(iter, '__iter__'):
    #     for i in iter:
    #         traversePrint(i, sp+2)

    # 次级耦合方案
    if isinstance(iter, dict):
        for item in iter.items():
            if isinstance(item[1], dict):
                print('{}{}'.format(' '*sp, item[0],))
                traversePrint(item[1], sp+2)
            else:
                print('{}{}: {}'.format(' '*sp, item[0], item[1]))
    else:
        print('{}{}'.format(' '*sp, iter))

def testRead1():
    with open('conf/test.yml') as f:
        # conf = yaml.safe_load(f)    # 此处若使用load()将会报警告，被认为是不安全的
        # conf = yaml.load(f, Loader=yaml.SafeLoader)    # 一种方案（https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation）
        conf = yaml.safe_load(f)
    # print(conf)
    traversePrint(conf)

def testRead2():
    # --- 对yaml分块
    with open('conf/obj.yml') as f:
        # conf = yaml.safe_load(f)  # 报错，---把yml文件分成了不止一个流对象，load只能接收一个流对象
        conf = yaml.load_all(f, Loader=yaml.SafeLoader)
        # 此处若使用load()将会报警告，被认为是不安全的

        # 此时conf是一个生成器
        # 这段操作不能放在f的范围之外，因为生成器实时取
        for ci in conf:
            print(ci)

def testWrite1():
    import yaml
    aproject = {'name': 'Silenthand Olleander',
                'race': 'Human',
                'traits': ['ONE_HAND', 'ONE_EYE']
                }
    aproject = {'main.common-arch.thumbnail-service-rs': ['/bfs/{}'.format('sss')]}
    # 将python对象封装为yaml对象
    print(yaml.dump(aproject,))
    '''
    name: Silenthand Olleander
    race: Human
    traits:
    - ONE_HAND
    - ONE_EYE
    '''
    # 写入文件
    with open('conf/writeconf.yml', 'w') as f:
        yaml.dump(aproject, f)

def testWriteAll():
    # 分段（---）写yml
    # 把几个对象分装成list写yml
    obj1 = {"name": "James", "age": 20}
    obj2 = ["Lily", 19]

    with open('writeall.yml', 'w') as f:
        yaml.dump_all([obj1, obj2], f)



if __name__ == '__main__':
    # testWriteAll()
    # testWrite1()
    # testRead2()
    testRead1()
