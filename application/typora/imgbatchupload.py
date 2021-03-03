# -*- coding=utf-8
# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 BucketName-APPID 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
import os
import re

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import yaml
from types import SimpleNamespace

BUCKET = 'zydstore-1258477714'

class Worker():
    def __init__(self, sid, skey, region, endpoint):
        self.secret_id = sid
        self.secret_key = skey
        self.region = region
        self.endpoint = endpoint

        config = CosConfig(Region=region, SecretId=sid, SecretKey=skey, Endpoint=endpoint)
        # 2. 获取客户端对象
        self.client = CosS3Client(config)

    def doAFile(self, file):
        print('=====do {}'.format(file))
        res = ''
        with open(file, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if '<img src="/Users' in line:
                    reg = re.compile('.*<img src="(.*?)".*')
                    match = reg.findall(line)
                    if match:
                        url = self.upload(match[0])
                        line = line.replace(match[0], url)
                    print(line)
                res+=line
        # save res
        with open(file, 'w') as f:
            f.write(res)

    def upload(self, src):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)

        #### 文件流简单上传（不支持超过5G的文件，推荐使用下方高级上传接口）
        # 强烈建议您以二进制模式(binary mode)打开文件,否则可能会导致错误
        with open(src, 'rb') as fp:
            response = self.client.put_object(
                Bucket=BUCKET,
                Body=fp,
                Key='typora/{}'.format(src.rsplit('/', 1)[-1]),
                # 亚马逊的对象存储没有文件夹的概念，不清腾讯云对象存储是不是； / 作为文件名的一部分，通过命名空间实现了类似文件夹的效果
                StorageClass='STANDARD',
                EnableMD5=False
            )
        print(response)
        if response['ETag']:
            return 'https://zydstore-1258477714.cos.ap-beijing.myqcloud.com/typora/{}'.format(src.rsplit('/', 1)[-1])

def main():
    with open('conf.own') as f:
        conf = yaml.safe_load(f)
    conf = SimpleNamespace(**conf)

    processer = Worker(conf.secret_id,conf.secret_key, conf.region, conf.endpoint)

    dirp = '/Users/baibianjingang/Downloads/Wp_work/wpftest/zyddocu/5mac'
    fs = os.listdir(dirp)
    for fi in fs:
        if not fi.endswith('.md'):
            continue
        fp = os.path.join(dirp, fi)

        processer.doAFile(fp)



if __name__ == '__main__':
    main()