# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 11:36 上午
# @Author  : 百变金刚
# @Content : note for time module

import time

'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示    12/18/20
%X 本地相应的时间表示    11:40:39
%Z 当前时区的名称
%% %号本身

'''

def testbasic():
    time.sleep(0.5)

    print('float的时间戳，单位是s，1970年1月1日00:00:00开始按秒计算的偏移量')
    print(time.time())  #
    print(type(time.time()))

    print('\n格式日期')
    print(time.strftime('%x %X'))   # 格式控制参见上文表示
    print(time.strftime("%Y-%m-%d %X"))
    print(time.strftime("%Y-%m-%d %H-%M-%S"))

    print('\n时间元组:localtime将一个时间戳转换为当前时区的struct_time')
    time_t = time.localtime()
    print(time_t)
    print(type(time_t))
    print(time_t.tm_wday)   # 一周内的天序号（0表示周一）
    print(time_t.tm_isdst)   # 是否为夏时令（默认0）

def timeConvert():
    #时间戳-->结构化时间(time.struct_time)
    #time.gmtime(时间戳)    #UTC时间，与英国伦敦当地时间一致
    #time.localtime(时间戳) #当地时间。例如我们现在在北京执行这个方法：与UTC时间相差8小时，UTC时间+8小时 = 北京时间
    time.gmtime(1500000000)
    # time.struct_time(tm_year=2017, tm_mon=7, tm_mday=14, tm_hour=2, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=195, tm_isdst=0)
    time.localtime(1500000000)
    # time.struct_time(tm_year=2017, tm_mon=7, tm_mday=14, tm_hour=10, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=195, tm_isdst=0)

    #结构化时间-->时间戳　
    #time.mktime(结构化时间)
    time_tuple = time.localtime(1500000000)
    time.mktime(time_tuple)
    1500000000.0

    #结构化时间-->字符串时间
    # time.strftime("格式定义","结构化时间")  结构化时间参数若不传，则显示当前时间
    time.strftime("%Y-%m-%d %X")
    # '2017-07-24 14:55:36'
    time.strftime("%Y-%m-%d",time.localtime(1500000000))
    # '2017-07-14'

    #字符串时间-->结构化时间
    #time.strptime(时间字符串,字符串对应格式)
    time.strptime("2017-03-16","%Y-%m-%d")
    # time.struct_time(tm_year=2017, tm_mon=3, tm_mday=16, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=75, tm_isdst=-1)
    time.strptime("07/24/2017","%m/%d/%Y")
    # time.struct_time(tm_year=2017, tm_mon=7, tm_mday=24, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=205, tm_isdst=-1)

    #结构化时间 --> %a %b %d %H:%M:%S %Y串
    # time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串
    time.asctime(time.localtime(1500000000))
    'Fri Jul 14 10:40:00 2017'
    time.asctime()
    'Mon Jul 24 15:18:33 2017'

    #时间戳 --> %a %b %d %H:%M:%S %Y串
    #time.ctime(时间戳)  如果不传参数，直接返回当前时间的格式化串
    time.ctime()
    'Mon Jul 24 15:19:07 2017'
    time.ctime(1500000000)
    'Fri Jul 14 10:40:00 2017'

if __name__ == '__main__':
    testbasic()