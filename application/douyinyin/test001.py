import douyin
from douyin.structures import Topic, Music

# 定义视频下载、音频下载、MongoDB 存储的处理器
video_file_handler = douyin.handlers.VideoFileHandler(folder='./videos')
music_file_handler = douyin.handlers.MusicFileHandler(folder='./musics')
#mongo_handler = douyin.handlers.MongoHandler()
# 定义下载器，并将三个处理器当做参数传递
#downloader = douyin.downloaders.VideoDownloader([mongo_handler, video_file_handler, music_file_handler])
downloader = douyin.downloaders.VideoDownloader([video_file_handler, music_file_handler])
# 循环爬取抖音热榜信息并下载存储
for result in douyin.hot.trend():
    for item in result.data:
        # 爬取热门话题和热门音乐下面的所有视频，每个话题或音乐最多爬取 10 个相关视频。
        downloader.download(item.videos(max=10))