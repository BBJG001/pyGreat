import urllib.request
import requests
import shutil
import json
import time
import os

os.environ["PATH"] += os.pathsep + r'C:\Program Files\wkhtmltopdf\bin'

def download_articles(p_numbers, p_titles, prefix, output_dir):
    for p, t in zip(p_numbers, p_titles):
        print('processing {}-{}'.format(p, t))
        # ret = os.system('wget -P {} -E -H -k -p https://zhuanlan.zhihu.com/p/{}'.format(prefix, p))
        # if ret != 0:
        #     raise ValueError('wget error! p={}'.format(p))

        url = 'https://zhuanlan.zhihu.com/p/{}'.format(p)
        print(url)
        html_string = requests.get(
            url=url,
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
            }
        ).text

        html_file = os.path.join(prefix, '{}.html'.format(p))

        with open(html_file, 'w', encoding='utf8') as f:
            # html_string = f.read()
            # wkhtmltopdf ignores images wrapped by noscript - weird
            html_string = html_string.replace('<noscript>', '')
            html_string = html_string.replace('</noscript>', '')
            f.seek(0)
            f.write(html_string)
            f.truncate()

        output_file = os.path.join(output_dir, '{}.pdf'.format(p))
        ret = os.system('wkhtmltopdf {} {}'.format(html_file, output_file))
        if ret != 0:
            raise ValueError('wkhtmltopdf error! p={}'.format(p))


def get_p_numbers(zhuanlan):
    urls = []
    # p_titles = []
    offset = 0
    while True:
        url = 'https://zhuanlan.zhihu.com/api/columns/{}/articles?include=data&limit=100&offset={}'.format(zhuanlan,
                                                                                                           offset)
        html_string = requests.get(
            url=url,
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
            }
        ).text
        content = json.loads(html_string)
        urls.extend([item['url'] for item in content['data']])
        # p_titles.extend([item['title'] for item in content['data']])
        if len(content['data']) < 100:
            break
        else:
            offset += 100
    return urls


if __name__ == '__main__':
    zhuanlan = 'reinforcementlearning'
    # prefix = 'working_dir'
    # output_dir = 'output_dir'
    #
    # shutil.rmtree(prefix)
    # os.makedirs(prefix, exist_ok=True)
    # os.makedirs(output_dir, exist_ok=True)

    urls = get_p_numbers(zhuanlan)
    for u in urls:
        print(u)

    # download_articles(p_numbers, p_titles, prefix, output_dir)