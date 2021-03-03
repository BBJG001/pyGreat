import urllib.request
import shutil
import json
import time
import os


def download_articles(p_numbers, p_titles, prefix, output_dir):
    for p, t in zip(p_numbers, p_titles):
        print('processing {}-{}'.format(p, t))
        ret = os.system('wget -P {} -E -H -k -p https://zhuanlan.zhihu.com/p/{}'.format(prefix, p))
        if ret != 0:
            raise ValueError('wget error! p={}'.format(p))

        html_file = os.path.join(prefix, 'zhuanlan.zhihu.com', 'p', '{}.html'.format(p))
        with open(html_file, 'r+') as f:
            html_string = f.read()
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
    p_numbers = []
    p_titles = []
    offset = 0
    while True:
        url = 'https://zhuanlan.zhihu.com/api/columns/{}/articles?include=data&limit=100&offset={}'.format(zhuanlan,
                                                                                                           offset)
        html_string = urllib.request.urlopen(url).read()
        content = json.loads(html_string)
        p_numbers.extend([item['id'] for item in content['data']])
        p_titles.extend([item['title'] for item in content['data']])
        if len(content['data']) < 100:
            break
        else:
            offset += 100

    return p_numbers, p_titles


if __name__ == '__main__':
    zhuanlan = 'reinforcementlearning'
    prefix = 'working_dir'
    output_dir = 'output_dir'

    shutil.rmtree(prefix)
    os.makedirs(prefix, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    p_numbers, p_titles = get_p_numbers(zhuanlan)
    download_articles(p_numbers, p_titles, prefix, output_dir)