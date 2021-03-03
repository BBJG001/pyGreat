# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 4:29 下午
# @Author  : 百变金刚
# @Content :
import re

def testGroup():
    datereg = re.compile(r'^(?:(?!0000)[0-9]{4}([-/.]?)(?:(?:0?[1-9]|1[0-2])\1(?:0?[1-9]|1[0-9]|2[0-8])|(?:0?[13-9]|1[0-2])\1(?:29|30)|(?:0?[13578]|1[02])\1(?:31))|(?:[0-9]{2}(?:0[48]|[2468][048]|[13579][26])|(?:0[48]|[2468][048]|[13579][26])00)([-/.]?)0?2\2(?:29))$')


    # 通过在小括号()中一部分匹配规则，这样可以在匹配结果中通过索引单独提取这部分结果
    match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
    print(match.group())    # 获取整个匹配结果
    # 021523, Date: Feb/12/2017
    print(match.group(1))   # 提取索引1的结果（第1个括号），索引从1开始
    # 021523
    print(match.group(2))   # 提取索引2的结果（第2个括号）
    # Date: Feb/12/2017

    # 通过?P<名称>可以为匹配结果指定key/名称/属性索引，可以在结果中通过这么名称访问分组匹配结果
    match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")

    print(match.group('id'))
    # 021523
    print(match.group('date'))
    # Date: Feb/12/2017
    print(match.groupdict())
    print(match.groups())

def testWhether(choose):
    if choose==1:
        sl = [
            '<x1="10" x2="11" x3="13">',
            '<x1="10" >',
            '<x1="10" x2="11" >',
            '<x1="10" x3="13">'
        ]
        reg = re.compile(r'(?i)<x1=([\'\"\"]?)(?P<x1>\d+)\1\s*(?:x2=([\'\"\"]?)(?P<x2>\d+)\2)?\s*(?:x3=([\'\"\"]?)(?P<x3>\d+)\3)?[^>]*>')
        for s in sl:
            match = re.search(reg, s).groupdict()
            print(match)
    elif choose==2:
        sl = [
            "My phone number is 12356897. ",
            "My phone number is 081-12356897. ",
        ]
        for s in sl:
            phoneNumRegex_2 = re.compile(r"((?P<area>\d\d\d)-)?(?P<num>\d\d\d\d\d\d\d\d)")
            mo = phoneNumRegex_2.search(s).groupdict()
            print(mo)

def testUrl():
    url='https://i0.hdslb.com/bfs/album/fa1e423624206ac8aa9dfb95595174ac541ccc2f.jpg@358w_358h_85q_!dynamic-android-multiple.webp'
    url2 = 'https://i0.hdslb.com/bfs/album/fa1e423624206ac8aa9dfb95595174ac541ccc2f.jpg'
    reg = re.compile(r'.*//(?P<domain>.+)/bfs/(?P<bucket>.+)/(?P<image>[^@]+)@?(?P<params>.*)?')
    result = re.match(reg, url2)
    print(result.groups())

if __name__ == '__main__':
    # testWhether(2)
    testGroup()