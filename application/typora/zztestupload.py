from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

from application.typora import *  # 是为了导入__init__.py中的常量



def upload(src):
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    secret_id = SECRET_ID
    secret_key = SECRET_KEY
    region = REGION
    endpoint = ENDPOINT
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Endpoint=endpoint)
    # 2. 获取客户端对象
    client = CosS3Client(config)

    #### 文件流简单上传（不支持超过5G的文件，推荐使用下方高级上传接口）
    # 强烈建议您以二进制模式(binary mode)打开文件,否则可能会导致错误
    with open(src, 'rb') as fp:
        response = client.put_object(
            Bucket=BUCKET,
            Body=fp,
            Key='typora/{}'.format(src.rsplit('/', 1)[-1]), # 亚马逊的对象存储没有文件夹的概念，不清腾讯云对象存储是不是； / 作为文件名的一部分，通过命名空间实现了类似文件夹的效果
            StorageClass='STANDARD',
            EnableMD5=False
        )
    print(response)
    if response['ETag']:
        return 'https://zydstore-1258477714.cos.ap-beijing.myqcloud.com/typora/{}'.format(src.rsplit('/', 1)[-1])


if __name__ == '__main__':
    src = '/Users/baibianjingang/Library/Application Support/typora-user-images/image-20201206141711751.png'
    url = upload(src)
    print(url)