# coding=gbk
# pip install pymupdf
import fitz
import os
from PIL import Image
import shutil


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

    long_canvas.save(out_path)  # ���泤ͼ
    # p.finish()


def getsubimg(f, n, end, o_p, str_='cameraSR'):
    for pg in range(n * 30, min(n * 30 + 30, end)):
        page = f[pg]
        zoom = 2.5  # Խ������ͼ������Խ��
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
    p_name = '2015���°��� ϵͳ�ܹ����ʦ �����'
    path = r'C:\Users\Administrator\Desktop\3-��ϵͳ�ܹ����ʦ\0-����𰸡��ɴ�ӡ��'
    in_p = os.path.join(path, p_name + '.pdf')
    # out_p = os.path.join(path, p_name+'.png')
    out_p = p_name + '.png'
    getimg(in_p)
    # generate_long_image(out_p)

    print('over')
