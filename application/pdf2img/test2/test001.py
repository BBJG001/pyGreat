# coding=gbk
# pip install pymupdf
import fitz
import os
from PIL import Image
import shutil
from progressbar import ProgressBar

def getimg(pdfpath):

    doc = fitz.open(pdfpath)
    str_ = 'cameraSR'
    # p = ProgressBar().start()

    if not os.listdir(str_)==None:
        shutil.rmtree(str_)
        os.mkdir(str_)

    for pg in range(doc.pageCount):
        page = doc[pg]
        zoom = 4.0 # 越大，生成图像像素越高
        rotate = int(0)
        trans = fitz.Matrix(zoom, zoom).preRotate(rotate)

        # create raster image of page (non-transparent)
        pm = page.getPixmap(matrix=trans, alpha=False)

        # write a PNG image of the page
        pm.writePNG('{}/{}_{}.png'.format(str_,str_,pg))
        print(pg)
        # p.update(pg+1)
    # p.finish()

def generate_long_image(out_path, img_path=r'E:\Workplace\Workplace_Python\wp_project\pdf2img\test2\cameraSR'):
    # out_path = os.path.dirname(img_path)  # 上一级文件目录

    # 获取单个图片
    ims = [Image.open(os.path.join(img_path, fn)) for fn in os.listdir(img_path) if fn.endswith('.png')]
    width, height = ims[0].size  # 取第一个图片尺寸
    long_canvas = Image.new(ims[0].mode, (width, height * len(ims)))  # 创建同宽，n高的白图片
    # p = ProgressBar().start()
    # 拼接图片
    for i, image in enumerate(ims):
        long_canvas.paste(image, box=(0, i * height))
        # p.update(i+1)
        print(i)

    long_canvas.save(out_path)  # 保存长图
    # p.finish()

<<<<<<< HEAD
def test1():
=======
if __name__ == '__main__':
>>>>>>> dev2
    p_name = '1__非常规4D时变火灾场景下地下矿人员安全疏散研究_卢娜'
    path = r'C:\Users\Administrator\Desktop\新建文件夹'
    in_p = os.path.join(path, p_name+'.pdf')
    out_p = os.path.join(path, p_name+'.png')
    getimg(in_p)
    generate_long_image(out_p)

<<<<<<< HEAD
    print('over')

def test2Imgs():
    pdfpath = ''
    savepath = ''
    getimg()

if __name__ == '__main__':
    test1()
=======
    print('over')
>>>>>>> dev2
