import os
from bs4 import BeautifulSoup
import re
import time
import subprocess as sp


class PageWork:
    def __init__(self):
        # 获取当前页面（目前市面上好像都是这么做的，先保存到手机，再获取）
        self.update()

    def tapNode(self, text='', name='node', attrs={}):
        cooridinate = self.getPos(text, name, attrs)
        if cooridinate:
            cmd = 'adb shell input tap ' + str(cooridinate[0]) + ' ' + str(cooridinate[1])
            os.system(cmd)
        else:
            raise RuntimeError('未能找到指定元素')
        self.update()

    def slide(self, direct=1, len=100, time=50):
        wsize = self.getWindowSize()
        midx = wsize[0] // 2
        midy = wsize[1] // 2
        if direct == 1:
            nextx, nexty = str(midx), str(midy + len)
        elif direct == 2:
            nextx, nexty = str(midx), str(midy - len)
        elif direct == 3:
            nextx, nexty = str(midx - len), str(midy)
        elif direct == 4:
            nextx, nexty = str(midx + len), str(midy)
        else:
            nextx, nexty = str(midx), str(midy)
        cmd = 'adb shell input swipe {} {} {} {} {}'.format(str(midx), str(midy), nextx, nexty, time)
        os.system(cmd)

    def getPos(self, text='', name='node', attrs={}):
        attrs['text'] = text
        cell = self.content.find(name, attrs=attrs)
        if cell:
            posstr = cell.attrs.get('bounds')
            match = re.search(r'\[(?P<lt0>\d+),(?P<lt1>\d+)\]\[(?P<rb0>\d+),(?P<rb1>\d+)\]', posstr)
            point_lt = [int(match.group('lt0')), int(match.group('lt1'))]
            point_rb = [int(match.group('rb0')), int(match.group('rb1'))]
            centerpos = [(point_lt[0] + point_rb[0]) // 2, (point_lt[1] + point_rb[1]) // 2]
            return centerpos
        else:
            return None

    def update(self):
        os.popen('adb shell uiautomator dump /sdcard/ui.xml').read()
        # popen是异步的，在执行的同时会开启下面，如果下面调用了上面的结果，可能会出问题
        # read()是在主进程操作的，这就相当于进行了阻塞，必须等popen结束了之后才能read(),保护了下方代码执行的安全性
        # os.system('adb shell uiautomator dump /sdcard/ui.xml')
        os.popen(
            r'adb pull /sdcard/ui.xml E:\Workplace\Workplace_Python\wp_project\pyGreat\application\ctrlmobile').read()
        with open(r'E:\Workplace\Workplace_Python\wp_project\pyGreat\application\ctrlmobile\ui.xml',
                  encoding='utf8') as f:
            self.content = BeautifulSoup(f.read(), 'lxml')

    def getWindowSize(self):
        cmd = 'adb shell wm size'
        res_size = os.popen(cmd).read()
        match = re.search(r'size: (?P<width>\d+)x(?P<height>\d+)', res_size)
        return (int(match.group('width')), int(match.group('height')))

    def save(self, path):
        with open(path, 'w') as f:
            f.write(self.content.__str__())


def operate1():
    obj = PageWork()
    for i in range(1000):
        print('Epoach', i + 1, '------------------------------------------------------------')
        try:
            obj.tapNode('免费获取积分')
        except RuntimeError as e:
            print('积分：', e)
        try:
            obj.tapNode('立即领取')
        except RuntimeError as e:
            print('领取：', e)
        time.sleep(30)
        obj.update()
        for i in range(3):
            if obj.getPos(attrs={'resource-id': 'com.strategyapp:id/tt_video_ad_close_layout'}):
                break
            else:
                time.sleep(5)
        try:
            obj.tapNode(attrs={'resource-id': 'com.strategyapp:id/tt_video_ad_close_layout'})
        except RuntimeError as e:
            print('退出：', e)


def operate2():
    obj = PageWork()
    for i in range(50):
        print(i)
        try:
            obj.tapNode('继续获得积分')
        except RuntimeError as e:
            print('积分：', e)
        time.sleep(25)
        obj.update()
        for i in range(3):
            if obj.getPos(attrs={'resource-id': 'com.strategyapp:id/tt_video_ad_close_layout'}):
                break
            else:
                time.sleep(5)
        try:
            obj.tapNode(attrs={'resource-id': 'com.strategyapp:id/tt_video_ad_close_layout'})  # 右上角x
        except RuntimeError as e:
            print('退出：', e)


def operate3():
    obj = PageWork()
    for i in range(50):
        print(i)
        try:
            obj.tapNode('继续获得积分')
        except RuntimeError as e:
            print('积分：', e)
        time.sleep(25)
        obj.update()
        for i in range(8):
            if obj.tapNode(attrs={'class': "android.widget.ImageView"}):
                break
            else:
                time.sleep(5)
        try:
            obj.tapNode(attrs={'class': "android.widget.ImageView"})  # 左上角x
        except RuntimeError as e:
            print('退出：', e)


def operate4():
    obj = PageWork()
    obj.slide(2)
    # for i in range(1000):
    #     print(i)
    #     try:
    #         obj.tapNode('继续获得积分')
    #     except RuntimeError as e:
    #         print('积分：', e)
    #     time.sleep(25)
    #     obj.update()
    #     for i in range(8):
    #         if obj.tapNode(attrs={'class': "android.widget.ImageView"}):
    #             break
    #         else:
    #             time.sleep(5)
    #     try:
    #         obj.tapNode(attrs={'class': "android.widget.ImageView"})  # 左上角x
    #     except RuntimeError as e:
    #         print('退出：', e)


if __name__ == '__main__':
    # operate1()
    # operate2()
    operate3()
    # operate4()

    # print(obj.getPos('福利手游'))
    # print(obj.getPos('游戏'))

    # obj.tapNode('福利手游')

    # # print(soup)
    # cell = soup.find('node', attrs={'text':'福利手游'})
    # print(cell.attrs.get('bounds'))
    # match = re.search(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', r0.text, flags=re.M)
