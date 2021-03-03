# coding=gbk
# ���ֻ����Linux��
from pdf2image import convert_from_path
import tempfile


def main(filename, outputDir):
    print('filename=', filename)
    print('outputDir=', outputDir)
    images = convert_from_path(filename)
    for index, img in enumerate(images):
        img.save('%s/page_%s.png' % (outputDir, index))

if __name__ == "__main__":
    main(r'C:\Users\Administrator\Desktop\test01.pdf',
         r'C:\Users\Administrator\Desktop\pdfimage')