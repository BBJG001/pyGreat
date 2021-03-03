import requests
import os

HEADER = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


def get_urls(url):
    res = requests.get(url, headers=HEADER, verify=False).text
    ll = res.split('.ts')
    end = int(ll[-2][-3:])

    u_base = url.rsplit('/', 1)[0]
    # print(u_base)
    uls = [u_base+'/out'+str(i).zfill(3)+'.ts' for i in range(end+1)]
    return uls


# 取出下载链接并下载
def download(ts_urls, download_path):
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    for i in range(0, len(ts_urls)):
        u = ts_urls[i]
        try:
            response = requests.get(headers=HEADER, url=u, stream=True, verify=False)
        except Exception as e:
            print("异常请求：%s" % e.args)
            return
        ts_path = download_path +'\\'+ u.rsplit('/',1)[-1]

        with open(ts_path, "wb+") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(u.rsplit('/',1)[-1], 'finished')


# 将已经下载的ts文件的路径进行排序
def file_walker(path):
    file_list = []
    for root, dirs, files in os.walk(path):  # 生成器
        for fn in files:
            p = str(root + '/' + fn)
            file_list.append(p)
    file_list.sort(key=lambda x: int(x[-6:-3]))
    return file_list


# 将所有下载好的ts文件组合成一个文件
# ts_path: 下载好的一堆ts文件的文件夹
# combine_path: 组合好的文件的存放位置
# file_name: 组合好的视频文件的文件名
def combine(ts_path, combine_path, file_name):
    file_list = file_walker(ts_path)
    file_path = combine_path + file_name + '.ts'
    with open(file_path, 'wb+') as fw:
        for i in range(len(file_list)):
            fw.write(open(file_list[i], 'rb').read())


if __name__ == '__main__':
    save_path = r'E:\Test\JYZJ'
    # url = 'https://www5.laqddc.com/hls/2018/12/23/D4hqwI4o/playlist.m3u8'
    url = 'https://www5.laqddc.com/hls/2018/12/23/vsrHWn6B/playlist.m3u8'
    # url = 'https://www5.laqddc.com/hls/2018/12/23/tXt94W9N/playlist.m3u8'
    # url = 'https://www5.laqddc.com/hls/2018/12/23/QaL4NBkC/playlist.m3u8'

    urls = get_urls(url)
    download(urls, save_path+'\\2')
    combine(save_path+'\\1', save_path+'\\over', "2")


# url = 'https://www.www5.laqddc.com/hls/2018/12/23/tXt94W9N/out000.ts'