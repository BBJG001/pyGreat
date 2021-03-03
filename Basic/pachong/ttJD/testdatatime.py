from datetime import datetime # 导入datetime模块
import time


stamp = datetime(2017, 10, 7) # 生成一个datetime对象
str(stamp) # 转换  #结果显示：'2017-10-07 00:00:00'

stamp.strftime('%Y-%m-%d') # 结果显示：'2017-10-07'

stamp.strftime("%w") # 结果显示：'6',表示当前日期为星期六

value = '2017/10/7'
datetime.strptime(value, '%Y/%m/%d')

dt1 = datetime.now()
dt2 = datetime.strptime('2017-01-01 14:00:01', '%Y-%m-%d %H:%M:%S')
print(dt1)
print(dt2)
print('time.time():',time.time())
tstr = time.strftime('%Y-%m-%d %H:%M:%S')
print(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))

def test():
    for i in range(3):
        if 3<5:
            pass
        try:
            b = 3/0
        except:
            pass
        print(i)

test()
