#----------------- 使用urllib.request.urlretrieve下载
from urllib.request import urlretrieve
urlretrieve(IMAGE_URL, './img/image1.png')
# urlretrieve(资源url， 保存地址）

#----------------- requests写入
import requests
r = requests.get(IMAGE_URL)
with open('./img/image2.png', 'wb', encoding='utf8') as f:   # 注意文件处理模式为‘wb’（以二进制写入）
    f.write(r.content)

# requests分批保存
r = requests.get(IMAGE_URL, stream=True)    # stream loading

with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)