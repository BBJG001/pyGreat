from application.Videodownload.getVideo import *

if __name__ == '__main__':
    url = 'http://www.wodedy.net/play/145-0-1.html'
    path = r'E:\Test\JYZJ\over'

    checkenv()
    download(url, path)

