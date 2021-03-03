# 根据元素获取坐标
# python+uiautomator+adb dump（Android手机自动化） 根据文本寻找所在坐标并点击
# https://blog.csdn.net/u014520313/article/details/79218897
# ! -*- coding:utf-8 -*-
# ! /usr/bin/python

import tempfile
import os
import re
import xml.etree.cElementTree as et
import time
import random


def tap_coord_by_name_id(deviceid, attrib_name, text_name):
    time.sleep(6)
    os.popen('adb -s' + ' ' + deviceid + ' ' + 'shell uiautomator dump --compressed /data/local/tmp/uidump.xml')
    os.popen('adb -s' + ' ' + deviceid + ' ' + r'pull data/local/tmp/uidump.xml E:\code\Smart\uidump.xml')

    source = et.parse("uidump.xml")
    root = source.getroot()

    for node in root.iter("node"):
        if node.attrib[attrib_name] == text_name:
            bounds = node.attrib["bounds"]
            pattern = re.compile(r"\d+")
            coord = pattern.findall(bounds)
            Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
            Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
            os.popen('adb  -s' + ' ' + deviceid + ' ' + 'shell input tap %s %s' % (str(Xpoint), str(Ypoint)))