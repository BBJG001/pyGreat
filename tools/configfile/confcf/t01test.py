import configparser


def testBase():
    cf = configparser.ConfigParser()
    cf.read('./data/project.conf')
    print(cf.get(section='environment', option='env'))
    print('if 没有：', cf.get(section='environment', option='env2', fallback='通过fallback设置的if没有的返回值')) # if 没有
    # 格式要 [] 加 下面属性 一共两层，在cf中分别识别命名为section和option；
    # 开头没有 [] 直接写属性报错

    secs = cf.sections()
    opts = cf.options('local')


    cf.set(section='environment', option='env2', value='probtest')  # 此时在本程序中属性已经被更改，但还并未持久胡按到文件
    print(cf.get('environment', 'env2'))

def testAdd():
    pass

def testSave():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45', 'Compression': 'yes', 'CompressionLevel': '9'}
    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']
    topsecret['Port'] = '50022'  # mutates the parser
    topsecret['ForwardX11'] = 'no'  # same here
    config['DEFAULT']['ForwardX11'] = 'yes'
    with open('./data/testsave.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    testSave()
    # testBase()