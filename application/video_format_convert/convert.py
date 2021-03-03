import os

def convert(pin, pout, aim):
    fname = pin.split('/')[-1].split('.')[0]
    print(fname)
    cmd = 'ffmpeg -i ' + pin + ' ' + pout+'/'+fname+'.'+aim
    print('converting. . .')
    # os.popen()命令会转为后台运行，先完成后面的命令的执行
    # os.popen(cmd)
    os.system(cmd)
    print('convert finished')


if __name__ == '__main__':
    # 定义输入文件路径
    path_in = r'C:\Users\Administrator\Desktop\wk.mp4'
    # 定义输出文件路径
    path_out = r'C:\Users\Administrator\Desktop\wk.mp3'
    # 拼接cmd下的命令
    cmd = 'ffmpeg -i '+path_in+' '+path_out
    # 执行cmd命令
    os.system(cmd)
    print('over')

    # convert(path_in, path_out)