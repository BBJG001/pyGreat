##PIL转cv2
import cv2
from PIL import Image
import numpy as np
import base64
from io import BytesIO
import time

'''
https://blog.csdn.net/haveanybody/article/details/86494063
PIL和cv2是python中两个常用的图像处理库
    PIL一般是anaconda自带的;
    cv2是opencv的python版本;
    base64在网络传输图片的时候经常用到。
'''


def pil_cv2(img_path):
    image = Image.open(img_path)
    img = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
    return img


def cv2_pil(img_path):
    image = cv2.imread(img_path)
    image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    return image

def pil_base64(image):
    img_buffer = BytesIO()
    image.save(img_buffer, format='JPEG')
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


def base64_pil(base64_str):
    image = base64.b64decode(base64_str)
    image = BytesIO(image)
    image = Image.open(image)
    return image


def cv2_base64(image):
    base64_str = cv2.imencode('.jpg', image)[1].tostring()
    base64_str = base64.b64encode(base64_str)
    return base64_str


def base64_cv2(base64_str):
    imgString = base64.b64decode(base64_str)
    nparr = np.fromstring(imgString, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return image


if __name__ == '__main__':
    testinp = 'data/big.png'

    # # 以PIL读入写出
    # img = Image.open(testinp)
    # img.save('data/bigpil.png')

    # # 以cv2读入写出
    # img = cv2.imread(testinp)
    # cv2.imwrite('data/bigcv2.png', img)

    # 以base64形式突入写出
    with open(testinp, "rb") as f:
        base64_str = base64.b64encode(f.read())

    t00 = time.time()
    for i in range(50):
        with open('data/bigbase64.png', 'wb') as f:
            imgdata = base64.b64decode(base64_str)
            f.write(imgdata)
        objcv2 = cv2.imread('data/bigbase64.png')
    t01 = time.time()

    print('time1:', t01-t00)

    t10 = time.time()
    for i in range(50):
        objcv2_ = base64_cv2(base64_str)
    t11 = time.time()

    print('time2:', t11 - t10)

