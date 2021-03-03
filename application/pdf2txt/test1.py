# -*- coding: utf-8 -*-
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO     # 原本是cString

def convert_pdf_to_txt(path,save_name):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    try:
        with open("%s"%save_name,"wb") as f:#格式化字符串还能这么用！，wb可以写入，只w可能会因为pdf中的特殊符号报错
            print(type(str))
            f.write(str.encode('utf-8'))
            # for i in str:
            #     f.write(i)
        print("%s Writing Succeed!"%save_name)
    except:
        print("Writing Failed!")


convert_pdf_to_txt(r'E:\ZYD\temporary\DesktopMirror\新建文件夹\20191126\paper\1124\Improved Multi-Agent Reinforcement Learning.pdf',"magent.txt")