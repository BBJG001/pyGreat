import re

def test01():

    line = '  <img src="/Users/baibianjingang/Library/Application Support/typora-user-images/image-20201206141711751.png" alt="image-20201206141711751" style="zoom:50%;" />'
    upres = 'https://ttt.com/zyd-store/xxx.png'



    reg = re.compile('.*<img src="(.*?)".*')
    match = reg.findall(line)
    # matchsearch = reg.search(line).groups()
    print(match)
    # print(matchsearch)
    line = line.replace(match[0], upres)
    print(line)

    file = match[0]
    print(file.rsplit('/', 1)[-1])

if __name__ == '__main__':
    test01()