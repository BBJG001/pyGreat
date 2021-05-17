# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 9:02 下午
# @Author  : 百变金刚
# @Content : use of argparse
# https://docs.python.org/zh-cn/3/library/argparse.html
import argparse

def baseUse():
    # 搞一个收集信息的对象（个人理解）
    parser = argparse.ArgumentParser(description='Process some integers.')
    '''
    prog - 程序的名称（默认：sys.argv[0]，就是所在的py文件名?）
    usage - 描述程序用途的字符串（默认值：从添加到解析器的参数生成）
    description - 在参数帮助文档之前显示的文本（默认值：无）
    epilog - 在参数帮助文档之后显示的文本（默认值：无）
    parents - 一个 ArgumentParser 对象的列表，它们的参数也应包含在内
    formatter_class - 用于自定义帮助文档输出格式的类
    prefix_chars - 可选参数的前缀字符集合（默认值：'-'）
    fromfile_prefix_chars - 当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值：None）
    argument_default - 参数的全局默认值（默认值： None）
    conflict_handler - 解决冲突选项的策略（通常是不必要的）
    add_help - 为解析器添加一个 -h/--help 选项（默认值： True）
    allow_abbrev - 如果缩写是无歧义的，则允许缩写长选项 （默认值：True）
    exit_on_error - 决定当错误发生时是否让 ArgumentParser 附带错误信息退出。 (默认值: True)
    '''

    # 添加参数add_argument
    ## 创建位置参数；'integers'是一个name？
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    ## 创建选项；-s --sum 是一系列flags？
    parser.add_argument('-s', '--sum', dest='accumulate', action='store_const', const=sum, default=max,
                        help='sum the integers (default: find the max)')    # 不传就计算max，传s就计算sum
    '''
    name or flags - 命令行中指定参数名，一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
    dest - 属性名，被添加到 parse_args() 所返回对象上的属性名。位置参数默认就是这个里面的 add_argument('bar') bar；可选参数（--foo）就是foo
    type - 命令行参数应当被转换成的类型。
    default - 默认值，The value produced if the argument is absent from the command line and if it is absent from the namespace object.
    required - 是否必须，此命令行选项是否可省略 （仅选项可用）。
    help - 一个此选项作用的简单描述。
    action - 当参数在命令行中出现时使用的动作基本类型。
    nargs - 命令行参数应当消耗的数目；可以指定一个int值，?: 0或1个，*: 0个或多个（没什么意思，默认？），+: 1个或多个，没有会报错
    const - 被一些 action 和 nargs 选择所需求的常数。  
    choices - 可用的参数的容器。
    metavar - 展示该参数的可以的示例
    '''
    # 将收集到的信息封装一个对象（个人理解）
    # args = parser.parse_args()

    # 这样可以在程序内直接加参数
    args = parser.parse_args(['--sum', '7', '-1', '42'])
    args = parser.parse_args('--sum 7 -1 42'.split())
    args.key = 'xxx'

    print(args.integers)    # [1, 2, 3]
    print(args.accumulate(args.integers))


def parse_args():
    """
    demo use
    :return:
    """
    parser = argparse.ArgumentParser(description="bucket_diff envs")
    parser.add_argument(dest="filenames", metavar="filename", nargs="*")
    parser.add_argument("-c", dest="yaml_file", metavar="yaml_file", default="apis/app_svr.yaml")
    parser.add_argument("-rec", "--env_record", dest="env_record", metavar="env_record: uat, pre, prod", default="prod")
    parser.add_argument("-rep", "--env_replay", dest="env_replay", metavar="env_replay: uat, pre, prod", default="pre")
    parser.add_argument("-缩写", "--缩写的全写",
                        dest="调用的时候的属性值，无该属性默认是全写",
                        metavar="参数示例这个参数可以是[1,2,3]中的值; ",
                        help='帮助信息',
                        required=False, # 是不是必须的
                        default='默认值')
    #  -缩写 参数示例这个参数可以是[1,2,3]中的值, --缩写的全写 参数示例这个参数可以是[1,2,3]中的值
    #                         帮助信息
    parser.add_argument("-cp", "--color_replay", dest="color_replay", metavar="color_replay", default=None)
    parser.add_argument("-n", "--api_size", type=int, dest="api_size", metavar="api num from ops-log", default=10)
    return parser.parse_args()

def testParse_args():
    args = parse_args()
    args.api_size = 100
    print(type(args))
    print(args)

if __name__ == '__main__':
    testParse_args()
    # baseUse()

