# 参考https://blog.csdn.net/qq_41192383/article/details/86559337
import cv2
import os
from application.processbar.progressbar import bar3 # 我自己写的模块

# 传入视频全路径，自动在视频路径下生成同名文件夹，将图片保存在里面
def video2img1(pathv):
    file_name = pathv.split(os.sep)[-1].split('.')[0]  # os.sep当前系统的路径分隔符，也可以用'\\'
    out_floder = pathv.split('.')[0]    # path全路径去掉最后的后缀，后面依据这个生成跟视频同名的文件夹
    if not os.path.exists(out_floder):
        os.makedirs(out_floder, exist_ok=True)
    vc = cv2.VideoCapture(pathv)  # 读入视频文件
    print(vc.get(cv2.CAP_PROP_FPS))     # 获取帧频
    print(vc.get(cv2.CAP_PROP_FRAME_WIDTH))     # 获取视频画面横向分辨率
    print(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))    # 获取视频画面的竖向分辨率
    n_frame = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))     # 视频总帧数
    print(n_frame)
    c = 0   # 帧索引
    rval = vc.isOpened()    # 检测vc是否初始化成功，如果成功则返回True，如为初始化则通过vc.open()打开

    while rval:  # 如果初始化成功，就可以循环读取视频帧
        c = c + 1
        rval, frame = vc.read() # 返回两个值，首先返回一个bool值，如果能正确读取帧，则为True，否则为False.可以通过检查该返回值来检查视频的结尾.再返回一个值，为每一帧的图像，该值是一个三维矩阵
        pic_name = file_name + '_' + str(c).zfill(4) + '.jpg'   # 拼接图片名称
        if rval:
            save_path = os.path.join(out_floder, pic_name)
            cv2.imwrite(save_path, frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
            # if c%50==0 or c==n_frame:
            #     print('\r[', c, '/', n_frame, ']', 'finished', end='')
            # print('\r处理进度 : %.2f%%\t' % (c / n_frame * 100), end='')
            # print('['+'>'*int(c/n_frame*60)+'-'*int(60-c/n_frame*60)+']', end='')
            bar3(c, n_frame, 40, '处理进度')
            cv2.waitKey(1)
        else:
            break
    vc.release()
    print('\nsave_success')
    print()


def video2img2(pathv, pathimgs):
    # 如果穿件来的是一批视频的文件夹
    if os.path.isdir(pathv):
        videos = os.listdir(pathv)
        for video in videos:
            # 这里可以通过video.endwith()加入格式判断
            for video_name in videos:
                file_name = video_name.split('.')[0]
                folder_name = pathv + file_name
                os.makedirs(folder_name, exist_ok=True)
                vc = cv2.VideoCapture(pathv + video_name)  # 读入视频文件
                c = 0
                rval = vc.isOpened()

                while rval:  # 循环读取视频帧
                    c = c + 1
                    rval, frame = vc.read()
                    pic_path = folder_name + '/'
                    if rval:
                        cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg',
                                    frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                        cv2.waitKey(1)
                    else:
                        break
                vc.release()
                print('save_success')
                print(folder_name)
        pass
    elif os.path.isfile(pathv):
        pass
    else:
        print('invalid error')
    video_path = r'F:\test\video1/'
    videos = os.listdir(pathv)
    for video_name in videos:
        file_name = video_name.split('.')[0]
        folder_name = pathv + file_name
        os.makedirs(folder_name, exist_ok=True)
        vc = cv2.VideoCapture(pathv + video_name)  # 读入视频文件
        c = 0
        rval = vc.isOpened()

        while rval:  # 循环读取视频帧
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name + '/'
            if rval:
                cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                cv2.waitKey(1)
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)


def save_img():
    video_path = r'F:\test\video1/'
    videos = os.listdir(video_path)
    for video_name in videos:
        file_name = video_name.split('.')[0]
        folder_name = video_path + file_name
        os.makedirs(folder_name, exist_ok=True)
        vc = cv2.VideoCapture(video_path + video_name)  # 读入视频文件
        c = 0
        rval = vc.isOpened()

        while rval:  # 循环读取视频帧
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name + '/'
            if rval:
                cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                cv2.waitKey(1)
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)

<<<<<<< HEAD
def testV2I():
    pv = 'data/1606998019134272.mp4'
    video2img1(pv)



if __name__ == '__main__':
    # pv = r'E:\Test\v2idemo.flv'
    testV2I()
=======

if __name__ == '__main__':
    # pv = r'E:\Test\v2idemo.flv'
    pv = r'E:\Test\historyimg.flv'

    video2img1(pv)
>>>>>>> dev2
