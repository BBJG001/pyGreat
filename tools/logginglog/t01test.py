# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 5:43 下午
# @Author  : 百变金刚
# @Content : logging basic record
# @Reference: https://www.cnblogs.com/Eva-J/articles/7228075.html#_label14
# output2console; output2file; remove in time
import logging
import time
from logging.handlers import TimedRotatingFileHandler

import yaml

# 级别	何时使用
# DEBUG	详细信息，一般只在调试问题时使用。(>=该level的log info将被输出)
# INFO	证明事情按预期工作。
# WARNING	（默认）某些没有预料到的事件的提示，或者在将来可能会出现的问题提示。例如：磁盘空间不足。但是软件还是会照常运行。
# ERROR	由于更严重的问题，软件已不能执行一些功能了。
# CRITICAL	严重错误，表明软件已不能继续运行了。

# handler配置level不能生效
# 在创建 handler之前将默认root logger的handler拉低
# logging.root.setLevel(logging.NOTSET)

def test2Terminal():
    logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.DEBUG)
    logging.debug('debug 信息')
    logging.info('info 信息')
    logging.warning('warning 信息')
    logging.error('error 信息')
    logging.critical('critial 信息')

def test2File():
    logging.basicConfig(
        level=logging.DEBUG,#控制台打印的日志级别
        filename='new.log',
        filemode='w',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
        #a是追加模式，默认如果不写的话，就是追加模式
        format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        #日志格式
    )
    logging.debug('debug 信息')
    logging.info('info 信息')
    logging.warning('warning 信息')
    logging.error('error 信息')
    logging.critical('critial 信息')

def testBoth():
    # !!! name, 指定了那么才会重新生成一个，不指定默认就只有一个（root）
    # logging的操作实际上是通过一个 logging.root 的对象的操作，level不过不指定默认为warning
    # 对于logging.getLogger(), 如果不显性的指定一个name，则默认返回logging.root   默认level为warning
    # 在对logger对象添加handler，且handler指定了level，Logger对logger的level的设置规则为选择更高级别的level，那么如果handler的级别低，则无法生效
    # 解决方法就是在自定义之前把logging，也就是logging.root的level设置为低级别，那么最终级别将取决于设定的handler
    # logging.root.setLevel(logging.NOTEST)
    # 有者将其封装进一个对象，该对象可以即又

    # 创建一个logger
    id=1
    logger = logging.getLogger('logger_{}'.format(id))  # 如果不指定name将不会新建logger，而是返回一个初始创建的公共logger

    # 创建一些设置
    formatter = logging.Formatter('%(levelname)-8s %(name)-12s: %(message)s')   # 设置日志打印格式
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('logs/testboth.log')

    # 创建一个stream handler，用于输出到控制台
    ch = logging.StreamHandler()   # 定义一个Handler打印INFO及以上级别的日志到sys.stderr

    # 绑定配置
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 这个setLevel 不work
    fh.setLevel(logging.INFO)
    ch.setLevel(logging.INFO)

    # 为logger绑定输出handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('all1')
    logger.debug('Quick zephyrs blow, vexing daft Jim.')
    logger.info('How quickly daft jumping zebras vex.')
    logger.warning('Jail zesty vixen who grabbed pay from quack.')
    logger.info('all2')
    logger.error('The five boxing wizards jump quickly.')
    # logger2.warning('Jail zesty vixen who grabbed pay from quack.')
    # logger2.error('The five boxing wizards jump quickly.')

def testBoth2():
    '''
    不太秀美，写法上兼容'logging'
    :return:
    '''
    plog = 'logs/testboth.log'
    # 写log文件logging设定
    logging.basicConfig(
        level=logging.INFO, # log文件的level
        format='%(levelname)-8s %(asctime)s: %(message)s',
        datefmt='%m-%d %H:%M',
        filename=plog,
        filemode='w')
    # 输出到控制台的loging设定
    console = logging.StreamHandler()   # 定义一个Handler打印INFO及以上级别的日志到sys.stderr
    console.setLevel(logging.INFO)  # 控制台的level
    formatter = logging.Formatter('%(levelname)-8s: %(message)s')   # 设置日志打印格式
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

# handler配置level不能生效
# 在创建 handler之间将默认root logger的handler拉低
# logging.root.setLevel(logging.NOTSET)

def testConfLog():
    logging_config_file = './conf/logging_config.yaml'

    # 设置日志
    with open(logging_config_file, 'r') as f:
        config = yaml.safe_load(f.read())

    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.info('global log')

# 写入多个logger
def test2variousfile():
    logger = logging.getLogger('alogger')  # 如果不指定name将不会新建logger，而是返回一个初始创建的公共logger

    # 创建一些设置
    formatter = logging.Formatter('%(levelname)-8s %(name)-12s: %(message)s')   # 设置日志打印格式
    # 创建一个handler，用于写入日志文件
    fh1 = logging.FileHandler('logs/various1.log')
    fh2 = logging.FileHandler('logs/various2.log')

    # 绑定配置
    fh1.setFormatter(formatter)
    fh2.setFormatter(formatter)

    # 为logger绑定输出handler
    logger.addHandler(fh1)
    logger.addHandler(fh2)

    logger.info('all1')
    logger.debug('Quick zephyrs blow, vexing daft Jim.')
    logger.info('How quickly daft jumping zebras vex.')
    logger.warning('Jail zesty vixen who grabbed pay from quack.')
    logger.info('all2')
    logger.error('The five boxing wizards jump quickly.')


# 滚动日志，清除过期日志——TimedRotatingFileHandler
def testTimeRotatingLog():
    #日志打印格式
    log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
    formatter = logging.Formatter(log_fmt)
    #创建TimedRotatingFileHandler对象
    log_file_handler = TimedRotatingFileHandler(filename="logs/timerotate.log", when="S", interval=1, backupCount=1)
    #log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    #log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger('timeRotate')
    log.addHandler(log_file_handler)
    #循环打印日志
    log_content = "test log"
    count = 1
    while count < 500:
        log.error('No.{} log'.format(count))
        time.sleep(0.01)
        count = count + 1
    # log.removeHandler(log_file_handler)

    '''
    filename：日志文件名的prefix；
    when：是一个字符串，用于描述滚动周期的基本单位，字符串的值及意义如下：
        “S”: Seconds
        “M”: Minutes
        “H”: Hours
        “D”: Days
        “W”: Week day (0=Monday)，这里应该为 when='W0' or W1 W2 ，，，
    “midnight”: Roll over at midnight
    interval: 滚动周期，单位有when指定，比如：when=’D’,interval=1，表示每天产生一个日志文件；
    backupCount: 表示日志文件的保留个数，超过之后会依次删除最早创建的,=0就不会删除。。。
    ！！！程序停止再次启动能把上次的接上，emmm，很nice
    '''


if __name__ == '__main__':
    test2variousfile()
    # testTimeRotatingLog()
    # testConfLog()
    # testBoth()
    # test2Terminal()
    # test2File()