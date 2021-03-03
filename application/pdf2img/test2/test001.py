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
        zoom = 4.0 # Խ������ͼ������Խ��
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
    # out_path = os.path.dirname(img_path)  # ��һ���ļ�Ŀ¼

    # ��ȡ����ͼƬ
    ims = [Image.open(os.path.join(img_path, fn)) for fn in os.listdir(img_path) if fn.endswith('.png')]
    width, height = ims[0].size  # ȡ��һ��ͼƬ�ߴ�
    long_canvas = Image.new(ims[0].mode, (width, height * len(ims)))  # ����ͬ��n�ߵİ�ͼƬ
    # p = ProgressBar().start()
    # ƴ��ͼƬ
    for i, image in enumerate(ims):
        long_canvas.paste(image, box=(0, i * height))
        # p.update(i+1)
        print(i)

    long_canvas.save(out_path)  # ���泤ͼ
    # p.finish()

<<<<<<< HEAD
def test1():
=======
if __name__ == '__main__':
>>>>>>> dev2
    p_name = '1__�ǳ���4Dʱ����ֳ����µ��¿���Ա��ȫ��ɢ�о�_¬��'
    path = r'C:\Users\Administrator\Desktop\�½��ļ���'
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
