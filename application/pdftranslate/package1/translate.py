# coding=gbk
import hashlib
import random
import urllib.parse
import requests
from concurrent import futures
from io import StringIO


from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
# https://gist.github.com/jmcarp/7105045
# from pdfminer.pdfinterp import process_pdf
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

# process_pdf被改变之后的替换方式
def process_pdf(rsrcmgr, device, fp, pagenos=None, maxpages=0, password='', caching=True, check_extractable=True):
  interpreter = PDFPageInterpreter(rsrcmgr, device)
  for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,
              caching=caching, check_extractable=check_extractable):
    interpreter.process_page(page)
  return


def read_from_pdf(file_path):
    '''
    解析pdf文件
    原本是用process_pdf写的，官方文档说改成了PDFPage.get_pages()，直接改换之后效果并不理想
    '''
    with open(file_path, 'rb') as file:
        resource_manager = PDFResourceManager()
        return_str = StringIO()
        lap_params = LAParams()
        device = TextConverter(resource_manager, return_str, laparams=lap_params)
        process_pdf(resource_manager, device, file)
        # PDFPage.get_pages(resource_manager, device, file)

        device.close()
        content = return_str.getvalue()
        return_str.close()
        return content

def get_from_pdf(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 10
    caching = True
    pagenos = set()
    # process_pdf一种比较认同的改写吧
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str


def create_sign(q, salt, appid=20191114000357043, key='JR0hpjF3v0XvhuqHCccL'):
    '''
    制造签名
    '''
    sign = str(appid) + str(q) + str(salt) + str(key)
    md5 = hashlib.md5()
    md5.update(sign.encode('utf-8'))
    return md5.hexdigest()


def create_url(q, url):
    '''
    根据参数构造query字典
    '''
    fro = 'auto'
    to = 'zh'
    salt = random.randint(32768, 65536)
    sign = create_sign(q, salt)
    url = url + '?appid=' + str(20191114000357043) + '&q=' + urllib.parse.quote(q) + '&from=' + str(fro) + '&to=' + str(
        to) + '&salt=' + str(salt) + '&sign=' + str(sign)
    return url


def translate(q):
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    url = create_url(q, url)
    r = requests.get(url)
    txt = r.json()
    if txt.get('trans_result', -1) == -1:
        print('程序已经出错，请查看报错信息：\n{}'.format(txt))
        return '这一部分翻译错误'
    return txt['trans_result'][0]['dst']


def clean_data(data):
    '''
    将输入的data返回成为段落组成的列表
    '''
    data = data.replace('\n\n', '闲谈后')
    data = data.replace('\n', ' ')
    return data.split('闲谈后')


def _main(pdf_path, txt_path):
    # try:
    data = read_from_pdf(pdf_path)
    data_list = clean_data(data)
    # print(data_list)
    with futures.ThreadPoolExecutor(20) as excuter:
        zh_txt = excuter.map(translate, data_list)
    # zh_txt = [translate(txt) for txt in data_list]
    zh_txt = list(zh_txt)
    article = '\n\n'.join(zh_txt)
    article = article.replace('这一部分翻译错误\n\n', '')
    print(article)
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(article)
    # except Exception:
    #     return -1


if __name__ == '__main__':
    # appid = XXXX  # 填入你的 appid ，为int类型
    # key = XXXX  # 填入你的 key ，为str类型
    doc_in = r'E:\ZYD\temporary\DesktopMirror\ReinforcementLearning\20200404\References\DuelingDQN.pdf'
    doc_out = doc_in.split('.')[0]+'.txt'
    # print(doc_out)
    _main(doc_in, doc_out)  # 填入 pdf 路径与翻译完毕之后的 txt 路径
