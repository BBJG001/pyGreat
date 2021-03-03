# coding=gbk
# pip install pymupdf
import fitz
import os
from PIL import Image
import shutil


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

    long_canvas.save(out_path)  # 保存长图
    # p.finish()


def getsubimg(f, n, end, o_p, str_='cameraSR'):
    for pg in range(n * 30, min(n * 30 + 30, end)):
        page = f[pg]
        zoom = 2.5  # 越大，生成图像像素越高
        rotate = int(0)
        trans = fitz.Matrix(zoom, zoom).preRotate(rotate)

        # create raster image of page (non-transparent)
        pm = page.getPixmap(matrix=trans, alpha=False)

        # write a PNG image of the page
        pm.writePNG('{}/{}_{}.png'.format(str_, str_, pg+100))
    generate_long_image(o_p)


def getimg(pdfpath):
    sub_path = pdfpath.split('.')[0]
    if not os.path.exists(sub_path):
        os.mkdir(sub_path)
    # shutil.move(pdfpath, sub_path)
    doc = fitz.open(pdfpath)
    n_doc = doc.pageCount
    str_ = 'cameraSR'
    n_group = int(n_doc / 30) if not n_doc % 30 == 0 else int(n_doc / 30)-1

    for i in range(n_group + 1):
        print('{}/{}'.format(i + 1, n_group + 1))
        if not os.listdir(str_) == None:
            shutil.rmtree(str_)
            os.mkdir(str_)
        getsubimg(doc, i, n_doc, os.path.join(sub_path, 'res_img_' + str(i + 1) + '.png'))
    doc.close()
    shutil.move(pdfpath, sub_path)


if __name__ == '__main__':
    p_name = '2015年下半年 系统架构设计师 答案详解'
    path = r'C:\Users\Administrator\Desktop\3-软考系统架构设计师\0-真题答案【可打印】'
    in_p = os.path.join(path, p_name + '.pdf')
    # out_p = os.path.join(path, p_name+'.png')
    out_p = p_name + '.png'
    getimg(in_p)
    # generate_long_image(out_p)

    print('over')
